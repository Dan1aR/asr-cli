from typing import List
from setuptools import find_packages, setup

def get_requires() -> List[str]:
    return [
        "torch==2.3.0",
        "torchaudio==2.3.0",
        "numpy",
        "transformers",
        "librosa"
    ]


setup(
    name="asr_cli",
    version="0.dev",
    description="Simple ASR CLI tool",
    package_dir={"": "src"},
    packages=find_packages("str", include=["asr_cli", "asr_cli.*"]),
    include_package_data=True,
    install_requires=get_requires(),
    python_requires=">=3.8",
)
