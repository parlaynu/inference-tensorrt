FROM nvcr.io/nvidia/l4t-cuda:10.2.460-runtime

RUN mkdir -p /workspace

WORKDIR /workspace

COPY local/nvidia-l4t-apt-source.list /etc/apt/sources.list.d/
COPY local/jetson-ota-public.asc /etc/apt/trusted.gpg.d/
RUN rm -f /etc/apt/sources.list.d/cuda.list

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get upgrade -y

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3.6 python3.6-dev python3.6-venv \
                            build-essential \
                            python3-libnvinfer python3-numpy \
                            git wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://bootstrap.pypa.io/pip/3.6/get-pip.py && \
    python3.6 get-pip.py && \
    rm get-pip.py

COPY files/requirements.txt requirements.txt
RUN pip3.6 install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

RUN git clone https://github.com/parlaynu/inference-onnx.git && \
    mv inference-onnx/tools/inference . && \
    rm -rf inference-onnx && \
    rm -f inference/classify-onnx.py

COPY local/onnx2trt /workspace/onnx2trt
COPY local/inference /workspace/inference/

RUN sed -i 's/env python3/env python3.6/g' /workspace/inference/classify-trt.py
    
ENTRYPOINT ["/bin/sh", "-c", "exec \"$0\" \"$@\""]
CMD ["/bin/bash"]

