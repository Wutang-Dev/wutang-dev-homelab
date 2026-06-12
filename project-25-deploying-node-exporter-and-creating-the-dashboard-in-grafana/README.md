# Project 23–25: Deploying Grafana, Prometheus and Node Exporter on Ubuntu Server

## Project Objective

The objective of this project was to build a centralized monitoring platform for my homelab infrastructure using Grafana, Prometheus and Node Exporter. The monitoring stack was deployed on an Ubuntu Server virtual machine running on my Proxmox environment and provides real-time visibility into system performance, resource utilization and infrastructure health.

This project introduced industry-standard observability tools commonly used by system administrators, cloud engineers, DevOps engineers and managed service providers.

---

## Technologies Used

* Ubuntu Server
* Docker
* Docker Compose
* Grafana
* Prometheus
* Node Exporter
* Tailscale
* Homepage Dashboard
* Linux CLI

---

## Infrastructure Overview

Monitoring Stack Host:

* Ubuntu Monitoring Server
* IP Address: 192.168.0.188

Services Deployed:

* Homepage Dashboard (Port 3000)
* Uptime Kuma (Port 3001)
* Grafana (Port 3002)
* Prometheus (Port 9090)
* Node Exporter (Port 9100)

---

## Project 23 – Deploying Grafana

### Deployment

Created a dedicated Grafana project directory and Docker Compose configuration.

Example configuration:

```yaml
services:
  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3002:3000"
    volumes:
      - grafana-storage:/var/lib/grafana
    restart: unless-stopped

volumes:
  grafana-storage:
```

Deployed Grafana using Docker Compose.

```bash
docker compose up -d
```

---

### Troubleshooting

Initial deployment failed due to incorrect port mapping.

Incorrect configuration:

```yaml
ports:
  - "3002:3002"
```

Grafana listens on port 3000 internally, therefore the container was inaccessible.

Corrected configuration:

```yaml
ports:
  - "3002:3000"
```

The container was redeployed and validated successfully.

---

### Validation

Verified successful access using:

```text
http://192.168.0.188:3002
```

and

```text
http://wutanglan-ubuntu-server.tail4de4cb.ts.net:3002
```

Successfully logged into the Grafana web interface.

---

## Homepage Integration

Added Grafana to the Homepage dashboard under the Monitoring section.

Configuration:

```yaml
- Grafana:
    href: http://wutanglan-ubuntu-server.tail4de4cb.ts.net:3002
    description: Metrics Dashboard
    icon: grafana.png
```

Validated successful access through Homepage.

---

## Project 24 – Deploying Prometheus

### Deployment

Created a dedicated Prometheus project directory and Docker Compose configuration.

Configured persistent storage and mounted the Prometheus configuration file.

Created a custom prometheus.yml file defining scrape targets.

Initial configuration:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]
```

Deployed Prometheus using Docker Compose.

```bash
docker compose up -d
```

---

### Validation

Successfully accessed the Prometheus web interface.

```text
http://192.168.0.188:9090
```

Verified target health page and confirmed Prometheus was scraping itself successfully.

---

## Project 25 – Deploying Node Exporter

### Deployment

Created a dedicated Node Exporter project directory and Docker Compose configuration.

Node Exporter was deployed to expose Linux operating system metrics.

Metrics endpoint:

```text
http://192.168.0.188:9100/metrics
```

---

### Validation

Verified metrics collection by accessing:

```text
http://192.168.0.188:9100/metrics
```

Observed live metrics including:

* CPU statistics
* Memory statistics
* Filesystem statistics
* Network statistics
* System uptime

This confirmed Node Exporter was operating correctly.

---

## Prometheus Integration

Updated Prometheus configuration to scrape Node Exporter.

Added the following job:

```yaml
- job_name: "node-exporter"

  static_configs:
    - targets:
      - "192.168.0.188:9100"
```

Reloaded Prometheus.

```bash
docker compose down
docker compose up -d
```

---

### Validation

Navigated to:

```text
Status → Target Health
```

Confirmed:

```text
node-exporter  UP
prometheus     UP
```

This verified successful communication between Prometheus and Node Exporter.

---

## Grafana Data Source Configuration

Added Prometheus as a Grafana data source.

Configured URL:

```text
http://prometheus:9090
```

Initial configuration failed due to incorrect connectivity settings.

After correcting the datasource configuration and validating container communication, Grafana successfully connected to Prometheus.

Result:

```text
Successfully queried the Prometheus API.
```

---

## Linux Server Monitoring Dashboard

Imported Grafana Community Dashboard:

```text
Node Exporter Full
Dashboard ID: 1860
```

Selected the Prometheus datasource.

Successfully imported the dashboard and validated live metrics.

---

## Dashboard Metrics

The monitoring dashboard now provides visibility into:

* CPU Utilization
* Memory Utilization
* Disk Usage
* Filesystem Usage
* Network Traffic
* Load Average
* Uptime
* Process Statistics

Metrics are collected by Node Exporter, stored by Prometheus and visualized through Grafana.

---

## Outcome

Successfully deployed a complete monitoring stack consisting of Grafana, Prometheus and Node Exporter.

The solution provides centralized monitoring and observability for the Ubuntu monitoring server and forms the foundation for future infrastructure monitoring projects.

Future monitoring targets include:

* Proxmox Host (HP Mini)
* Jellyfin Server
* Ryzen Lab
* Additional Linux and Windows systems

---

## Skills Demonstrated

* Linux Administration
* Docker
* Docker Compose
* Infrastructure Monitoring
* Observability
* Prometheus Configuration
* Grafana Dashboard Management
* Node Exporter Deployment
* Service Troubleshooting
* Network Connectivity Validation
* Infrastructure Documentation
* Homelab Engineering
