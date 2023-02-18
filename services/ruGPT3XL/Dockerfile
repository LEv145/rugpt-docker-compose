FROM nvcr.io/nvidia/pytorch:22.02-py3


ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1


WORKDIR /opt/
RUN git clone https://github.com/sberbank-ai/ru-gpts


RUN pip install -U pip

# Install Apex
WORKDIR /tmp/unique_for_apex
RUN git clone https://github.com/NVIDIA/apex
WORKDIR /tmp/unique_for_apex/apex
RUN git reset --hard 0c8400aa04f4279b1384ae0633e73d6daf9fead7
RUN pip install -v --global-option="--cpp_ext" --global-option="--cuda_ext" .
RUN rm -Rf /tmp/unique_for_apex/apex

RUN pip install "nltk>=3.4"
RUN pip install "numpy>=1.15.4"
RUN pip install "pandas>=0.24.0"
RUN pip install "sentencepiece>=0.1.8"
RUN pip install "tensorflow>=1.12.0"
RUN pip install boto3==1.11.11
RUN pip install regex==2020.1.8
RUN pip install triton==1.0.0
RUN DS_BUILD_CPU_ADAM=1 DS_BUILD_SPARSE_ATTN=1 pip install deepspeed==0.8.0
RUN pip install transformers==4.26.1
RUN pip install timm==0.3.2


WORKDIR /opt/ru-gpts
