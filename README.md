# RuGPT Docker compose

## Setup

```sh
# Download models to store
docker compose --profile download up --build
# Run RuGPT
docker compose --profile [model] run --build
# Where [model] is one of: rugpt3 | rugpt3-xl (experemental)
```
`./store` is mounted to `/mnt/store` in container
