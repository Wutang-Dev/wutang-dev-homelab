# Project 20 – Immich Deployment on Proxmox

## Overview

This project involved deploying Immich, a self-hosted photo management platform, on my Proxmox server using Docker Compose. The primary goal was to gain hands-on experience with containerized application deployment, Docker networking, persistent storage, PostgreSQL databases, and Tailscale integration rather than implementing a long-term photo backup solution.

## Objectives

* Deploy Immich using Docker Compose
* Configure PostgreSQL and Redis containers
* Implement persistent storage for uploaded media and database data
* Test photo uploads and data persistence
* Explore Tailscale integration for remote access
* Troubleshoot common Docker deployment issues

## Environment

### Host System

* Proxmox VE 9.2.3
* HP Mini PC
* Docker Engine
* Docker Compose
* Tailscale

### Immich Components

* Immich Server
* Immich Machine Learning Service
* PostgreSQL Database
* Valkey (Redis)
* Tailscale Container (initial testing)

## Initial Deployment

Created an Immich Docker Compose configuration containing:

* Immich Server
* PostgreSQL Database
* Valkey Redis Cache
* Machine Learning Container
* Tailscale Container

The containers were deployed using:

```bash
docker compose up -d
```

## Issue 1 – Database Container Failure

### Symptoms

The PostgreSQL container continuously restarted.

Checking the logs revealed:

```text
FATAL: could not write to file "pg_wal/xlogtemp.xx":
No space left on device
```

### Investigation

Initial checks included:

```bash
df -h
```

```bash
lsblk -f
```

Disk usage showed:

* Root filesystem had over 50 GB available
* Docker storage was healthy

The issue was traced to incorrect volume mappings.

### Resolution

Created dedicated storage directories:

```bash
mkdir -p /opt/immich/upload
mkdir -p /opt/immich/database
mkdir -p /opt/immich/ts-config
mkdir -p /opt/immich/ts-state
```

Verified structure:

```bash
tree /opt/immich
```

Output:

```text
/opt/immich
├── database
├── ts-config
├── ts-state
└── upload
```

Updated the PostgreSQL volume mapping:

```yaml
volumes:
  - /opt/immich/database:/var/lib/postgresql/data
```

The database container successfully initialized after redeployment.

## Issue 2 – Persistent Storage Configuration

Configured persistent storage for uploaded images.

### Upload Storage

```yaml
volumes:
  - /opt/immich/upload:/usr/src/app/upload
```

### Database Storage

```yaml
volumes:
  - /opt/immich/database:/var/lib/postgresql/data
```

This ensured:

* Uploaded photos survive container recreation
* Database survives container recreation
* Configuration remains persistent

## Container Lifecycle Management

Stopping containers:

```bash
docker compose down
```

Starting containers:

```bash
docker compose up -d
```

Verifying status:

```bash
docker ps -a
```

## Tailscale Integration Testing

### Objective

Explore secure remote access without exposing ports to the public internet.

### Initial Configuration

Configured Tailscale Serve:

```bash
tailscale serve --bg http://127.0.0.1:2283
```

This exposed Immich through the tailnet using HTTPS.

### Validation

Successfully accessed Immich remotely through Tailscale.

## Testing Data Persistence

### Test Upload

Uploaded:

* Personal profile photo
* Wu-Tang Clan logo image

### Validation Process

1. Uploaded images
2. Logged out
3. Logged back in
4. Restarted containers
5. Verified images remained present

### Result

✅ Uploads persisted correctly

## Final Configuration

### Proxmox Access

```text
https://proxmox.tail4de4cb.ts.net
```

Provided secure remote access to the Proxmox management interface through Tailscale.

### Immich Access

```text
http://192.168.0.90:2283
```

Available locally on the home network.

## Skills Practiced

### Docker

* Docker Compose deployment
* Container lifecycle management
* Volume mappings
* Service dependencies
* Container networking

### Linux

* Directory creation
* Storage troubleshooting
* Filesystem inspection
* Command-line administration

### Databases

* PostgreSQL deployment
* Database persistence
* Database troubleshooting

### Networking

* Tailscale integration
* Local network access
* Remote access configuration
* Reverse proxy concepts

### Troubleshooting

* Log analysis
* Container restart loops
* Storage issues
* Volume configuration problems

## Key Commands Used

### Storage Verification

```bash
df -h
lsblk -f
```

### Directory Creation

```bash
mkdir -p /opt/immich/upload
mkdir -p /opt/immich/database
mkdir -p /opt/immich/ts-config
mkdir -p /opt/immich/ts-state
```

### Container Management

```bash
docker compose down
docker compose up -d
docker ps -a
```

### Tailscale

```bash
tailscale status
tailscale serve status
tailscale serve --bg http://127.0.0.1:2283
tailscale serve --https=443 off
```

## Lessons Learned

* Docker containers require correctly mapped persistent storage.
* PostgreSQL initialization errors can sometimes appear as storage issues even when disk space is available.
* Docker volume mappings should always be explicitly defined.
* Tailscale provides secure remote access without exposing services directly to the internet.
* Persistent storage should be verified before deploying production workloads.
* Testing uploads and container restarts is essential when validating self-hosted applications.

## Outcome

Successfully deployed Immich on Proxmox using Docker Compose, configured persistent storage for uploaded media and database data, validated image persistence through testing, and explored secure remote access using Tailscale.

Although Immich is not currently required as a production service, the project provided valuable hands-on experience with Docker, Linux administration, storage management, networking, and troubleshooting within a self-hosted environment.
