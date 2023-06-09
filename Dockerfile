# Use a base image with Python pre-installed
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 2000

# Set the entrypoint command to run the Flask application
CMD python ./app.py