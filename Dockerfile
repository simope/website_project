# Use an official Python runtime as a parent image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Add bash application to run the script
RUN apk update && apk add bash

# Command to run on container start
CMD ["/app/entrypoint.sh"]