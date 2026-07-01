# Day 32 - Deploying File Browser with Docker Compose

## Overview

Today I deployed **File Browser** on my Ubuntu Desktop Docker host. File Browser provides a lightweight web interface for managing files and directories from any web browser, eliminating the need to SSH into the server for simple file management tasks.

This project expands my Docker management environment alongside Portainer and Nginx and prepares the Ubuntu Desktop to become a dedicated Docker management node within my homelab.

---

# Objectives

- Deploy File Browser using Docker Compose
- Expose the web interface on port **8081**
- Configure persistent storage
- Create an administrator account
- Integrate File Browser into my Docker projects directory
- Test web-based file management

---

# Environment

| Component | Value |
|-----------|-------|
| Host | Ubuntu Desktop 22.04 LTS |
| IP Address | 192.168.0.191 (Reserved DHCP) |
| Container | File Browser |
| Port | 8081 |
| Deployment | Docker Compose |

---

# Folder Structure

```text
/home/ravi/docker
├── filebrowser
│   └── docker-compose.yml
├── nginx
├── portainer
└── backups
```

---

# Docker Compose Configuration

```yaml
services:
  filebrowser:
    image: filebrowser/filebrowser:latest
    container_name: filebrowser

    ports:
      - "8081:80"

    volumes:
      - /home/ravi/docker:/srv
      - filebrowser_database:/database
      - filebrowser_config:/config

    restart: unless-stopped

volumes:
  filebrowser_database:
  filebrowser_config:
```

---

# Deployment

Created the project directory:

```bash
mkdir -p ~/docker/filebrowser
cd ~/docker/filebrowser
```

Created the compose file and deployed:

```bash
docker compose up -d
```

Verified the container:

```bash
docker ps
```

---

# Initial Login

Accessed:

```text
http://192.168.0.191:8081
```

Created the administrator account and logged into File Browser successfully.

---

# Issue Encountered

Initially File Browser displayed an empty directory because it was only mapped to its internal data folder.

Updated the volume mapping from:

```yaml
./data:/srv
```

to

```yaml
/home/ravi/docker:/srv
```

Restarted the container:

```bash
docker compose down
docker compose up -d
```

After restarting, File Browser displayed my Docker projects correctly.

---

# Verification

Successfully viewed the following Docker project folders through the web interface:

- filebrowser
- nginx
- portainer
- backups

Confirmed the following features were working:

- Folder browsing
- Directory navigation
- File management interface
- Persistent storage
- Docker volume mapping

---

# Skills Demonstrated

- Docker Compose
- Container deployment
- Docker volumes
- Bind mounts
- Linux file management
- Web-based administration
- Persistent container storage
- Docker troubleshooting

---

# Outcome

Successfully deployed File Browser as a web-based file management solution for my Ubuntu Docker host.

This provides a convenient way to manage Docker project files, edit configurations, upload files and organise future projects directly from a browser without requiring SSH for routine file operations.

The Ubuntu Desktop is now evolving into a dedicated Docker management node within my homelab alongside existing infrastructure hosted on Proxmox.

---

# Technologies Used

- Ubuntu Desktop 22.04 LTS
- Docker
- Docker Compose
- File Browser
- Linux
- VS Code
