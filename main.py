import warnings
from argparse import ArgumentParser, Namespace

from asr_cli.asr_config import ASRArch
from asr_cli.asr_getter import get_asr
from asr_cli.infer import infer

warnings.filterwarnings("ignore")


def _get_args() -> Namespace:
    parser = ArgumentParser() 
    parser.add_argument(
        "--wav_path",
        type=str,
        help="wav_path to process"
    )
    return parser.parse_args()


def main(wav_path: str):
    asr_recognizer = get_asr(ASRArch.wav2vec2ctc, remote=True)

    result = infer(wav_path, asr_recognizer)
    print(result)


if __name__ == "__main__":
    args = _get_args()
    main(args.wav_path)