# mlagents-xvfb-fail

Repro of failing to get mlagents work with xvfb in docker

## Hardware

- AMD Ryzen Threadripper 1920X 12-Core Processor
- Nvidia GeForce GTX 1080 Ti
- Dell screens (NOTE: this machine has screens)

## Software

- Ubuntu 18.04.2 LTS
- Nvidia drivers 415.27
- Docker 18.09.3

## Docker fails (ubuntu 18.04)

From repo root run:

```bash
docker build -f fails.dockerfile -t xvfb-fails .
docker run xvfb-fails
```

## Docker works (ubuntu 16.04)

From repo root run:

```bash
docker build -f works.dockerfile -t xvfb-works .
docker run xvfb-works
```
