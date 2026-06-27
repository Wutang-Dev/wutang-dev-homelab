# Project 29 - Repurposing a Toshiba Laptop into a Linux Docker Learning Workstation

## Overview

The goal of this project was to repurpose an old Toshiba laptop into a dedicated Ubuntu-based Linux workstation for learning Docker, Linux administration, and self-hosting technologies.

Initially, the laptop was intended to become a second Jellyfin server for the family. After reviewing my existing homelab architecture, I decided to continue using my production Jellyfin server hosted on my Wutanglan Proxmox environment and instead dedicate the Toshiba to Linux and Docker learning.

This approach allows me to experiment freely without affecting my production environment.

---

## Objectives

* Install Ubuntu Desktop.
* Configure secure remote management.
* Install Docker and Docker Compose.
* Install development tools.
* Integrate the workstation into my existing Tailscale network.
* Prepare the workstation for future Docker projects.

---

## Hardware

* Toshiba Laptop
* AMD E1-2100 APU
* 4GB RAM
* Ubuntu Desktop 22.04 LTS

---

## Challenges

### Ubuntu 24.04 Installation

During installation Ubuntu 24.04 repeatedly failed to boot correctly and displayed watchdog soft lockup errors.

After troubleshooting, I decided to install Ubuntu 22.04 LTS instead.

Ubuntu 22.04 booted successfully and completed the installation without issues, demonstrating the importance of selecting an operating system version that is compatible with older hardware.

---

## System Configuration

Completed the following configuration:

* Updated Ubuntu using:

```bash
sudo apt update
sudo apt upgrade
```

* Installed OpenSSH Server.

* Verified SSH service.

* Installed Docker.

* Installed Docker Compose.

* Verified Docker using:

```bash
docker run hello-world
```

* Installed Tailscale.

* Joined my existing Tailnet.

* Enabled Tailscale SSH.

* Installed Google Chrome.

* Installed Visual Studio Code.

* Installed the Tailscale Visual Studio Code extension.

---

## Remote Administration

The workstation can now be managed remotely from my existing Windows machines.

Successfully tested SSH from my Jellyfin workstation to the Ubuntu laptop over Tailscale.

Following a reboot I confirmed:

* SSH automatically starts.
* Tailscale automatically reconnects.
* Docker remains operational.

This means the laptop can remain permanently connected while being administered remotely.

---

## Final Architecture

Production Environment

* HP Mini Proxmox Server
* Jellyfin
* ROMM
* Pi-hole
* Grafana
* Prometheus
* Uptime Kuma

Learning Environment

* Ubuntu Desktop 22.04
* Docker
* Docker Compose
* Visual Studio Code
* Tailscale
* SSH

Administration

* Managed remotely from Ryzen Lab and Jellyfin PC via SSH.

---

## Lessons Learned

* Older hardware may require an earlier Linux LTS release.
* Docker installation and verification on Ubuntu.
* Secure remote administration using OpenSSH and Tailscale.
* Building Linux systems using a repeatable deployment process.
* Separating production services from a learning environment.

---

## Future Projects

* Homepage
* Portainer
* Uptime Kuma
* AdGuard Home (learning environment only)
* File Browser
* Nginx Proxy Manager
* Vaultwarden
* Docker networking
* Linux administration
* Bash scripting

---

## Outcome

This project transformed an unused Toshiba laptop into a dedicated Linux and Docker learning workstation.

Rather than duplicating production services, the workstation will be used to learn Linux administration, Docker, self-hosting, networking, and automation while my production homelab continues running independently on Proxmox.
