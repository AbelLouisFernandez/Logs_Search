# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y python3-opencv \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install -U --no-cache-dir -r requirements.txt

# Copy the rest of the app's code
COPY . .
