# Project 26 – Proxmox Monitoring with Prometheus and Grafana

## Objective

Extend the existing monitoring stack to include the Proxmox host (HP Mini PC) alongside the Ubuntu monitoring server using Prometheus, Node Exporter, and Grafana.

---

## Environment

### Monitoring Server

* Ubuntu Server
* Docker
* Prometheus
* Grafana
* Homepage
* Uptime Kuma

### Monitored Devices

| Device                   | IP Address    | Monitoring Method           |
| ------------------------ | ------------- | --------------------------- |
| Ubuntu Monitoring Server | 192.168.0.188 | Node Exporter (Docker)      |
| Proxmox HP Mini Host     | 192.168.0.90  | Node Exporter (APT Package) |

---

## Implementation

### Step 1 – Install Node Exporter on Proxmox

Connected to the Proxmox host using Tailscale SSH.

Verified package availability:

```bash
apt update
apt install prometheus-node-exporter -y
```

Verified service status:

```bash
systemctl status prometheus-node-exporter
```

Result:

```text
Active: active (running)
```

---

### Step 2 – Validate Metrics Endpoint

Confirmed that Node Exporter was serving metrics on port 9100.

```bash
curl http://192.168.0.90:9100/metrics
```

Result:

Large metrics output successfully returned.

This confirmed:

* Node Exporter installation successful
* Port 9100 accessible
* Metrics available for Prometheus scraping

---

### Step 3 – Configure Prometheus Target

Updated Prometheus configuration file.

File:

```bash
~/prometheus/prometheus.yml
```

Configuration:

```yaml
global:
  scrape_interval: 15s

scrape_configs:

  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9090"]

  - job_name: "node-exporter"
    static_configs:
      - targets:
        - "192.168.0.188:9100"
        - "192.168.0.90:9100"
```

Added:

```yaml
192.168.0.90:9100
```

for the Proxmox host.

---

### Step 4 – Reload Prometheus

Restarted Prometheus container.

```bash
cd ~/prometheus

docker compose down
docker compose up -d
```

Verified containers:

```bash
docker ps
```

Result:

```text
prometheus     Up
grafana        Up
node-exporter  Up
homepage       Up
uptime-kuma    Up
```

---

### Step 5 – Validate Prometheus Target

Opened:

```text
http://192.168.0.188:9090
```

Navigated to:

Status → Target Health

Verified target status:

```text
proxmox
192.168.0.90:9100
UP
```

Result:

Prometheus successfully scraping Proxmox metrics.

---

### Step 6 – Validate Grafana Dashboard

Opened Grafana dashboard:

```text
Node Exporter Full
```

Selected:

```text
Nodename = proxmox
Instance = 192.168.0.90:9100
```

Dashboard successfully displayed:

* CPU Usage
* Memory Usage
* Disk Usage
* Uptime
* Core Count
* Total RAM

Example values observed:

```text
CPU Usage: 95.7%
Memory Usage: 32.6%
Disk Usage: 31.6%
Uptime: 1.6 weeks
CPU Cores: 6
Memory: 15 GiB
```

---

## Skills Practiced

* Linux server administration
* Prometheus configuration
* Infrastructure monitoring
* Service validation
* Docker container management
* Grafana dashboard configuration
* Tailscale remote administration
* Proxmox monitoring

---

## Outcome

Successfully expanded the monitoring platform from a single monitored host to a multi-device monitoring solution.

The monitoring stack now provides centralized visibility into:

* Ubuntu Monitoring Server
* Proxmox HP Mini Host

using:

* Prometheus
* Node Exporter
* Grafana

This forms the foundation for future monitoring of:

* Raspberry Pi (Pi-hole)
* Jellyfin Server
* Additional Proxmox nodes
* Virtual Machines
* Containers

and moves the homelab closer to an enterprise-style monitoring architecture.

