# Build the base images
FROM ubuntu:latest

# Install or add the necessary modules and packages
RUN apt-get upgrade && apt-get update && apt-get install -y python3 && apt-get install -y python3-pip && pip3 install flask

# Define the working directory
WORKDIR /Flask_apps/

# Copy the directory from the local machine to the docker image
COPY ./Flask_apps/1-Webapp/ ./

# Instead, we can also copy files by providing the respective paths
# COPY ./Flask_apps/1-Webapp/init.py ./init.py

# Make the port 5000 available to the outer web at which the Flask app runs
EXPOSE 5000

# Write the set of commands which the docker image must run during the runtime or
# Following are the commands which the docker runs first when it starts.
CMD python3 /Flask_apps/init.py
