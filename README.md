# mlagents-xvfb-fail

Repro of failing to get mlagents work with xvfb in docker

## Hardware

- AMD Ryzen Threadripper 1920X 12-Core Processor
- Nvidia GeForce GTX 1080 Ti

## Software

- Ubuntu 18.04.2 LTS
- Nvidia drivers 415.27
- CUDA 10.0
- Docker 18.09.3
- nvidia-docker 2.0.3

## Repro steps

From repo root run:

- `docker build -f .dockerfile -t mlagents-xvfb-fail .`
- `nvidia-docker run mlagents-xvfb-fail`