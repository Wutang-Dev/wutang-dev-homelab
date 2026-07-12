# Project 34 - Troubleshooting the ARR Stack After a Network Migration

## Overview

Following the migration of my Jellyfin server from the **Wutanglan router** to the **BT Wi-Fi extender**, I discovered that my ARR stack had stopped functioning correctly.

Although the Docker containers were all running, **Radarr, Sonarr and Prowlarr were no longer able to communicate with each other or qBittorrent**.

This project focused on identifying the root cause, restoring communication between the services and understanding how network changes can impact self-hosted applications.

---

# Objective

Restore communication between:

- Prowlarr
- Radarr
- Sonarr
- qBittorrent

after changing the network topology of the homelab.

---

# Environment

| Component | Platform |
|-----------|----------|
| Ubuntu Server | Docker Engine |
| Jellyfin | Docker |
| Radarr | Docker |
| Sonarr | Docker |
| Prowlarr | Docker |
| qBittorrent | Docker |
| BT Smart Hub | DHCP Server |
| BT Wi-Fi Extender | Connected media server |

---

# Problem

Following the network migration I observed multiple health warnings across the ARR applications.

### Radarr

- All RSS-capable indexers unavailable
- All search-capable indexers unavailable
- Indexers unavailable for more than 6 hours

### Sonarr

- Unable to communicate with qBittorrent
- Download client unavailable
- Indexer unavailable

### Prowlarr

- Indexers failing health checks
- Unable to communicate with connected applications

At first glance it appeared that multiple services had failed simultaneously.

---

# Investigation

Rather than rebuilding containers immediately, I worked through the problem logically.

## Step 1

Verified that all Docker containers were running.

All containers were healthy.

---

## Step 2

Checked qBittorrent.

The application itself was functioning correctly.

---

## Step 3

Reviewed the health status within Radarr, Sonarr and Prowlarr.

This confirmed that every failure involved communication between applications rather than application crashes.

---

## Step 4

Compared the configured host addresses with the current IP address of the Jellyfin server.

This revealed that the server had obtained a **new IP address** after being connected through the BT Wi-Fi extender.

---

# Root Cause

The migration changed the IP address assigned to the server by DHCP.

Prowlarr, Radarr and Sonarr were still configured to communicate using the previous IP address.

Because every application relied on the old address, communication between services failed even though the containers themselves were healthy.

---

# Resolution

Updated the application host addresses throughout the ARR stack.

## Prowlarr

Updated:

- Radarr application
- Sonarr application

with the new server IP address.

---

## Radarr

Updated:

- qBittorrent download client

using the new IP address.

---

## Sonarr

Updated:

- qBittorrent download client

using the new IP address.

---

## Verification

Performed connection tests within each application.

Confirmed:

- Prowlarr connected successfully
- Radarr connected successfully
- Sonarr connected successfully
- qBittorrent connected successfully
- Indexers synchronised correctly
- Health warnings cleared

---

# Outcome

The ARR stack returned to full operation without rebuilding any Docker containers.

Media requests, indexer synchronisation and download client communication were all restored.

---

# Skills Practised

- Docker troubleshooting
- Linux networking
- DHCP troubleshooting
- Self-hosted application management
- Service dependency analysis
- Root cause analysis
- Network migration validation

---

# Lessons Learned

Changing network infrastructure can unintentionally change the IP address of self-hosted services.

Applications configured with static IP addresses will fail if those addresses change.

Rather than assuming Docker was broken, following a structured troubleshooting process made it possible to identify the real issue quickly.

This project also reinforced the importance of:

- DHCP reservations
- Static addressing for servers
- Testing application dependencies after network changes
- Using health dashboards to identify communication failures

---

# Future Improvements

- Configure DHCP reservations for all homelab servers.
- Replace IP-based configuration with Docker DNS where possible.
- Document application dependencies within the homelab.
- Create a post-migration validation checklist for future network changes.

---

# Conclusion

This project demonstrated how a simple network migration can affect multiple interconnected Docker services.

By analysing health checks, validating connectivity and tracing application dependencies, I restored the complete ARR stack without redeploying any containers.

The experience reinforced the importance of understanding networking fundamentals alongside Docker and Linux administration, as infrastructure changes often impact service communication more than the applications themselves.
