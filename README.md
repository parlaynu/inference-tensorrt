# Inference Using Nvidia TensorRT

This repository has tools and guidelines for converting ONNX models to [TensortRT](https://developer.nvidia.com/tensorrt)
engines and running classification inference using the exported model. 

The tools include:

* bash script wrapper for trtexe 
* running inference using the exported engine

The `tools` directory contains the source code in python for the onnx2trt conversion and the inference. It builds 
on the tools in [inference-onnx](https://github.com/parlaynu/inference-onnx). Models converted to ONNX using the 
`inference-onnx` project can be used as input to the tools here.

The `platforms` directory contains the tooling to build docker images with the tools and packages to
run the conversion and inference.

Each platform needs to do its own conversion as the TensorRT engine is a binary format matched to the GPU
on the system.

## The Tools

### Convert ONNX to TensorRT

This tools converts an ONNX model to a TensorRT engine. It is a wrapper script around the Nvidia tool `trtexec`.

The full usage is:

    $  ./onnx2trt.sh 
    Usage: onnx2trt.sh model.onnx

The containers built by the platform tools mount a directory called `models` from the host file system which
can be used as the source for ONNX model files.

### Running Inference

The tool `classify-tvm.py` runs inference on the exported TVM model. The full usage is:

    $ ./classify-trt.py -h
    usage: classify-trt.py [-h] [-l LIMIT] [-r RATE] engine dataspec
    
    positional arguments:
      engine                path to the tensorrt engine file
      dataspec              the data source specification
    
    options:
      -h, --help            show this help message and exit
      -l LIMIT, --limit LIMIT
                            maximum number of images to process
      -r RATE, --rate RATE  requests per second

A simple run using a camera server from the `inference-onnx` project looks like this:

    $ ./classify-trt.py -l 10 ../models/resnet18-1x3x224x224.trt tcp://192.168.24.31:8089
    loading engine...
    - input shape: [1, 3, 224, 224]
    - output shape: [1, 1000]
    00 image_0000 640x480x3
       315 @ 51.36
    01 image_0001 640x480x3
       315 @ 25.14
    02 image_0002 640x480x3
       315 @ 50.38
    03 image_0003 640x480x3
       315 @ 37.04
    04 image_0004 640x480x3
       315 @ 27.28
    05 image_0005 640x480x3
       315 @ 46.95
    06 image_0006 640x480x3
       315 @ 41.22
    07 image_0007 640x480x3
       315 @ 52.79
    08 image_0008 640x480x3
       315 @ 53.13
    09 image_0009 640x480x3
       315 @ 47.75
    runtime: 0 seconds
        fps: 13.13

See the [inference-onnx](https://github.com/parlaynu/inference-onnx) project for details on the camera server.

## The Platforms

Under the `platforms` directory, there is a directory for each platform supported. This project builds a single 
container that can be used by all the tools. 

In the platform directory are the tools to build the conversion container and launch it.

Use the `build.sh` script to build the container. This does everything automatically including downloading the 
TVM source code and compiling it and building and installing the python package. This takes some time on the
JetsonNano and RaspberryPi4 platforms.

    ./build.sh

Use the `run-latest.sh` script to launch the container with the correct parameters:

    $ ./run-latest.sh
    
    root@eximius:/workspace# ls
    inference  models  onnx2trt

The `models` directory is mounted from the host system from ${HOME}/Workspace/models. Place any models you want to convert
into this directory so they are accessible from this container.

## References

* https://docs.nvidia.com/deeplearning/tensorrt/api/python_api/index.html
* https://documen.tician.de/pycuda/


