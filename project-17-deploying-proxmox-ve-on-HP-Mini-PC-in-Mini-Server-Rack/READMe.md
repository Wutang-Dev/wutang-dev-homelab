# Project 17 – Deploying Proxmox VE on HP Mini PC

## Overview

Deployed Proxmox Virtual Environment (PVE) onto a dedicated HP Mini PC as part of my ongoing homelab / mini server rack build.

The objective of this project was to introduce a dedicated virtualization platform to support future isolated lab environments, Linux workloads, container deployments, and infrastructure experimentation.

---

## Hardware

| Device | Purpose |
|---------|---------|
| HP Mini PC | Proxmox Host |
| Mini Rack | Compact infrastructure platform |
| Managed Switch | Network connectivity |
| Dedicated USB Installer | Proxmox installation media |

---

## Objectives

- Deploy a dedicated virtualization host
- Prepare infrastructure for future VM and container workloads
- Implement server-style remote management
- Integrate with existing homelab environment

---

## Deployment Process

### 1. Installation Media Creation

Created a bootable Proxmox USB installer.

Initial testing was performed using Ventoy, however a dedicated USB installer was later used to simplify deployment and validation.

---

### 2. BIOS / Boot Configuration

Configured the HP Mini PC to boot from USB installation media.

Verified successful boot into the Proxmox installer.

---

### 3. Proxmox Installation

Installed:

- Proxmox VE 9.x
- Default storage configuration
- Dedicated management interface

Configured:

- Hostname
- Static management IP
- Gateway
- DNS configuration

---

### 4. Initial Validation

Validated:

✅ Installation success  
✅ Network connectivity  
✅ ICMP reachability  
✅ SSH connectivity  
✅ Web UI access

Successfully connected to:

```text
https://<management-address>:8006
```

---

## Post Installation

Implemented:

- Community PVE post-install script
- Repository cleanup
- Package updates
- System reboot validation

Performed:

```bash
apt update
apt upgrade
```

---

## Results

Successful deployment of a dedicated Proxmox virtualization host.

Working features:

✅ Proxmox Web UI  
✅ SSH Management  
✅ Package Updates  
✅ Dedicated Virtualization Platform

---

## Key Learning

This project reinforced:

- Linux server deployment
- Hypervisor installation
- Boot media preparation
- Network configuration
- SSH administration
- System updates
- Infrastructure planning

---

## Next Steps

Planned future work:

- Secure remote management
- Tailscale integration
- VM deployment
- Container workloads
- Backup configuration
- Network segmentation experiments
