# Sample Web Application

## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Requirements
- node 18.7.x

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

## Build docker container
- `## TODO Create dockerfile` <-- do this before the next step
- build server app
```
# command
docker build -t <name>:<version> <path>

# example
docker build -t sample-web-app:0.0.1 .
```

## Run docker container
- using `docker run` command
```
# command
docker run -d --rm -p <host-port>:<container-port> --name <container-name> <image-name>

# example
docker run -d --rm -p 8001:8001 --name web-app sample-web-app:0.0.1
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
docker stop web-app
```

- if started with `docker compose`
```
# command
docker compose down
```