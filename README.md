# RuGPT Docker compose

## Setup

```sh
# Download models to store
docker compose up --build download
# Run RuGPT
docker compose run [model]
# Where [model] is one of: rugpt3 | rugpt3-xl (experemental)
```
`./store` is mounted to `/mnt/store` in container
