# 2026-01-26 – Project 07 – Nginx Reverse Proxy (Local + Remote Services)

## Overview
In this project, I configured Nginx on my Ubuntu MacBook to function as a reverse proxy for multiple backend services.

The objective was to understand how a reverse proxy routes traffic to different applications, including both locally hosted services and remote services accessed over a private Tailscale network.

This builds directly on Project 06 (Nginx installation and firewall configuration).

---

## Environment

Host: MacBook  
OS: Ubuntu  
Web Server: Nginx  
Firewall: UFW (enabled)  
Private Network: Tailscale  

Backends:
- Python HTTP Test App (localhost:9000)
- Pi-hole Admin Interface (Raspberry Pi via Tailscale IP)

---

## Architecture

Traffic Flow:

Client → Nginx (Port 80) → Backend Service

Path-Based Routing:

- `/app/` → Python HTTP Test App
- `/pihole/` → Pi-hole Admin UI

This setup allows multiple services to be accessed through a single entry point while maintaining backend isolation.

---

## Why Python HTTP Instead of Jellyfin?

Jellyfin is actively used within my home environment.  
To avoid disrupting a production media service, I deployed a lightweight Python HTTP server for safe reverse proxy testing:

```bash
python3 -m http.server 9000
```

This ensured:
- No service downtime
- No disruption to household streaming
- A controlled backend for reverse proxy experimentation

---

## Nginx Configuration (Tracked Copy)

The live configuration file exists at:

```
/etc/nginx/sites-available/project-07-reverse-proxy
```

The version stored in this repository is a tracked copy for documentation and version control purposes.

Core configuration used for this project:

```nginx
server {
    listen 80;
    server_name localhost;

    location /app/ {
        proxy_pass http://localhost:9000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /pihole/ {
        proxy_pass http://<PIHOLE_IP>/admin/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

Important:
- Trailing slashes in `proxy_pass` are required for correct path handling.
- The Pi-hole IP should be replaced with the Raspberry Pi's Tailscale or LAN address.

---

## Validation Process

### 1. Verified backend services directly

```bash
curl http://localhost:9000
curl http://<PIHOLE_IP>/admin
```

Both returned valid responses before introducing the reverse proxy layer.

---

### 2. Tested Nginx configuration safely

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Reload was used instead of restart to avoid unnecessary service interruption.

---

### 3. Confirmed reverse proxy routing

Tested via browser and curl:

- http://localhost/app/
- http://localhost/pihole/

The Python test app loaded successfully through Nginx.  
Pi-hole admin interface loaded through the reverse proxy without affecting DNS functionality.

---

### 4. Confirmed DNS was unaffected

```bash
nslookup google.com
```

This validated that Pi-hole DNS (port 53) remained operational and separate from the proxied web interface (port 80).

---

## Key Concepts Reinforced

- Separation between DNS services and web management interfaces
- Reverse proxy fundamentals using `proxy_pass`
- Path-based routing with Nginx `location` blocks
- Importance of forwarding headers in proxied environments
- Impact of trailing slashes in Nginx configurations
- Safe change management in a live home network
- Validation before reload to reduce service risk

---

## Outcome

- Successfully proxied both local and remote services through a single Nginx entry point.
- Maintained full DNS functionality across WuTangLAN.
- Implemented realistic reverse proxy architecture using private networking.
- Practiced structured configuration testing and controlled reload procedures.

---

## Next Steps

- Implement HTTPS using self-signed certificates
- Restrict backend services to localhost where possible
- Containerise Nginx using Docker
- Create a structured break-and-fix troubleshooting lab

