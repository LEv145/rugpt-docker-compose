
import os
import sys

sys.path.append("/opt/ru-gpts/")
# Singleton moment
os.environ["USE_DEEPSPEED"] = "1"
os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = "5000"
from src.xl_wrapper import RuGPT3XL


def main():
    gpt = RuGPT3XL.from_pretrained(
        "sberbank-ai/rugpt3xl",
        weights_path="/mnt/store/models/rugpt3xl/mp_rank_00_model_states.pt",
        seq_len=512,
    )
    result = gpt.generate(
        "Кто был президентом США в 2020? ",
        max_length=50,
        no_repeat_ngram_size=3,
        repetition_penalty=2.0,
    )
    print(result)


if __name__ == "__main__":
    main()
