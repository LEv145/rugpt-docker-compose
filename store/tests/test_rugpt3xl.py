import os
import sys


os.environ["MASTER_ADDR"] = "127.0.0.1"
os.environ["MASTER_PORT"] = "5000"
os.environ["USE_DEEPSPEED"] = "1"


from src.xl_wrapper import RuGPT3XL  # Singleton moment



gpt = RuGPT3XL.from_pretrained(
    "sberbank-ai/rugpt3xl",
    weights_path="/mnt/store/models/rugpt3xl/mp_rank_00_model_states.pt",
    seq_len=512,
)
gpt.generate(
    (
        "\u041a\u0442\u043e \u0431\u044b\u043b \u043f\u0440\u0435\u0437\u0438"
        "\u0434\u0435\u043d\u0442\u043e\u043c \u0421\u0428\u0410 \u0432 2020?"
    ),
    max_length=50,
    no_repeat_ngram_size=3,
    repetition_penalty=2.0,
    num_beams=5,
)
