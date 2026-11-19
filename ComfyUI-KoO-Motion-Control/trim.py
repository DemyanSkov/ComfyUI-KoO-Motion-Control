# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 MiniMax H3 Audio T8 contributors.
# Extraction retains the installed trim implementation; only schema node_id is namespaced.
from __future__ import annotations
from collections.abc import Mapping
import json
import torch
import torch.nn.functional as torch_functional
from comfy_api.latest import io
CATEGORY = "T8/MiniMax H3"


def validate_audio(audio: Mapping, name: str = "audio") -> tuple[torch.Tensor, int]:
    if not isinstance(audio, Mapping):
        raise ValueError(f"{name} must be a connected AUDIO value")
    waveform = audio.get("waveform")
    sample_rate = audio.get("sample_rate")
    if not isinstance(waveform, torch.Tensor) or sample_rate is None:
        raise ValueError(f"{name} is missing waveform or sample_rate")
    if waveform.ndim != 3:
        raise ValueError(f"{name} must use [batch,channels,samples], got {tuple(waveform.shape)}")
    if waveform.shape[0] < 1 or waveform.shape[1] < 1 or waveform.shape[2] < 1:
        raise ValueError(f"{name} is empty")
    if waveform.shape[0] != 1:
        raise ValueError(f"{name} must have batch size 1 for MiniMax H3")
    return waveform, int(sample_rate)


def trim_av_output(frames: torch.Tensor, start_seconds: float, duration_seconds: float, audio=None,
                   fps: float = 24.0, frame_count: int = 0):
    if frames.ndim != 4:
        raise ValueError(f"frames must be IMAGE [N,H,W,C], got {tuple(frames.shape)}")
    if start_seconds < 0 or duration_seconds <= 0 or fps <= 0:
        raise ValueError("trim start must be nonnegative; duration and fps must be positive")
    if type(frame_count) is not int or frame_count < 0:
        raise ValueError("frame_count must be a nonnegative integer; 0 keeps legacy duration rounding")
    start_frame = round(start_seconds * fps)
    # A compiler's discrete video endpoint is independent of the requested
    # audio interval. Keep old callers' rounding and PCM coordinates unchanged.
    frame_count = frame_count or max(1, round(duration_seconds * fps))
    end_frame = start_frame + frame_count
    if end_frame > frames.shape[0]:
        raise ValueError(
            f"Requested output frames [{start_frame}:{end_frame}] exceed decoded frame count {frames.shape[0]}"
        )
    trimmed_frames = frames[start_frame:end_frame]

    trimmed_audio = None
    if audio is not None:
        waveform, sample_rate = validate_audio(audio)
        start_sample = round(start_seconds * sample_rate)
        sample_count = round(duration_seconds * sample_rate)
        sliced = waveform[..., start_sample : start_sample + sample_count]
        if sliced.shape[-1] < sample_count:
            sliced = torch_functional.pad(sliced, (0, sample_count - sliced.shape[-1]))
        trimmed_audio = {"waveform": sliced, "sample_rate": sample_rate}

    report = json.dumps(
        {
            "start_seconds": start_seconds,
            "requested_duration_seconds": duration_seconds,
            "fps": fps,
            "start_frame": start_frame,
            "frame_count": frame_count,
            "actual_video_duration_seconds": frame_count / fps,
        },
        ensure_ascii=False,
        indent=2,
    )
    return trimmed_frames, trimmed_audio, report


class MiniMaxH3OutputTrimT8(io.ComfyNode):
    @classmethod
    def define_schema(cls):
        return io.Schema(
            node_id="KoOMiniMaxH3OutputTrimT8", display_name="MiniMax H3 Output Trim (T8)", category=CATEGORY,
            description="Applies Duration Planner trim metadata to decoded IMAGE frames and optional AUDIO.",
            inputs=[
                io.Image.Input("frames"),
                io.Float.Input("start_seconds", default=0.0, min=0.0, max=900.0, step=0.001),
                io.Float.Input("duration_seconds", default=5.0, min=0.04, max=None, step=0.001),
                io.Float.Input("fps", default=24.0, min=1.0, max=240.0, step=0.001, advanced=True),
                io.Audio.Input("audio", optional=True),
                io.Int.Input("frame_count", default=0, min=0, max=None, optional=True, advanced=True,
                             tooltip="Exact video frame count; 0 keeps duration rounding. Audio still uses the requested seconds."),
            ],
            outputs=[io.Image.Output("frames"), io.Audio.Output("audio"), io.String.Output("report_json")],
        )

    @classmethod
    def execute(cls, frames, start_seconds, duration_seconds, fps, audio=None, frame_count=0):
        return io.NodeOutput(*trim_av_output(frames, start_seconds, duration_seconds, audio, fps, frame_count))
