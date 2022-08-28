# base image
FROM node:18.7.0

# set work directory
WORKDIR /usr/src/app

# copy package file
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files
COPY . .

# start
CMD ["npm", "start"]