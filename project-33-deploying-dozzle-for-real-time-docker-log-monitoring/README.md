# Day 34 – Deploying Dozzle for Real-Time Docker Log Monitoring

## Project Overview

In this project I deployed **Dozzle**, a lightweight web-based Docker log viewer, on my **Ravi Ubuntu Desktop** (Toshiba laptop).

This machine serves as my **Docker and Linux test environment**, allowing me to learn new technologies before implementing them on my production servers, such as **Jellyfin-Server** and **wutanglan-ubuntu-server**.

Dozzle provides a central interface for viewing live Docker container logs without needing to SSH into the server and manually run Docker commands.

---

## Objective

- Deploy Dozzle using Docker Compose
- Connect Dozzle to the Docker socket
- View all running containers in one interface
- Monitor live container logs
- Integrate Dozzle into my Homepage dashboard

---

## Lab Environment

**Host**

- Ravi Ubuntu Desktop (Toshiba Laptop)

**Purpose**

- Docker learning environment
- Linux administration practice
- Test platform before deploying services into production

---

## Technologies Used

- Ubuntu Desktop 22.04
- Docker Engine
- Docker Compose
- Dozzle
- Homepage
- VS Code
- PowerShell SSH

---

## Folder Structure

```text
~/docker/
└── dozzle/
    └── docker-compose.yml
```

---

## Docker Compose Configuration

```yaml
services:
  dozzle:
    image: amir20/dozzle:latest
    container_name: dozzle
    restart: unless-stopped

    ports:
      - "8082:8080"

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

---

## Deployment

Started the container using Docker Compose.

```bash
docker compose up -d
```

Verified the deployment.

```bash
docker ps
```

---

## Verification

Accessed the Dozzle web interface.

```text
http://192.168.0.191:8082
```

Dozzle successfully detected all running Docker containers, including:

- Dozzle
- Portainer
- Nginx
- File Browser
- Watchtower

The dashboard also displayed:

- Host CPU usage
- Memory usage
- Running container count
- Individual container resource utilisation

---

## Homepage Integration

Added Dozzle to the **Monitoring** section of my Homepage dashboard alongside:

- Uptime Kuma
- Grafana

This provides quick access to live Docker logs from my homelab dashboard.

---

## Outcome

Successfully deployed Dozzle as a centralised Docker log monitoring solution.

My Ravi Ubuntu Desktop is now acting as a dedicated Docker management environment where I can safely learn, test and validate new services before introducing them into my production homelab infrastructure.

Current Docker management stack:

- Portainer
- Nginx
- File Browser
- Watchtower
- Dozzle

---

## Skills Demonstrated

- Docker
- Docker Compose
- Linux administration
- Container monitoring
- Docker log analysis
- Self-hosting
- Homepage integration
- Infrastructure management

---

## Lessons Learned

- Dozzle provides an excellent real-time alternative to repeatedly using `docker logs`.
- Mounting the Docker socket in read-only mode allows Dozzle to access container logs securely.
- A dedicated Docker test environment makes it easier to experiment with new services before deploying them into production.
- Integrating services into Homepage creates a single dashboard for managing the homelab.

---

## Next Steps

- Deploy additional Docker management tools.
- Continue expanding the Docker learning environment.
- Test new services on Ravi Ubuntu Desktop before migrating them to Jellyfin-Server or wutanglan-ubuntu-server.
- Continue building a production-ready self-hosted Docker platform.
