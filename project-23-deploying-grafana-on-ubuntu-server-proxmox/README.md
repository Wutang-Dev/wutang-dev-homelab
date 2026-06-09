# Project 23 - Deploying Grafana on Ubuntu Server (Proxmox)

## Project Overview

The objective of this project was to deploy Grafana within my Proxmox homelab environment to begin building a monitoring and observability stack. Grafana provides a central dashboard platform that can later be integrated with Prometheus and Node Exporter to visualise system performance metrics across my infrastructure.

## Environment

* Hypervisor: Proxmox VE 9.2.3
* Virtual Machine: Ubuntu Server 24.04 LTS
* VM ID: 100
* Hostname: wutanglan-ubuntu-server
* Remote Access: Tailscale SSH
* Management Tool: VS Code Remote SSH
* Container Platform: Docker & Docker Compose

## Tasks Completed

### 1. Created Grafana Project Directory

Created a dedicated project directory for Grafana:

```bash
mkdir ~/grafana
cd ~/grafana
```

### 2. Created Docker Compose Configuration

Created a compose.yaml file containing the Grafana container configuration.

Key configuration included:

* Latest Grafana image
* Persistent Docker volume for dashboard and configuration storage
* Automatic restart policy
* Port mapping for web access

### 3. Initial Troubleshooting

During deployment the Grafana web interface was inaccessible.

Investigation identified an incorrect port mapping within the Docker Compose configuration.

Incorrect configuration:

```yaml
ports:
  - "3002:3002"
```

Correct configuration:

```yaml
ports:
  - "3002:3000"
```

This issue occurred because Grafana listens on port 3000 inside the container.

After correcting the port mapping, the container was redeployed successfully.

### 4. Redeployed Grafana

Stopped and recreated the container using:

```bash
docker compose down
docker compose up -d
```

Verified successful deployment using:

```bash
docker ps
```

### 5. Accessed Grafana Dashboard

Successfully connected to Grafana using:

```text
http://192.168.0.188:3002
```

and

```text
http://wutanglan-ubuntu-server.tail4de4cb.ts.net:3002
```

Logged in using the default administrator account and changed the password during first login.

### 6. Verified Dashboard Functionality

Confirmed successful deployment by accessing:

* Grafana Home Dashboard
* Dashboard Management
* Data Source Configuration Area
* Administration Section

## Skills Practiced

* Linux administration
* Docker container deployment
* Docker Compose configuration
* Troubleshooting container networking issues
* Port mapping concepts
* Tailscale remote access
* Proxmox virtual machine management
* Monitoring platform deployment

## Outcome

Grafana was successfully deployed and is now operational within the Ubuntu Server virtual machine hosted on Proxmox.

Current monitoring stack:

* Homepage
* Uptime Kuma
* Grafana

Future phases will include:

* Prometheus deployment
* Node Exporter deployment
* System metric collection
* Grafana dashboard visualisation
* Infrastructure performance monitoring

## Key Learning

A significant learning point from this project was understanding Docker port mapping and how container ports differ from host ports. Troubleshooting the incorrect port configuration reinforced the importance of verifying service listening ports when deploying containerised applications.

## Project Status

✅ Grafana Installed

✅ Container Running

✅ Persistent Storage Configured

✅ Tailscale Accessible

✅ Web Interface Accessible

🔜 Prometheus Integration

🔜 Node Exporter Integration

🔜 Infrastructure Monitoring Dashboards
