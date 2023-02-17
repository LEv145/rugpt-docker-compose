FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu20.04


RUN apt-get update
RUN apt install -y clang-9 llvm-9 llvm-9-dev llvm-9-tools
RUN apt install -y git python3 python3-pip python3-dev build-essential


WORKDIR /opt/
RUN git clone https://github.com/sberbank-ai/ru-gpts


RUN pip install -U pip

RUN pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 \
-f https://download.pytorch.org/whl/torch_stable.html
# Install Apex
WORKDIR /tmp/unique_for_apex
RUN git clone https://github.com/qywu/apex
WORKDIR /tmp/unique_for_apex/apex
RUN  pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" ./

RUN pip install "triton==1.0.0"
RUN DS_BUILD_CPU_ADAM=1 DS_BUILD_SPARSE_ATTN=1 pip install deepspeed==0.7.4
RUN pip install "transformers==4.24.0"
RUN pip install "timm==0.3.2"


WORKDIR /opt/ru-gpts
# Monkey patch
RUN cp src_utils/trainer_pt_utils.py /usr/local/lib/python3.8/dist-packages/transformers/trainer_pt_utils.py
RUN cp src_utils/_amp_state.py /usr/local/lib/python3.8/dist-packages/apex/amp/_amp_state.py
