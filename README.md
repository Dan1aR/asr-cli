# asr-cli
Simple ASR CLI tool

## Installation
```
python3 -m pip install -e .
```

## Install from [Test PyPI](https://test.pypi.org/project/asr-cli-dan1ar/0.0.2/)
```
python3 -m pip install -i https://test.pypi.org/simple/ asr-cli-dan1ar==0.0.2
```

## Use as a CLI tool
```
asr-cli --wav_path examples/resources/tts-example.wav
```

## Usage with Docker
```bash
./run.sh # build and run docker container
# Откроется bash в контейнере, далее работаем в нем
cd /_mnt # Переходи в директорию, которую примаунтили к контейнеру на запуске
# Распознаем пример
asr-cli --wav_path examples/resources/tts-example.wav
```
