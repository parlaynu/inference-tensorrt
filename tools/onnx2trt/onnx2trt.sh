#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    echo "Usage: $(basename $0) model.onnx"
    exit
fi

ONNX_MODEL=$1
TRT_MODEL="${ONNX_MODEL%.*}".trt

if [ ! -f "${ONNX_MODEL}" ]; then
    echo Error: onnx model not found
    exit 1
fi


/usr/src/tensorrt/bin/trtexec --onnx="${ONNX_MODEL}" --saveEngine="${TRT_MODEL}"

