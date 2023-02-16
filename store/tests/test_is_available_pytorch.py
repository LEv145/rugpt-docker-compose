import torch


def main():
    is_available = torch.cuda.is_available()
    print(is_available)


if __name__ == "__main__":
    main()
