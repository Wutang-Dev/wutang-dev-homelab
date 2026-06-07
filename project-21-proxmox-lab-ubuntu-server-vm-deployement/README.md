# Proxmox Lab – Ubuntu Server VM Deployment

## Objective

Deploy and configure my first Ubuntu Server virtual machine within Proxmox and gain familiarity with the Proxmox VM creation workflow.

## Tasks Completed

### 1. Update Existing Infrastructure

Updated both Proxmox and Pi-hole to ensure the environment was running the latest available packages.

**Proxmox**

```bash
apt update
apt upgrade
```

**Pi-hole**

```bash
sudo apt update
sudo apt upgrade
```

### 2. ISO Management

Reviewed the process for uploading ISO files into Proxmox.

Rather than uploading my entire ISO collection, I uploaded a single Ubuntu Server ISO from my ISO repository hosted on the Jellyfin PC. This helped conserve storage while I continue learning how Proxmox manages disk allocation.

### 3. Create Ubuntu Server Virtual Machine

Created my first Linux virtual machine within Proxmox.

Configuration:

* VM Name: Ubuntu-Server
* VM ID: 100
* Operating System: Ubuntu Server
* CPU: 2 vCPUs
* Memory: 2 GB RAM
* QEMU Guest Agent: Enabled
* Start at Boot: Enabled

### 4. Install Ubuntu Server

Installed Ubuntu Server using the uploaded ISO.

As I have previously deployed Ubuntu Server using Hyper-V, the installation process was familiar. The main differences encountered were Proxmox-specific terminology and management options.

### 5. Initial Server Configuration

Configured the server hostname:

```text
wutanglan-ubuntu-server
```

Enabled SSH during installation to allow remote administration from other devices on the network, including:

* Jellyfin Server
* Ryzen-Lab

## Key Learning Points

* Updating Proxmox and Linux systems using apt.
* Uploading and managing ISO files within Proxmox.
* Creating virtual machines using Proxmox.
* Understanding the role of the QEMU Guest Agent.
* Configuring CPU and memory allocation for Linux VMs.
* Installing Ubuntu Server within a Proxmox environment.
* Enabling SSH for remote management.
* Comparing Proxmox VM deployment with previous Hyper-V experience.

## Outcome

Successfully deployed and configured an Ubuntu Server virtual machine in Proxmox. The server is operational, accessible via SSH, and ready for future Linux administration and self-hosting projects.
