# Project 30 - Deploying Portainer on Ubuntu Desktop

## Project Overview

The objective of this project was to deploy Portainer on my dedicated Ubuntu Desktop Docker host to provide a graphical interface for managing Docker containers. This machine will serve as my Linux and Docker learning environment while my existing Ubuntu Server continues hosting production services.

---

## Objectives

- Deploy Portainer using Docker Compose.
- Manage Docker containers through a web interface.
- Continue learning Docker best practices.
- Create a dedicated Docker sandbox separate from my production environment.

---

## Environment

| Component | Details |
|----------|---------|
| Host | Toshiba Laptop |
| Operating System | Ubuntu Desktop 22.04 LTS |
| Docker | Installed |
| Docker Compose | Installed |
| Management Tool | Portainer CE |
| Hostname | ravi-ubuntu-desktop |
| IP Address | 192.168.0.191 |

---

## Prerequisites

- Ubuntu Desktop installed.
- Docker installed and verified.
- Docker Compose installed.
- Static DHCP reservation configured on the TP-Link AX3000 router.
- SSH configured.
- VS Code Remote SSH configured.
- Tailscale installed.

---

## Project Folder

```bash
mkdir -p ~/docker/portainer
cd ~/docker/portainer
```

---

## Docker Compose File

```yaml
services:
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer
    command: --no-setup-token
    ports:
      - "9000:9000"
      - "9443:9443"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data
    restart: unless-stopped

volumes:
  portainer_data:
```

---

## Deploying the Stack

```bash
docker compose up -d
```

---

## Verification

Verified the container was running.

```bash
docker ps
```

---

## Viewing Logs

```bash
docker logs portainer
```

The logs confirmed:

- HTTPS server started
- HTTP server started
- Portainer running successfully

---

## Initial Issues

### Setup Token

The latest Portainer release required a setup token before creating the administrator account.

Initially I attempted to retrieve the token from the logs, however the process repeatedly failed with an "Invalid or Missing Setup Token" error.

To simplify the deployment for a standalone lab environment I configured Portainer to disable the setup token requirement by adding:

```yaml
command: --no-setup-token
```

---

### Browser Issue

Another issue occurred where Portainer timed out during the initial setup.

After troubleshooting I discovered that uBlock Origin was interfering with the setup page.

Disabling uBlock for the local Portainer page resolved the problem.

---

## Successful Deployment

Successfully created the administrator account.

Portainer is now available at:

```
https://192.168.0.191:9443
```

---

## Skills Practiced

- Docker
- Docker Compose
- Portainer
- Docker Volumes
- Container Management
- Docker Logs
- YAML Configuration
- Linux Administration
- SSH
- Network Troubleshooting

---

## Outcome

Successfully deployed a dedicated Portainer instance on my Ubuntu Desktop Docker host.

This machine will now be used as my Docker learning platform while keeping my existing Ubuntu Server dedicated to production services including Homepage, ROMM and future self-hosted applications.

Separating production and learning environments allows me to safely experiment with new containers and Docker concepts without impacting existing services.

---

## Lessons Learned

- Portainer can be deployed quickly using Docker Compose.
- Reading Docker logs is essential when troubleshooting deployments.
- Browser extensions can interfere with local web applications.
- Docker Compose provides a simple and repeatable deployment method.
- Maintaining separate production and lab environments is a best practice for learning and testing.

---

## Next Steps

- Deploy Nginx.
- Learn Docker networking.
- Learn bind mounts and Docker volumes.
- Deploy File Browser.
- Deploy Dozzle.
- Deploy AdGuard Home.
- Deploy Watchtower.
- Deploy Homepage on a non-conflicting port for additional Docker practice.
