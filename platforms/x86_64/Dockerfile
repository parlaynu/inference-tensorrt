FROM nvidia/cuda:12.2.2-cudnn8-devel-ubuntu22.04

RUN mkdir -p /workspace

WORKDIR /workspace

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y python3 python3-pip \
                            libnvinfer-bin python3-libnvinfer \
                            git wget && \
    rm -rf /var/lib/apt/lists/*

COPY files/requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

RUN git clone https://github.com/parlaynu/inference-onnx.git && \
    cd inference-onnx && \
    git checkout 74a032633c283134c3677ef241b17e31fe3179b8 && \
    cd .. && \
    mv inference-onnx/tools/inference . && \
    rm -rf inference-onnx

COPY local/onnx2trt /workspace/onnx2trt
COPY local/inference /workspace/inference/

ENTRYPOINT ["/bin/sh", "-c", "exec \"$0\" \"$@\""]
CMD ["/bin/bash"]


