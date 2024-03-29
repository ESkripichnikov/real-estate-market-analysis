# set base image (host OS)
FROM python:3.9

# set the working directory in the container
WORKDIR /code

# copy the content of the local src directory to the working directory
COPY . /code

# install dependencies
RUN pip install -r requirements.txt


# command to run on container start
CMD [ "bash" ]
