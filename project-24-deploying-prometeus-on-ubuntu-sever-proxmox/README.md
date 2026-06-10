# Project 24 - Deploying Prometheus on Ubuntu Server (Proxmox)

## Project Overview

In this project I deployed Prometheus on my Ubuntu Server virtual machine running within Proxmox.

The objective was to begin building a monitoring stack for my homelab environment. Prometheus is an open-source monitoring and alerting platform that collects and stores time-series metrics from systems and applications.

This deployment forms the foundation for future monitoring projects, including Node Exporter and Grafana dashboard integration.

---

## Technologies Used

- Proxmox VE
- Ubuntu Server
- Docker
- Docker Compose
- Prometheus
- Tailscale
- VS Code Remote SSH

---

## Environment

### Host

- HP ProDesk Mini
- Proxmox VE

### Virtual Machine

- Ubuntu Server
- 2 vCPU
- 2 GB RAM

### Remote Access

- Tailscale
- SSH
- VS Code Remote SSH Extension

---

## Objectives

- Deploy Prometheus using Docker Compose
- Configure persistent storage
- Verify Prometheus metrics collection
- Enable LAN access
- Enable Tailscale remote access
- Prepare for Grafana integration

---

## Creating the Project Directory

Created a dedicated project directory:

```bash
mkdir ~/prometheus
cd ~/prometheus
```

---

## Creating the Docker Compose Configuration

Created a compose.yaml file:

```yaml
services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus

    ports:
      - "9090:9090"

    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml

    restart: unless-stopped
```

Configuration highlights:

- Latest Prometheus image
- Port mapping for web access
- Mounted configuration file
- Automatic restart policy

---

## Creating the Prometheus Configuration File

Created a prometheus.yml file:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"

    static_configs:
      - targets: ["localhost:9090"]
```

This configuration instructs Prometheus to:

- Scrape metrics every 15 seconds
- Monitor itself as the first target
- Store collected metrics in the internal database

---

## Deploying the Container

Started the container:

```bash
docker compose up -d
```

Verified deployment:

```bash
docker ps
```

Prometheus container was shown as running successfully.

---

## Access Verification

### LAN Access

Verified access using:

```text
http://wutanglan-ubuntu-server:9090
```

and

```text
http://192.168.x.x:9090
```

---

### Tailscale Access

Verified remote access using:

```text
http://wutanglan-ubuntu-server.tail4de4cb.ts.net:9090
```

Prometheus was accessible successfully over the Tailscale network.

---

## Testing Metrics Collection

To confirm Prometheus was collecting metrics, I executed the following query:

```text
up
```

Result:

```text
up{instance="localhost:9090",job="prometheus"} 1
```

A value of:

```text
1
```

indicates the target is healthy and reachable.

---

## Additional Verification

Executed:

```text
prometheus_build_info
```

Prometheus returned build information including:

- Version
- Operating System
- Architecture
- Go Runtime Version

This confirmed that metrics were being collected and exposed correctly.

---

## Skills Practiced

- Linux administration
- Docker deployment
- Docker Compose configuration
- Monitoring fundamentals
- Infrastructure monitoring
- Tailscale remote access
- Troubleshooting container deployments
- Prometheus query testing

---

## Outcome

Successfully deployed Prometheus on Ubuntu Server running within Proxmox.

Verified:

- Docker deployment
- Prometheus configuration
- Metrics collection
- LAN access
- Tailscale access
- Internal metric queries

This project establishes the monitoring foundation for future integrations with Node Exporter and Grafana dashboards.

---

## Next Steps

Planned follow-up projects:

- Project 25 - Deploying Node Exporter
- Project 26 - Integrating Prometheus with Grafana
- Project 27 - Building Infrastructure Monitoring Dashboards

---

## Key Takeaways

- Prometheus can be deployed quickly using Docker Compose.
- Metrics are collected through configurable scrape targets.
- Prometheus can monitor both local and remote systems.
- Tailscale provides secure remote access without port forwarding.
- Prometheus forms the core data source for Grafana dashboards.
