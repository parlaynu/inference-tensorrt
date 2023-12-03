#!/usr/bin/env bash

# make sure we're in the right location
RUN_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd ${RUN_DIR}

# a stamp to tag the image with
STAMP=$(date +%s)

# collect the files needed
rm -rf local
mkdir -p local
cp -r ../../tools/inference local
cp -r ../../tools/onnx2trt local

# build the image
docker build \
    --tag local/inference-tensorrt:${STAMP} \
    --tag local/inference-tensorrt:latest \
    .

