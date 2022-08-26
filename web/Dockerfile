# base image
FROM node:18.7.0

# install simple http server
RUN npm install -g http-server

# set work directory
WORKDIR /usr/src/app

# copy package file
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files
COPY . .

# build app for production
RUN npm run build

# serve file via http-server
CMD ["http-server", "dist"]