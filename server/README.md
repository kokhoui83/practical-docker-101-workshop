# Sample Server Application

## Requirements
- python 3.10.x
- virtualenv or pipenv

## Setup
- setup virtual environment
```
# virtualenv
virtualenv .venv

# pipenv
mkdir .venv
pipenv --python 3.10
```
- activate virtual environment
```
# activate via virtualenv
source .venv/bin/activate

# activeate via pipenv
pipenv shell
```
- install dependencies
```
# install dependencies via pip
pip install -r requirements.txt

# install dependencies via pipenv
pipenv install
```

## Run
- start server
```
python src/server.py
```

## API
- documentations http://localhost:8001/docs

## Build docker container
- `## TODO Create dockerfile` <-- do this before the next step
- build server app
```
# command
docker build -t <name>:<version> <path>

# example
docker build -t sample-server-app:0.0.1 .
```

## Run docker container
- using `docker run` command
```
# command
docker run -d --rm -p <host-port>:<container-port> --name <container-name> <image-name>

# example
docker run -d --rm -p 8001:8001 --name server-app sample-server-app:0.0.1
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
docker stop server-app
```

- if started with `docker compose`
```
# command
docker compose down
```