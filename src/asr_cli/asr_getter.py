from asr_cli.asr.asr import ASR
from asr_cli.asr.asr_wav2vec2_ctc import Wav2Vec2CTCASR
from asr_cli.asr_config import ASRArch, Wav2Vec2CTCConfig, Wav2Vec2CTCRemoteConfig


def get_asr(asr_arch: ASRArch, remote: bool = False) -> ASR:
    if asr_arch == ASRArch.wav2vec2ctc:
        config = Wav2Vec2CTCRemoteConfig if remote else Wav2Vec2CTCConfig
        return Wav2Vec2CTCASR(config)
    else:
        raise ValueError(f"Unknown {asr_arch=}")
