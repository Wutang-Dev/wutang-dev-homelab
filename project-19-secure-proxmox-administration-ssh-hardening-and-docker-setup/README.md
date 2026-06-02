# Project 19 – Secure Proxmox Administration, SSH Hardening & Docker Setup

## Overview

Continued developing my Proxmox homelab environment by improving security, remote administration, and container capabilities.

The focus of this project was:

- Secure remote access
- SSH authentication improvements
- TLS certificate implementation
- Proxmox update management
- Docker deployment preparation for future self-hosted services

---

## Objectives

- Practice SSH administration workflows
- Learn secure authentication concepts
- Remove browser certificate warnings
- Implement secure remote management
- Prepare Proxmox for self-hosting workloads

---

## SSH Administration & Authentication

Practiced remote administration by connecting to infrastructure services using:

- Windows Terminal
- SSH
- Tailscale MagicDNS hostname resolution

Validated successful remote connections to:

- Proxmox node
- Pi-hole server

Examples used:

```bash
ssh root@proxmox
ssh pi@pihole
```

---

## SSH Keys & Passwordless Authentication

Learned about SSH key authentication and why it is commonly used in infrastructure environments.

Implemented passwordless SSH access through Tailscale SSH.

Configured:

```bash
tailscale up --ssh
```

This allowed authentication to be handled through Tailscale identity controls rather than traditional password login.

### Results

✅ Passwordless SSH access  
✅ Centralized authentication via Tailscale  
✅ Improved remote administration workflow

Applied this approach to both:

- Proxmox
- Pi-hole

---

## Proxmox Update Management

Learned about the recommended Proxmox node update workflow.

Rather than using standard package management commands alone, used:

```bash
pveupgrade
```

to update the Proxmox node following platform-recommended practices.

### Key Learning

- Proxmox-specific update tooling
- Node maintenance workflows
- Package management differences in appliance-style systems

---

## TLS Certificate Implementation

Implemented HTTPS certificate handling for Proxmox administration using Tailscale Serve.

### Goal

Remove browser certificate warnings during remote access.

Configured:

```bash
tailscale serve --bg https+insecure://localhost:8006
```

This created a secure HTTPS endpoint for accessing the Proxmox web interface through Tailscale networking.

### Results

✅ TLS certificate generated  
✅ Secure browser access  
✅ Cleaner administration experience

---

## Docker Installation

Installed Docker on the Proxmox environment to prepare for future self-hosting experimentation.

Installed using:

```bash
curl -fsSL https://get.docker.com | sh
```

Validated deployment with:

```bash
docker run --rm -it hello-world
```

Successful validation confirmed:

✅ Docker installation  
✅ Container runtime functionality  
✅ Environment ready for future services

---

## Key Learning

This project reinforced:

- SSH administration
- SSH key concepts
- Passwordless authentication
- Secure remote access
- TLS certificates
- Proxmox node maintenance
- Docker deployment
- Self-hosting fundamentals

---

## Next Steps

Planned future projects:

- Immich deployment
- Audiobookshelf deployment
- Home Assistant deployment
- Container management workflows
- Service persistence & backups
- Reverse proxy experimentation
