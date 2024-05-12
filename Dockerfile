# Use the official Python image as the base
FROM python:3.7

# Set the working directory in the container
WORKDIR /app

# Copy the Dockerfile from the current directory into the container at /app/
COPY Dockerfile /app/