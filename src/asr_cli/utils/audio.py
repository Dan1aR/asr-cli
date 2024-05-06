from typing import Tuple

import torch
import torchaudio


def read_audio(
    path: str, sampling_rate: int = 16_000,
) -> Tuple[torch.Tensor, int]:
    wav, sr = torchaudio.load(path)
    if wav.size(0) > 1:
        wav = wav.mean(dim=0, keepdim=True)
    
    if sampling_rate != sr:
        transform = torchaudio.transforms.Resample(
            orig_freq=sr, new_freq=sampling_rate
        )
        wav = transform(wav)
        sr = sampling_rate


    return wav.squeeze(0), sr
