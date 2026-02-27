# Project 12 – Uptime Kuma Monitoring Stack

## 🎯 Objective

Deploy centralized service monitoring within the WuTang Dev Homelab to introduce structured observability, service health validation, and remote access verification using Uptime Kuma.

This project implements layered monitoring similar to production infrastructure environments.

---

## 🏗 Environment Overview

**Monitoring Node**
- Ubuntu 24.04 LTS
- Docker
- Private overlay network (VPN)

**Services Monitored**
- Network Gateway
- Monitoring Node
- Primary DNS Server
- Secondary DNS Server
- Media Server (Internal)
- Media Server (Remote Tunnel Path)

---

## 🚀 Deployment Steps

### 1. Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

### 2. Deploy Uptime Kuma

```bash
docker run -d \
  --name uptime-kuma \
  -p 3001:3001 \
  -v $(pwd)/data:/app/data \
  --restart unless-stopped \
  louislam/uptime-kuma:latest
```

Access dashboard:

```
http://<monitoring-node>:3001
```

---

## 📊 Monitoring Architecture

### Layer 1 – Infrastructure Monitoring (Ping)

| Service | Type | Purpose |
|----------|--------|----------|
| Network Gateway | Ping | Detect upstream connectivity loss |
| Monitoring Node | Ping | Detect host-level failure |
| DNS Server (Primary) | Ping | Validate DNS availability |
| DNS Server (Secondary) | Ping | Validate DNS redundancy |

---

### Layer 2 – Application Monitoring (HTTP)

| Service | Type | Purpose |
|----------|--------|-------------------------------|
| Media Server (Internal) | HTTP | Validate application health |
| Media Server (Remote Path) | HTTP | Validate encrypted tunnel access |

**HTTP Configuration**

- Accepted Status Codes: `200-299`
- Retries: `2`
- Heartbeat Interval: `30 seconds`

---

## 🔍 Failure Isolation Design

| Scenario | Interpretation |
|------------|----------------|
| Ping 🟢 + HTTP 🔴 | Application failure |
| Internal 🟢 + Remote 🔴 | Tunnel/VPN issue |
| All 🔴 | Host offline |
| Infrastructure 🟢 + External Monitor 🔴 | ISP outage |

This layered model enables structured troubleshooting instead of reactive guesswork.

---

## 🔐 Security Model

- Services accessible only via private overlay network
- No public port exposure
- No direct internet-facing services
- Monitoring node isolated within internal segment

---

## 📈 Results

- Centralized monitoring dashboard operational
- Infrastructure + Application observability established
- Remote path validation implemented
- Uptime tracking active

---

## 🧠 Key Learning Outcomes

- Docker container deployment
- Observability fundamentals
- Layered monitoring architecture
- Service vs host health validation
- Remote tunnel path verification
- Structured failure isolation

---

## 🔮 Future Improvements

- External dependency monitoring
- Alerting integrations (Email/Telegram/Discord)
- Reverse proxy deployment
- SSL automation with certificate management
- Service containerization expansion

---

## 🏁 Status

Internal monitoring stack deployed.

Observability layer successfully integrated into homelab environment.
