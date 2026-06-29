# Project 31 - Deploying Nginx with Docker

## Project Overview

The objective of this project was to deploy an Nginx web server using Docker Compose on my Ubuntu Desktop Docker host. This project introduced the core Docker concepts of images, containers, port mapping, bind mounts and Docker Compose while continuing to build my dedicated Linux learning environment.

---

## Objectives

* Deploy an Nginx container using Docker Compose.
* Learn Docker image deployment.
* Understand container port mapping.
* Create and use bind mounts.
* Serve a custom HTML page from the host.
* Troubleshoot Docker Compose configuration errors.

---

## Environment

| Component        | Details                  |
| ---------------- | ------------------------ |
| Host             | Toshiba Laptop           |
| Operating System | Ubuntu Desktop 22.04 LTS |
| Docker           | Installed                |
| Docker Compose   | Installed                |
| Container        | Nginx                    |
| Hostname         | ravi-ubuntu-desktop      |
| IP Address       | 192.168.0.191            |

---

## Project Folder

```bash
mkdir -p ~/docker/nginx
cd ~/docker/nginx
```

---

## Docker Compose Configuration

```yaml
services:
  nginx:
    image: nginx:latest
    container_name: nginx
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html:ro
    restart: unless-stopped
```

---

## Deploying the Container

```bash
docker compose up -d
```

---

## Verifying the Deployment

Verified the container was running.

```bash
docker ps
```

Confirmed the container was exposing:

```
0.0.0.0:8080 -> 80/tcp
```

---

## Creating a Custom Web Page

Created a directory to store website files.

```bash
mkdir html
```

Created the default page.

```bash
nano html/index.html
```

Example content:

```html
<h1>Project 31 - Nginx Docker Deployment</h1>
<p>This page is served from a Docker bind mount.</p>
<p>Host: ravi-ubuntu-desktop</p>
<p>IP Address: 192.168.0.191</p>
```

---

## Redeploying the Container

```bash
docker compose down
docker compose up -d
```

After refreshing the browser, Nginx successfully served the custom HTML page from the bind mount.

---

## Troubleshooting

### YAML Validation Error

During deployment Docker Compose returned the following error:

```
services.nginx.volumes must be an array
```

Cause:

The `volumes` section in the Docker Compose file had incorrect YAML formatting.

Resolution:

Corrected the indentation and formatted the bind mount as an array.

```yaml
volumes:
  - ./html:/usr/share/nginx/html:ro
```

After correcting the YAML syntax the container deployed successfully.

---

## Skills Practiced

* Docker
* Docker Compose
* Nginx
* Docker Images
* Docker Containers
* Docker Port Mapping
* Docker Bind Mounts
* YAML
* Linux CLI
* Container Troubleshooting

---

## Outcome

Successfully deployed an Nginx web server using Docker Compose and served a custom web page from a bind-mounted directory on the Ubuntu host.

This project introduced the fundamental concepts of containerised web applications and demonstrated how Docker can separate application code from the host operating system while still allowing persistent content through bind mounts.

---

## Lessons Learned

* Docker Compose makes application deployment simple and repeatable.
* Bind mounts allow host files to be served directly by containers.
* Correct YAML indentation is essential.
* Docker validation errors often point directly to configuration issues.
* Troubleshooting configuration errors is an important part of learning Docker.

---

## Next Steps

* Deploy File Browser.
* Learn Docker volumes in greater depth.
* Deploy AdGuard Home.
* Deploy Dozzle.
* Deploy Watchtower.
* Learn Docker networking.
* Deploy additional self-hosted services using Docker Compose.
