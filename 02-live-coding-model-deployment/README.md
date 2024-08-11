# 02. Live Coding Sessions 🎥

## Exercises - Model Deployment with Flask/Docker

### 1. Build a Simple API with Flask

We will work through the following exercises to build and deploy a simple API using Flask and Docker.

#### 1.1 Read a JSON File and Return an Object by Name or ID

- **Task:** Write a Python function that reads a `channels.json` file with the following structure:

    ```json
    {
        "id": "channel id",
        "name": "channel name",
        "tags": ["list of tags", "tag 2", ...],
        "description": "channel description ..."
    }
    ```

- **Functionality:** The function should return the channel object given either the channel name or the channel ID.

#### 1.2 Build a `GET` Endpoint to Retrieve All Channels

- **Task:** Build a `GET` endpoint that returns the entire list of channels.

#### 1.3 Build a `GET` Endpoint to Retrieve a Specific Channel

- **Task:** Build a `GET` endpoint that accepts a channel ID or channel name as a parameter and returns the corresponding channel's JSON object.

#### 1.4 Write a `POST` Method to Add a New Channel

- **Task:** Write a `POST` method to add a new channel to the `channels.json` file.


### 2. Dockerize the Flask API

In this exercise, we will containerize the Flask API you built in the previous exercise using Docker.

#### 2.1 Create a `Dockerfile`

- **Task:** Create a `Dockerfile` in the root directory of your project. This file will define the environment in which your Flask app will run.

- **Contents of the `Dockerfile`:**

    ```dockerfile
    # Use an official Python runtime as a parent image
    FROM python:3.9-slim

    # Set the working directory in the container
    WORKDIR /app

    # Copy the current directory contents into the container at /app
    COPY . /app

    # Install any necessary dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Make port 5000 available to the world outside this container
    EXPOSE 5000

    # Define environment variable
    ENV FLASK_ENV=production

    # Run app.py when the container launches
    CMD ["python", "app.py"]
    ```

#### 2.2 Create a `docker-compose.yml` (Optional)

- **Task:** If you have additional services (like a database), you can use `docker-compose` to manage them.

- **Contents of the `docker-compose.yml`:**

    ```yaml
    version: '3'
    services:
      web:
        build: .
        ports:
          - "5000:5000"
        volumes:
          - .:/app
        environment:
          - FLASK_ENV=development
    ```

#### 2.3 Build the Docker Image

- **Task:** Build the Docker image from the `Dockerfile`.

- **Command:**

    ```bash
    docker build -t flask-api-app .
    ```

#### 2.4 Run the Docker Container

- **Task:** Run the Flask API inside a Docker container.

- **Command:**

    ```bash
    docker run -d -p 5000:5000 flask-api-app
    ```

  This command will start your Flask API in a detached mode and map port 5000 of the container to port 5000 of your local machine.


#### 2.6 Push the Image to Docker Hub (Optional)

- **Task:** Optionally, you can push your Docker image to Docker Hub.

- **Command:**

    ```bash
    docker tag flask-api-app your-dockerhub-username/flask-api-app
    docker push your-dockerhub-username/flask-api-app
    ```
