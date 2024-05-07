import dataclasses
from enum import Enum


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

Wav2Vec2CTCRemoteConfig = ASRConfig(
    processor_path="jonatasgrosman/wav2vec2-large-xlsr-53-russian",
    model_path="jonatasgrosman/wav2vec2-large-xlsr-53-russian",
)
