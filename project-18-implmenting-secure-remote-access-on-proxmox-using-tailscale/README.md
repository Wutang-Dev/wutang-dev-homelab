# Project 18 – Implementing Secure Remote Access on Proxmox using Tailscale

## Overview

Implemented secure remote access for my Proxmox host using Tailscale.

The goal was to enable remote infrastructure management without exposing management ports publicly through router port forwarding.

---

## Objectives

- Enable secure remote access
- Avoid exposing Proxmox to the public internet
- Implement overlay networking
- Use hostname-based management access

---

## Deployment Steps

### 1. Tailscale Installation

Installed Tailscale directly onto the Proxmox host.

Validated service installation and node registration.

---

### 2. Authentication & Node Join

Joined the Proxmox host to my private Tailnet.

Validated:

✅ Device registration  
✅ Tailnet connectivity  
✅ Peer visibility

---

### 3. Connectivity Testing

Validated:

- SSH access over Tailscale
- Remote browser access
- Cross-device connectivity

Successfully tested:

```bash
ssh root@proxmox
```

---

### 4. MagicDNS Implementation

Configured hostname-based access using MagicDNS.

Successfully accessed Proxmox via:

```text
https://proxmox:8006
```

instead of relying on:

- Local LAN IP addresses
- Manual overlay IP memorisation

---

### 5. Mobile Validation

Tested remote access from a secondary device.

Validated successful login via:

- Tailscale overlay networking
- Hostname resolution
- Secure HTTPS access

---

## Results

Implemented secure remote administration without router port forwarding.

Working functionality:

✅ Tailscale Connectivity  
✅ SSH Remote Access  
✅ Proxmox Web UI Remote Access  
✅ MagicDNS Resolution  
✅ Cross Device Management

---

## Architecture

```text
Remote Device
     ↓
Tailscale Tailnet
     ↓
Proxmox Host
     ↓
HTTPS Management Interface
```

---

## Security Benefits

Benefits of this approach:

- No public port exposure
- Encrypted overlay networking
- Private infrastructure access
- Simplified hostname management

---

## Key Learning

This project reinforced:

- Overlay networking
- Secure remote administration
- Linux package deployment
- SSH management
- DNS abstraction
- Infrastructure security concepts

---

## Next Steps

Future work:

- Deploy Ubuntu Server VM
- Implement containers
- Backup automation
- Service monitoring
- Network segmentation
