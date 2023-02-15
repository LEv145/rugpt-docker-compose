import os
import sys


os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = "5000"
os.environ["USE_DEEPSPEED"] = "1"


from src.xl_wrapper import RuGPT3XL  # Singleton moment



gpt = RuGPT3XL.from_pretrained("/mnt/store/models/rugpt3xl", seq_len=512)
gpt.generate(
    "Кто был президентом США в 2020?",
    max_length=50,
    no_repeat_ngram_size=3,
    repetition_penalty=2.,
)
