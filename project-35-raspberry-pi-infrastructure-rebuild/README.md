# Project 35 - Raspberry Pi Infrastructure Rebuild

## Overview

Following a major network troubleshooting session involving BT Hub, Wi-Fi extenders, WutangLAN and the ARR stack, I decided to redesign part of my homelab infrastructure.

Rather than hosting infrastructure services inside the mini rack, the Raspberry Pi was rebuilt from scratch and moved directly onto the BT network.

The objective was to create a dedicated infrastructure node responsible for core network services such as DNS, monitoring and management, while allowing the Jellyfin server to focus entirely on media services.

---

## Objectives

- Rebuild the Raspberry Pi from scratch.
- Deploy Raspberry Pi OS Lite.
- Enable headless administration using SSH.
- Install Docker and Docker Compose.
- Configure the Raspberry Pi as a reusable Docker host.
- Integrate Git for infrastructure documentation.
- Prepare the platform for infrastructure containers.

---

## Why This Change?

During network troubleshooting I discovered that placing multiple layers of networking between BT and the homelab increased operational complexity.

Previous topology:

BT Hub

↓

Wi-Fi Extender

↓

WutangLAN Router

↓

Mini Rack

↓

Infrastructure Services

↓

Applications

While functional, this introduced unnecessary dependencies between production media services and infrastructure components.

The new design separates infrastructure from production workloads.

---

## New Architecture

BT Hub

├── Raspberry Pi (Infrastructure)

│ ├── Pi-hole

│ ├── Monitoring

│ ├── Docker Host

│ └── Git Documentation

│

└── WutangLAN Router

↓

Jellyfin Server

↓

ARR Stack

↓

Media Services

---

## Build Process

The Raspberry Pi was rebuilt using Raspberry Pi Imager with:

- Raspberry Pi OS Lite
- SSH enabled
- Headless configuration
- Initial network configuration
- Raspberry Pi Connect enabled

After booting:

- Connected via SSH
- Updated the operating system
- Installed Docker Engine
- Installed Docker Compose
- Added the user to the Docker group
- Validated Docker installation
- Created the standard Docker workspace
- Created a GitHub workspace
- Installed Git
- Cloned project repositories

---

## Validation

The following checks were completed successfully:

- SSH connectivity
- Docker Engine
- Docker Compose
- Hello World container
- Git installation
- GitHub repository cloning
- Documentation repository push

---

## Documentation

Rather than duplicating installation steps within project documentation, the complete Linux host build process has been documented separately within the Wutang Runbooks repository.

Runbook:

Linux Docker Host Bootstrap

---

## Lessons Learned

Large networking changes can have unexpected consequences across dependent services.

Separating infrastructure services from application services simplifies troubleshooting and reduces operational risk.

Maintaining reusable runbooks enables faster recovery and consistent server deployments.

Treating infrastructure as documented code improves repeatability and reduces reliance on memory.

---

## Next Steps

- Deploy Pi-hole using Docker Compose.
- Deploy Homepage.
- Deploy Uptime Kuma.
- Deploy Dozzle.
- Deploy Grafana.
- Deploy Prometheus.
- Continue building a dedicated infrastructure node for the homelab.
