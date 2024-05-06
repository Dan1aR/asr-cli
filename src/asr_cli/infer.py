"""
    Simple asr infernece
"""
from asr_cli.asr.asr import ASR
from asr_cli.utils.audio import read_audio


def infer(
    wav_path: str,
    asr_recognizer: ASR
) -> str:
    samples, _ = read_audio(wav_path, sampling_rate=16_000)
    # skipping VAD for now
    segments = [samples]

    asr_results = asr_recognizer.process(segments=segments)

    return " ".join(asr_results)

