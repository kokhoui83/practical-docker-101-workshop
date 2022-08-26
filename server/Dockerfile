# base image
FROM python:3.10.6

# set work directory
WORKDIR /usr/src/app

# copy pipfile
COPY requirements.txt ./

# install project dependencies
RUN pip install -r requirements.txt

# copy src code
COPY . .

# run server
CMD ["python", "src/server.py"]