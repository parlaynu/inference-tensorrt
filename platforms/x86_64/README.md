# Platform: AMD64 with Nvidia RTX2060

| Item    | Version                       |
| ------- | ----------------------------- |
| CPU     | AMD Ryzen 7 3700X             |
| GPU     | Nvidia GeForce RTX 2060 SUPER |
| Memory  | 32 GBytes                     |
| OS      | Ubuntu 22.04                  |

## Setup

### Docker

This repository uses docker to build the environments and run the tools. I've taken this approach as it can
be fully automated and isolated from the host environment - it should work reliably no matter what you have 
installed on your host.

Install docker following these [instructions](https://docs.docker.com/engine/install/ubuntu/)

Then install the nvidia container toolkit following these [instructions](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)

Once installed, add your user to the docker group so you can interact with the system without being root or
running sudo all the time:

    $ sudo usermod -aG docker <username>

Log out and back in and you'll be ready to go. Test by running the nvidia-smi example:

    $ docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi

