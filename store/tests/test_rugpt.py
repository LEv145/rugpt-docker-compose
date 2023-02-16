from sys import argv

from transformers import GPT2LMHeadModel, GPT2Tokenizer


def main(argv):
    model_name_or_path = argv[1]
    text = "Александр Сергеевич Пушкин родился в "

    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
    model = GPT2LMHeadModel.from_pretrained(model_name_or_path).cuda()
    input_ids = tokenizer.encode(text, return_tensors="pt").cuda()
    out = model.generate(input_ids.cuda())
    generated_text = list(map(tokenizer.decode, out))[0]

    print(generated_text)


if __name__ == "__main__":
    main(*argv)
