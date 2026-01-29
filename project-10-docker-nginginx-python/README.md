# 2026-01-29 – Project 10 – Dockerised Python Application

---

## Overview

In this project, I containerised a simple Python web application using Docker.

The objective was to understand the core Docker workflow end-to-end: building an image, running a container, exposing application ports, and validating service availability from the host system.

This project serves as a foundational step before introducing more complex containerised services such as Nginx and Pi-hole.

This project builds directly on:

Project 09 – Nginx HTTPS redirect and hardening  
Earlier Python HTTP application testing  

---

## Environment

Host: MacBook  
OS: Ubuntu  
Container Runtime: Docker  
Language: Python  

---

## What I Implemented

- Installed and validated Docker on the host system  
- Created a simple Python HTTP application (`app.py`)  
- Created a Dockerfile to containerise the Python application  
- Built a Docker image locally  
- Ran the container in detached mode  
- Exposed the application using Docker port mapping  
- Validated application access via browser and curl  

---

## Application Overview

The Python application is a minimal HTTP service that returns a static response confirming it is running inside a Docker container.

The application listens on port 5000 inside the container.

---

## Docker Configuration

The Dockerfile performs the following actions:

- Uses an official Python base image  
- Sets a working directory inside the container  
- Copies the application source code into the image  
- Executes the application using `python app.py`  

---

## Image Build

The Docker image was built locally using:

**`docker build -t project-10-docker-nginx-python .`**

The image was confirmed using:

**`docker images`**

---

## Running the Container

The container was started in detached mode with port mapping:

**`docker run -d -p 8080:5000 --name project10-app project-10-docker-nginx-python`**

Port mapping details:

- Host port: 8080  
- Container port: 5000  

---

## Validation Steps

Confirm running containers:

**`docker ps`**

Test application via browser:

**`http://localhost:8080`**

Test application via curl:

**`curl http://localhost:8080`**

Expected response:

Project 10 -**` Python app running inside Docker`**


---

## Result

The Python application is running successfully inside a Docker container.

The application is accessible from the host system through port mapping and responds correctly via both browser and command-line testing.

---

## Troubleshooting & Lessons Learned

Initially, container execution failed due to incorrect image naming.

By listing local images and matching the exact image tag, the container was able to start successfully.

This reinforced the importance of verifying image names and understanding Docker’s local vs remote image behaviour.

---

## Key Takeaways

- Docker images must be referenced using their exact tag names  
- Containers isolate application runtime from the host system  
- Port mapping is required to expose container services  
- Validation should always be performed via both browser and CLI  
