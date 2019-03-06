# mlagents-xvfb-fail

Repro of failing to get mlagents work with xvfb in docker

## Hardware

- AMD Ryzen Threadripper 1920X 12-Core Processor
- Nvidia GeForce GTX 1080 Ti
- Dell screens (NOTE: this machine has screens)

## Software

- Ubuntu 18.04.2 LTS
- Nvidia drivers 415.27
- CUDA 10.0
- Docker 18.09.3
- nvidia-docker 2.0.3

## Out of docker working repro

From repo root run:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python test.py
```

## Out of docker issue with xvfb repro

From repo root run:

```bash
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python test.py --docker_training
```

## Docker issue with xvfb repro

From repo root run:

```bash
docker build -f .dockerfile -t mlagents-xvfb-fail .
nvidia-docker run mlagents-xvfb-fail
```
