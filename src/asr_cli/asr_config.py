import dataclasses
from enum import Enum

from asr_cli.asr.asr import ASR
from asr_cli.asr.asr_wav2vec2_ctc import Wav2Vec2CTCASR

class ASRArch(Enum):
    wav2vec2ctc = "wav2vec2ctc"

@dataclasses.dataclass
class ASRConfig:
    processor_path: str
    model_path: str


Wav2Vec2CTCConfig = ASRConfig(
    processor_path="wav2vec2ctc_processor.pt",
    model_path="wav2vec2ctc.pt",
)

def get_asr(asr_arch: ASRArch) -> ASR:
    if asr_arch == ASRArch.wav2vec2ctc:
        return Wav2Vec2CTCASR()
