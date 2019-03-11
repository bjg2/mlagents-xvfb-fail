FROM ubuntu:18.04

# Install needed apt stuff
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    xvfb \
    mesa-utils

# Install needed python dependencies
RUN pip3 install \
    mlagents-envs==0.6.2 \
    portpicker==1.3.1

# Copy our files into docker image
COPY . /mlagents-xvfb-fail

# Run test with docker training
CMD cd mlagents-xvfb-fail && python3 test.py