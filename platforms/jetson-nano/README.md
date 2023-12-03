# Platform: Jetson Nano

| Item    | Version             |
| ------- | ------------------- |
| Hardare | Jetson Nano         |
| Memory  | 4 GBytes            |
| L4T     | 32.7.4              |
| OS      | Ubuntu 18.04.6 LTS  |
| Jetpack | 4.6.4-b39           |

## Setup

### Operating System

Install your Operating system as described in detail [here](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

### Additional OS Setup

A few other configuration items you might want to do are listed in this section.

Update the operating system:

    $ sudo apt update
    $ sudo apt dist-upgrade
    $ sudo reboot

Turn off the GUI so you have more RAM available:

    $ sudo systemctl set-default multi-user
    $ sudo reboot

If you wish to turn it back on at any time, run this command:

    $ sudo systemctl set-default graphical

Disable In-Memory Swap

    $ sudo systemctl disable nvzramconfig.service

Setup Swap File

    $ SWAPLOCATION=/swapfile
    $ SWAPSIZE=4G
    $ sudo fallocate -l ${SWAPSIZE} ${SWAPLOCATION}
    $ sudo chmod 600 ${SWAPLOCATION}
    $ sudo mkswap ${SWAPLOCATION}
    $ sudo swapon ${SWAPLOCATION}

Add to /etc/fstab:

    /swapfile  none  swap  sw  0  0

And reboot:

    $ sudo reboot

Install the latest pip:

    $ wget https://bootstrap.pypa.io/pip/3.6/get-pip.py
    $ sudo -H python3 get-pip.py
    $ rm get-pip.py

Install jtop:

    $ sudo -H python3 -m pip install -U jetson-stats
    $ sudo reboot

### Docker

This repository uses docker to build the environments and run the tools. I've taken this approach as it can
be fully automated and isolated from the host environment - it should work reliably no matter what you have 
installed on your host.

Docker is installed and ready to use as part of the standard install.

Add your user to the docker group so you can interact with the system without being root or
running sudo all the time:

    $ sudo usermod -aG docker <username>

Log out and back in and you'll be ready to go. Test by running the hello-world example:

    $ docker run hello-world

