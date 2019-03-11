FROM ubuntu:18.04

# Install needed apt stuff
RUN apt-get update && apt-get install -y \
    xvfb \
    mesa-utils

# Copy our files into docker image
COPY . /mlagents-xvfb-fail

# Run test with docker training
CMD xvfb-run -s "-screen 0 640x480x24" /mlagents-xvfb-fail/gridworld/gridworld.x86_64 --port 20742