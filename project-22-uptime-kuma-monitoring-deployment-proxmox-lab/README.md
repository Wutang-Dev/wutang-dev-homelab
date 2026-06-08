# Project 22 – Uptime Kuma Monitoring Deployment (Proxmox Lab)

## Overview

As part of my ongoing Proxmox and Linux learning journey, I deployed Uptime Kuma on an Ubuntu Server virtual machine running inside Proxmox.

The objective of this project was to create a central monitoring platform for my homelab infrastructure while gaining hands-on experience with:

- Ubuntu Server administration
- Docker and Docker Compose
- Containerized application deployment
- Tailscale remote access
- Infrastructure monitoring
- Service availability monitoring

## Environment

### Hypervisor

- Proxmox VE 9.2.3

### Virtual Machine

| Setting | Value |
|----------|---------|
| VM Name | Ubuntu Server |
| VM ID | 100 |
| vCPU | 2 Cores |
| RAM | 2 GB |
| Operating System | Ubuntu Server |
| QEMU Agent | Enabled |
| SSH | Enabled |

### Networking

- Connected to home LAN
- Managed through Tailscale
- Accessible remotely via Tailscale hostname

## Objectives

The goals of this project were:

1. Deploy a Linux server inside Proxmox.
2. Install Docker and Docker Compose.
3. Deploy Uptime Kuma using containers.
4. Configure remote access through Tailscale.
5. Monitor key homelab services.
6. Build a foundation for future monitoring projects.

## Docker Deployment

A Docker Compose deployment was used to simplify installation and management.

### Container Deployed

| Container | Purpose |
|------------|-----------|
| uptime-kuma | Infrastructure monitoring |

### Deployment Command

```bash
docker compose up -d
```

### Verification

Container status was verified using:

```bash
docker ps
```

## Tailscale Integration

Tailscale was installed on the Ubuntu Server VM to provide secure remote access.

### Features Implemented

- Tailscale node registration
- Remote access via Tailnet
- Tailscale SSH enabled
- Browser access to Uptime Kuma

Example URL:

```text
http://wutanglan-ubuntu-server.tail4de4cb.ts.net:3001
```

## Monitoring Configuration

The following devices and services were added to Uptime Kuma.

### Monitors

| Service | Monitor Type |
|-----------|---------------|
| Gateway Router | Ping |
| Proxmox Host | HTTP |
| Pi-hole | HTTP |
| Jellyfin | HTTP |
| Ubuntu Server | Ping |

### Results

All monitored devices successfully reported:

```text
Status: UP
Availability: 100%
```

## Homepage Dashboard Integration

Uptime Kuma was integrated into the Homepage dashboard for centralized management.

### Service Entry

```yaml
- Monitoring:
    - Uptime Kuma:
        href: http://wutanglan-ubuntu-server.tail4de4cb.ts.net:3001
        description: Infrastructure Monitoring Dashboard
        icon: uptime-kuma.png
```

This allows direct access to the monitoring platform from the homelab dashboard.

## Skills Practiced

### Linux

- SSH administration
- Service management
- Package updates
- File navigation

### Docker

- Container deployment
- Docker Compose
- Container management

### Networking

- ICMP monitoring
- Service monitoring
- Remote access

### Infrastructure

- Monitoring implementation
- Availability tracking
- Dashboard integration

## Challenges Encountered

### Learning Docker Compose

Understanding container deployment and management through Docker Compose was a new skill area.

### Monitoring Selection

Deciding which infrastructure components provided the most useful monitoring information required some experimentation.

### Homepage Integration

Homepage service configuration required editing YAML configuration files and restarting containers to apply changes.

## Outcome

The deployment was successful.

The Ubuntu Server VM now serves as a monitoring platform for the homelab and provides visibility into the availability of key infrastructure components including:

- Proxmox
- Pi-hole
- Jellyfin
- Gateway Router
- Ubuntu Server

This project also creates a foundation for future monitoring tools such as Grafana and Prometheus.

## Next Steps

Future planned projects include:

- Homepage Dashboard Enhancements
- Grafana Deployment
- Prometheus Deployment
- Additional Linux Services
- Containerized Applications
- Expanded Infrastructure Monitoring

## Key Takeaways

- Successfully deployed Uptime Kuma using Docker.
- Successfully managed a Linux VM inside Proxmox.
- Integrated Tailscale for secure remote access.
- Built a centralized monitoring dashboard.
- Continued developing Linux, Docker, and Proxmox administration skills.
- Created a reusable monitoring platform for future homelab projects.
