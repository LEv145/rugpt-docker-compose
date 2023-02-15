FROM huggingface/transformers-pytorch-gpu:3.5.0


RUN pip install -U pip

# Install Apex
WORKDIR /tmp/unique_for_apex
RUN git clone https://github.com/NVIDIA/apex
WORKDIR /tmp/unique_for_apex/apex
RUN pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .

RUN pip install \
"nltk>=3.4" \
"numpy>=1.15.4" \
"pandas>=0.24.0" \
"sentencepiece>=0.1.8" \
"tensorflow>=1.12.0" \
"boto3==1.11.11" \
"regex==2020.1.8" \
"huggingface_hub" \
"timm==0.3.2" \
"triton==0.4.2"
RUN pip install transformers
#RUN DS_BUILD_CPU_ADAM=1 DS_BUILD_SPARSE_ATTN=1 pip install "deepspeed==0.5.10"


WORKDIR /opt/
RUN git clone https://github.com/sberbank-ai/ru-gpts rugpts
WORKDIR /opt/rugpts
