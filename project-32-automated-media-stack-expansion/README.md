# Project 34–41: Automated Media Stack Expansion

## Overview

This project expanded the WutangLAN media platform from a basic Jellyfin server into a fully automated self-hosted media ecosystem.

The implementation focused on automating movie and TV management, integrating request management, improving storage, and creating a seamless workflow where users can request content directly from Jellyfin.

---

# Objectives

- Upgrade storage capacity
- Monitor drive health
- Automate movie downloads
- Automate TV show downloads
- Centralise indexer management
- Provide self-service media requests
- Integrate all services together
- Continue building practical Docker and Linux administration skills

---

# Environment

## Hardware

- Jellyfin Server
- 4TB Seagate IronWolf HDD
- External USB 3.0 HDD Enclosure
- Mini Rack
- TP-Link Switch
- BT Smart Hub
- BT Wi-Fi Extender (planned replacement with Powerline + RE700X)

---

## Software

- Windows 11
- Docker
- Docker Compose
- Jellyfin
- qBittorrent
- Prowlarr
- Sonarr
- Radarr
- Jellyseerr
- CrystalDiskInfo

---

# Storage Upgrade

Installed a new 4TB Seagate IronWolf drive inside a USB enclosure.

The drive became the primary storage location for:

- Movies
- TV Shows
- ROM Collections
- Future media expansion

The previous external drive was retained for backups.

---

# Drive Health Monitoring

CrystalDiskInfo was deployed using Microsoft Intune.

Purpose:

- SMART monitoring
- Temperature monitoring
- Drive health reporting
- Early warning of disk failures

This allows proactive maintenance before storage failures occur.

---

# qBittorrent

Configured qBittorrent as the primary download client.

Configured:

- Download location
- Completed download location
- Docker networking
- Integration with Sonarr
- Integration with Radarr

---

# Prowlarr

Implemented Prowlarr as the central index manager.

Configured:

- Indexers
- API integration
- Automatic synchronisation
- Connected Sonarr
- Connected Radarr

This removed the need to configure indexers individually.

---

# Sonarr

Configured Sonarr for television automation.

Features:

- TV monitoring
- Episode tracking
- Automatic searches
- Automatic imports
- Integration with qBittorrent

---

# Radarr

Configured Radarr for movie automation.

Features:

- Movie monitoring
- Automatic downloads
- Automatic imports
- Quality profiles
- Integration with qBittorrent

---

# Jellyseerr

Implemented Jellyseerr to provide self-service media requests.

Configured:

- Radarr integration
- Sonarr integration
- User permissions
- Request management

Users can browse available content and request new media without accessing the backend applications.

---

# Jellyfin Integration

Integrated Jellyseerr directly into Jellyfin.

Users can now request media directly from the Jellyfin interface.

Workflow:

1. User browses Jellyfin
2. User clicks the Favourite (❤️) icon
3. Jellyseerr receives the request
4. Sonarr or Radarr processes the request
5. Prowlarr searches configured indexers
6. qBittorrent downloads the media
7. Sonarr/Radarr imports completed files
8. Jellyfin updates the library automatically

---

# Final Architecture

```text
User
 │
 ▼
Jellyfin
 │
Favourite ❤️
 │
 ▼
Jellyseerr
 │
 ├─────────────┐
 │ │
 ▼ ▼
Sonarr Radarr
 │ │
 └──────┬──────┘
        │
        ▼
    Prowlarr
        │
        ▼
  Torrent Indexers
        │
        ▼
   qBittorrent
        │
        ▼
 Download Complete
        │
        ▼
Sonarr/Radarr Import
        │
        ▼
Jellyfin Library
        │
        ▼
User Streams Content
```

---

# Skills Demonstrated

- Docker
- Docker Compose
- Linux Administration
- Windows Administration
- Storage Management
- SMART Monitoring
- Media Automation
- API Integration
- Service Integration
- Network Troubleshooting
- Self-hosted Infrastructure
- Automation Workflows

---

# Outcome

Successfully transformed the WutangLAN media server into a fully automated self-hosted media platform.

The completed solution allows users to discover, request, download, organise and stream media with minimal manual intervention while providing a scalable architecture for future expansion.
