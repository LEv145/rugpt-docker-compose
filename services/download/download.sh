#!/usr/bin/env bash

cd /mnt/store/models

git lfs install
git clone https://huggingface.co/sberbank-ai/rugpt3large_based_on_gpt2
git clone https://huggingface.co/sberbank-ai/rugpt2large
git clone https://huggingface.co/sberbank-ai/rugpt3small_based_on_gpt2
git clone https://huggingface.co/sberbank-ai/rugpt3medium_based_on_gpt2
git clone https://huggingface.co/sberbank-ai/rugpt3xl
