# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install flask pymongo

# Expose the port the app runs on
EXPOSE 3000

# Run main.py when the container launches
CMD ["python", "/app/main.py"]
