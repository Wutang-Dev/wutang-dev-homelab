# Project 28 - Monitoring Proxmox and Raspberry Pi with Prometheus & Grafana

## Overview

In this project I expanded my existing monitoring stack by adding both my Proxmox host and Raspberry Pi (Pi-hole) to Prometheus and Grafana.

The goal was to move beyond monitoring a single Ubuntu server and begin building a centralised monitoring platform capable of collecting metrics from multiple devices across my homelab.

By the end of the project I was successfully monitoring:

* Ubuntu Monitoring Server
* HP Mini Proxmox Host
* Raspberry Pi running Pi-hole

using a single Prometheus instance and Grafana dashboard.

---

## Objectives

* Install Node Exporter on Proxmox
* Install Node Exporter on Raspberry Pi
* Configure Prometheus to scrape metrics from multiple devices
* Validate Prometheus target health
* Visualise metrics in Grafana
* Create a central monitoring solution for the homelab

---

## Existing Environment

### Monitoring Server

Hostname: wutanglan-ubuntu-server

Services already running:

* Grafana
* Prometheus
* Homepage
* Uptime Kuma
* Node Exporter

### Devices to Monitor

#### HP Mini Proxmox Host

IP Address:

192.168.0.90

#### Raspberry Pi (Pi-hole)

Hostname:

pihole

IP Address:

192.168.0.99

---

## Step 1 - Install Node Exporter on Proxmox

I connected to the Proxmox host using SSH.

```bash
ssh root@proxmox
```

I installed Node Exporter using the Debian package repository.

```bash
apt update
apt install prometheus-node-exporter -y
```

After installation I verified the service was running.

```bash
systemctl status prometheus-node-exporter
```

The service showed:

```text
Active: active (running)
```

I also confirmed metrics were available on port 9100.

```bash
curl http://localhost:9100/metrics
```

Metrics were successfully returned.

---

## Step 2 - Install Node Exporter on Raspberry Pi

I connected to my Raspberry Pi running Pi-hole.

```bash
ssh ravi@pihole
```

I updated the Pi-hole installation.

```bash
sudo pihole -up
```

I then installed Node Exporter.

```bash
sudo apt update
sudo apt install prometheus-node-exporter -y
```

I verified the service status.

```bash
systemctl status prometheus-node-exporter
```

The service showed as active and running.

To confirm Node Exporter was working correctly I tested the metrics endpoint.

```bash
curl http://localhost:9100/metrics
```

The endpoint returned Prometheus metrics successfully.

---

## Step 3 - Configure Prometheus

I opened the Prometheus configuration file.

```bash
cd ~/prometheus
nano prometheus.yml
```

I updated the Node Exporter scrape targets.

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
          - "192.168.0.99:9100"
```

Where:

* 192.168.0.188 = Ubuntu Monitoring Server
* 192.168.0.90 = Proxmox Host
* 192.168.0.99 = Raspberry Pi

---

## Step 4 - Restart Prometheus

After updating the configuration file I restarted the Prometheus container.

```bash
docker compose restart
```

I then opened the Prometheus web interface.

```text
http://wutanglan-ubuntu-server:9090/targets
```

All targets reported:

```text
UP
```

This confirmed Prometheus was successfully scraping metrics from all three systems.

---

## Step 5 - Validate Grafana

I opened Grafana and accessed the existing Node Exporter Full dashboard.

The dashboard automatically detected all monitored hosts.

Available systems included:

* Ubuntu Monitoring Server
* Proxmox Host
* Raspberry Pi

Using the dashboard filters I could switch between devices and view:

* CPU utilisation
* Memory usage
* Disk usage
* Uptime
* Network activity
* System performance metrics

No additional dashboards were required because the existing dashboard could display metrics from multiple Node Exporter instances.

---

## Monitoring Architecture

```text
Grafana
   │
   ▼
Prometheus
   │
   ├── Ubuntu Monitoring Server (192.168.0.188)
   │
   ├── HP Mini Proxmox Host (192.168.0.90)
   │
   └── Raspberry Pi / Pi-hole (192.168.0.99)
```

---

## Skills Practised

* Linux administration
* SSH management
* Prometheus configuration
* YAML editing
* Grafana dashboards
* Infrastructure monitoring
* Service validation
* Troubleshooting
* Homelab observability
* Raspberry Pi administration
* Proxmox administration

---

## Outcome

Project 28 successfully expanded the monitoring platform from a single monitored host to a multi-device monitoring solution.

Prometheus now collects metrics from Ubuntu, Proxmox and Raspberry Pi devices, while Grafana provides a centralised dashboard for visualising system performance across the homelab.

This project introduced the foundations of infrastructure observability and provides a scalable monitoring platform that can be expanded in future projects to include Windows devices, virtual machines, containers and additional services.
