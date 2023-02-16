FROM nvcr.io/nvidia/pytorch:22.02-py3


WORKDIR /opt/
RUN git clone https://github.com/sberbank-ai/ru-gpts rugpts


RUN pip install -U pip

# Install Apex
WORKDIR /tmp/unique_for_apex
RUN git clone https://github.com/NVIDIA/apex
WORKDIR /tmp/unique_for_apex/apex
RUN pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .

RUN pip install "nltk>=3.4"
RUN pip install "numpy>=1.15.4"
RUN pip install "pandas>=0.24.0"
RUN pip install "sentencepiece>=0.1.8"
RUN pip install "tensorflow>=1.12.0"
RUN pip install "boto3==1.11.11"
RUN pip install "regex==2020.1.8"
#"timm==0.3.2" \
RUN DS_BUILD_CPU_ADAM=1 DS_BUILD_SPARSE_ATTN=1 pip install deepspeed


WORKDIR /opt/rugpts
