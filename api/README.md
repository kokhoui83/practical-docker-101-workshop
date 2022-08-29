# Sample Api Service
- Provide API for random qoutes

## Requirements
- node 18.7.x

## Project Setup

```sh
npm install
```

## Build docker container
- `## TODO Create dockerfile` <-- do this before the next step
- build server app
```
# command
docker build -t <name>:<version> <path>

# example
docker build -t sample-api-service:0.0.1 .
```

## Run docker container
- using `docker run` command
```
# command
docker run -d --rm --name <container-name> <image-name>

# example
docker run -d --rm --name api-service api-service:0.0.1
```

- `## TODO: Create docker-compose file` <-- do this before running the compose command
- using `docker compose` command
```
# command
docker compose up -d
```

## Stop docker container
- if started with `docker run`
```
# commmand
docker stop <container-name>

# example
docker stop api-service
```

- if started with `docker compose`
```
# command
docker compose down
```