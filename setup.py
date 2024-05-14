from typing import List
from setuptools import find_packages, setup


def get_requires() -> List[str]:
    return [
        "soundfile==0.12.1",
        "soxr==0.3.7",
        "torch==2.3.0",
        "torchaudio==2.3.0",
        "numpy==1.26.4",
        "transformers==4.40.2",
        "webrtcvad==2.0.10",
    ]


setup(
    name="asr_cli",
    entry_points = {
        'console_scripts': ['asr-cli=asr_cli.main:main'],
    },
    version="0.dev",
    description="Simple ASR CLI tool",
    package_dir={"": "src"},
    packages=find_packages("str", include=["asr_cli", "asr_cli.*"]),
    include_package_data=True,
    install_requires=get_requires(),
    python_requires=">=3.8",
    zip_safe=False
)
