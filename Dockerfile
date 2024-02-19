# Use the official Python 3.10.11 image from Docker Hub
FROM python:3.10.11-alpine

# Set a working directory inside the container
WORKDIR /app

# Copy all files from the current directory into the container at /app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apk add --no-cache bash

# Command to run your Python script
# CMD ["python", "main.py"]
