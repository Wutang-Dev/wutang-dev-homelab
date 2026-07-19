# Project 37 – Deploying Uptime Kuma for Centralized Homelab Monitoring with Docker Compose

## Overview

This project focused on deploying **Uptime Kuma** as a centralized monitoring platform for my homelab infrastructure and self-hosted services.

Uptime Kuma was deployed as a Docker container on my Raspberry Pi using Docker Compose. The deployment forms part of my **30-Day Docker and Self-Hosting Roadmap** and builds upon the Raspberry Pi infrastructure established in previous projects.

The goal was to create a central dashboard capable of continuously monitoring the availability of critical network infrastructure, DNS services, media services, and the ARR stack.

The Docker Compose configuration was also committed to my `WutangDev-SelfHosting` GitHub repository, allowing the deployment configuration to be version controlled and supporting an **Infrastructure as Code (IaC)** approach.

---

## Project Objectives

The objectives of this project were to:

- Deploy Uptime Kuma using Docker Compose.
- Host Uptime Kuma on the Raspberry Pi.
- Configure persistent storage for Uptime Kuma.
- Verify the Docker Compose configuration before deployment.
- Verify the health of the running container.
- Access the Uptime Kuma web dashboard.
- Configure centralized monitoring for homelab infrastructure.
- Monitor the BT Router.
- Monitor Pi-hole.
- Monitor Jellyfin.
- Monitor Jellyseerr.
- Monitor the ARR stack.
- Monitor qBittorrent.
- Configure regular service availability checks.
- Store the Docker Compose configuration in GitHub.
- Continue developing an Infrastructure as Code approach for self-hosted services.

---

## Environment

The Uptime Kuma deployment was hosted on my Raspberry Pi, which is being developed as a dedicated infrastructure and monitoring server.

The environment included:

- Raspberry Pi
- Raspberry Pi OS
- Docker
- Docker Compose
- Git
- GitHub
- Visual Studio Code Remote SSH
- Tailscale
- Pi-hole
- Uptime Kuma
- BT Router
- Jellyfin Server
- Jellyseerr
- Radarr
- Sonarr
- Prowlarr
- qBittorrent

The Raspberry Pi uses the following reserved IP address:

```text
192.168.1.111
```

The Jellyfin media server currently uses:

```text
192.168.1.188
```

The BT Router uses:

```text
192.168.1.254
```

---

## Architecture

The monitoring architecture implemented during this project is:

```text
                    BT Router
                 192.168.1.254
                       │
                       │
                 Local Network
                       │
          ┌────────────┴────────────┐
          │                         │
          │                         │
    Raspberry Pi              Jellyfin Server
   192.168.1.111               192.168.1.188
          │                         │
          │                         ├── Jellyfin
          ├── Pi-hole               │
          │                         ├── Jellyseerr
          └── Uptime Kuma           │
                                    ├── Radarr
                                    │
                                    ├── Sonarr
                                    │
                                    ├── Prowlarr
                                    │
                                    └── qBittorrent
```

Uptime Kuma now acts as the centralized availability monitoring platform for these services.

---

# Part 1 – Creating the Uptime Kuma Project Directory

A dedicated directory was created inside the `WutangDev-SelfHosting` Git repository for the Uptime Kuma deployment.

The project directory contains the Docker Compose configuration required to recreate the Uptime Kuma container.

The deployment configuration is stored separately from the live Docker application data so that runtime data is not committed to GitHub.

This separation supports a cleaner Infrastructure as Code model.

The repository stores:

```text
Docker Compose configuration
```

The Docker environment stores:

```text
Persistent application data
```

This means the GitHub repository contains the instructions required to deploy the service rather than the live runtime database and application state.

---

# Part 2 – Creating the Docker Compose Configuration

A `docker-compose.yml` file was created for the Uptime Kuma deployment.

The configuration used was:

```yaml
services:
  uptime-kuma:
    image: louislam/uptime-kuma:1
    container_name: uptime-kuma
    restart: unless-stopped

    ports:
      - "3001:3001"

    volumes:
      - uptime-kuma-data:/app/data

volumes:
  uptime-kuma-data:
```

This configuration defines the Uptime Kuma service and provides persistent storage for its application data.

---

# Part 3 – Understanding the Docker Compose Configuration

The following Docker image was used:

```text
louislam/uptime-kuma:1
```

The container was assigned the name:

```text
uptime-kuma
```

The restart policy was configured as:

```text
unless-stopped
```

This allows the Uptime Kuma container to automatically restart following a Docker service restart or Raspberry Pi reboot unless the container has been intentionally stopped.

The following port mapping was configured:

```text
3001:3001
```

This exposes the Uptime Kuma web interface on TCP port `3001`.

A named Docker volume was configured:

```text
uptime-kuma-data
```

The volume is mounted inside the container at:

```text
/app/data
```

This ensures that Uptime Kuma configuration and monitoring data persist independently of the container lifecycle.

---

# Part 4 – Validating the Docker Compose Configuration

Before deploying the container, the Docker Compose configuration was validated using:

```bash
docker compose config
```

The command successfully parsed the Compose file and displayed the resulting Docker configuration.

The validation confirmed the configuration included:

- Uptime Kuma service.
- `louislam/uptime-kuma:1` Docker image.
- TCP port `3001`.
- Persistent Docker volume.
- Default Docker network.
- `unless-stopped` restart policy.

Validating the configuration before deployment helped identify potential YAML formatting or configuration errors before creating the container.

---

# Part 5 – Deploying Uptime Kuma

The Uptime Kuma container was deployed using:

```bash
docker compose up -d
```

Docker successfully:

- Pulled the Uptime Kuma image.
- Created the Docker network.
- Created the persistent Docker volume.
- Created the Uptime Kuma container.
- Started the container.

The `-d` option runs the container in detached mode.

---

# Part 6 – Verifying the Deployment

The running container was verified using:

```bash
docker compose ps
```

The output confirmed that the Uptime Kuma container was running successfully.

The container reported:

```text
Up
Healthy
```

The port mapping confirmed that TCP port `3001` was exposed from the container to the Raspberry Pi host.

This verified that the Docker deployment itself was operational before configuring monitoring.

---

# Part 7 – Accessing the Uptime Kuma Dashboard

The Uptime Kuma dashboard was accessed using the Raspberry Pi IP address and port `3001`.

```text
http://192.168.1.111:3001
```

The web interface loaded successfully.

The initial Uptime Kuma configuration was completed and the monitoring dashboard became available.

At this stage, Uptime Kuma was ready to begin monitoring the homelab infrastructure.

---

# Part 8 – Monitoring Pi-hole

Pi-hole was added to Uptime Kuma as one of the monitored services.

Pi-hole is hosted on the same Raspberry Pi as Uptime Kuma.

The Pi-hole server uses:

```text
192.168.1.111
```

Monitoring Pi-hole provides visibility into the availability of one of the core network services in the homelab.

Because Pi-hole provides DNS filtering for selected devices, monitoring its availability helps identify potential DNS-related outages.

---

# Part 9 – Monitoring the BT Router

The BT Router was added to Uptime Kuma using its local network address:

```text
192.168.1.254
```

The router was configured as a monitored network device.

This provides a basic availability check for the primary network gateway.

Monitoring the router alongside individual services helps distinguish between:

- Individual application failures.
- Docker container failures.
- Server failures.
- DNS failures.
- Wider network connectivity problems.

This creates a more useful monitoring hierarchy.

---

# Part 10 – Monitoring Jellyfin

The Jellyfin media server was added to Uptime Kuma.

The Jellyfin server currently uses:

```text
192.168.1.188
```

The Jellyfin service is available on:

```text
http://192.168.1.188:8096
```

Monitoring Jellyfin allows Uptime Kuma to continuously verify that the main media streaming service remains accessible.

This is particularly useful because Jellyfin is one of the primary self-hosted services running in the homelab.

---

# Part 11 – Monitoring Jellyseerr

Jellyseerr was added to the monitoring dashboard.

The service is hosted on the Jellyfin server and integrated with the wider automated media environment.

Monitoring Jellyseerr provides visibility into whether the media request platform remains available independently of Jellyfin itself.

This means that if Jellyfin remains operational but Jellyseerr fails, the individual service failure can be identified immediately from the Uptime Kuma dashboard.

---

# Part 12 – Monitoring the ARR Stack

The ARR stack was added to Uptime Kuma as a collection of individually monitored services.

The monitored applications include:

- Radarr
- Sonarr
- Prowlarr

Each application is monitored separately rather than treating the entire media stack as a single service.

This provides more granular monitoring.

For example:

```text
Jellyfin      UP
Jellyseerr    UP
Radarr        UP
Sonarr        DOWN
Prowlarr      UP
qBittorrent   UP
```

This would immediately identify Sonarr as the affected component without requiring manual troubleshooting across the entire media stack.

This is particularly valuable because the ARR stack contains several interconnected services.

---

# Part 13 – Monitoring qBittorrent

qBittorrent was also added to Uptime Kuma.

The qBittorrent web interface is currently available at:

```text
http://192.168.1.188:8080
```

Monitoring qBittorrent adds visibility into another component of the automated media platform.

The monitoring stack can now identify whether problems originate from:

- Jellyfin.
- Jellyseerr.
- Radarr.
- Sonarr.
- Prowlarr.
- qBittorrent.

This significantly improves troubleshooting compared with manually checking each application when an issue occurs.

---

# Part 14 – Centralized Monitoring Dashboard

After configuring the monitors, Uptime Kuma provided a centralized dashboard showing the status of the homelab services.

The dashboard displays information including:

- Current service status.
- Uptime percentage.
- Response time.
- Monitoring history.
- Recent events.
- Service availability.

The services were configured to be checked at regular intervals, with the dashboard showing successful availability checks.

At the completion of the project, the monitored infrastructure was reporting successfully.

The monitoring environment now provides a single location to check the operational state of the core homelab.

---

# Part 15 – Monitoring Strategy

The monitoring deployment creates several layers of visibility.

```text
Layer 1 – Network
│
└── BT Router

Layer 2 – Infrastructure
│
└── Raspberry Pi

Layer 3 – Network Services
│
└── Pi-hole

Layer 4 – Media Platform
│
├── Jellyfin
└── Jellyseerr

Layer 5 – Media Automation
│
├── Radarr
├── Sonarr
├── Prowlarr
└── qBittorrent
```

This layered approach makes troubleshooting easier.

If every service becomes unavailable simultaneously, the issue may exist at the network or server level.

If only one service becomes unavailable, troubleshooting can focus directly on that application or Docker container.

---

# Part 16 – Infrastructure as Code

The Docker Compose configuration was stored in the `WutangDev-SelfHosting` GitHub repository.

The deployment was staged using Git:

```bash
git add Uptime-kuma/
```

The configuration was committed using:

```bash
git commit -m "Deploy Uptime Kuma with Docker Compose"
```

The commit was then pushed to GitHub:

```bash
git push
```

The push completed successfully.

The repository now contains the Docker Compose configuration required to redeploy the Uptime Kuma container.

This continues the Infrastructure as Code approach introduced during the Pi-hole deployment.

---

# Infrastructure as Code Repository Structure

The self-hosting repository now contains deployment configurations for multiple services.

An example structure is:

```text
WutangDev-SelfHosting/
│
├── pihole/
│   └── docker-compose.yml
│
├── Uptime-kuma/
│   └── docker-compose.yml
│
├── dozzle/
├── grafana/
├── homepage/
└── prometheus/
```

As the 30-Day Self-Hosting Roadmap progresses, additional Docker services can be added to the repository.

The long-term goal is to maintain reusable deployment configurations that allow the self-hosted environment to be rebuilt from Git.

---

# Deployment Workflow

The deployment workflow used during this project was:

```text
Plan Service
      │
      ▼
Create Project Directory
      │
      ▼
Create docker-compose.yml
      │
      ▼
Validate Configuration
      │
      ▼
docker compose up -d
      │
      ▼
Verify Container Health
      │
      ▼
Access Web Interface
      │
      ▼
Configure Application
      │
      ▼
Configure Monitors
      │
      ▼
Test Monitoring
      │
      ▼
Commit Compose Configuration
      │
      ▼
Push to GitHub
      │
      ▼
Document Project
```

This workflow provides a repeatable deployment process that can be reused for future Docker projects.

---

# Troubleshooting Benefits

Deploying Uptime Kuma improves the troubleshooting capabilities of the homelab.

Previously, determining whether a service was available could require manually opening each web interface or connecting to individual hosts.

Uptime Kuma now provides immediate visibility into multiple components from a single dashboard.

For example, if Jellyfin becomes unavailable while the BT Router and Pi-hole remain online, the issue is more likely to be isolated to:

- The Jellyfin server.
- The Jellyfin Docker container.
- The Jellyfin application.
- The server's network connection.

If all monitored services become unavailable simultaneously, the issue may instead involve:

- The BT Router.
- The local network.
- The Raspberry Pi.
- The monitoring host itself.
- A wider infrastructure failure.

This provides a starting point for troubleshooting before connecting directly to individual systems.

---

# Skills Practised

This project provided practical experience with:

- Docker
- Docker Compose
- Linux
- Raspberry Pi administration
- Container deployment
- Container health verification
- Docker networking
- Docker volumes
- Persistent application storage
- Service monitoring
- Infrastructure monitoring
- HTTP monitoring
- Network availability monitoring
- Uptime monitoring
- Homelab observability
- Media server monitoring
- ARR stack monitoring
- Git
- GitHub
- Infrastructure as Code
- YAML
- Troubleshooting
- Service dependency awareness

---

# Key Learning Outcomes

## Centralized Monitoring

I learned how to deploy a centralized monitoring platform that provides visibility into multiple self-hosted applications and network services.

## Docker Compose

I continued developing practical Docker Compose skills by defining the Uptime Kuma container, networking, port mapping, restart policy, and persistent storage.

## Persistent Storage

I used a Docker named volume to ensure Uptime Kuma application data persists independently of the container.

## Monitoring Individual Services

I learned the benefit of monitoring individual components of an application stack rather than monitoring only the host machine.

## Layered Monitoring

I implemented monitoring across different infrastructure layers, including the network gateway, DNS service, media server, and individual applications.

## Infrastructure as Code

I stored the Uptime Kuma Docker Compose configuration in GitHub so the service deployment can be recreated in the future.

## Troubleshooting

I improved the troubleshooting design of the homelab by creating a dashboard that can quickly identify which services are operational and which may require investigation.

---

# Current Status

At the completion of this project:

- Uptime Kuma is deployed successfully.
- Uptime Kuma is running as a Docker container.
- The container is reporting a healthy status.
- Persistent storage is configured.
- The dashboard is accessible on TCP port `3001`.
- Pi-hole is monitored.
- The BT Router is monitored.
- Jellyfin is monitored.
- Jellyseerr is monitored.
- Radarr is monitored.
- Sonarr is monitored.
- Prowlarr is monitored.
- qBittorrent is monitored.
- Services are reporting availability through the Uptime Kuma dashboard.
- The Docker Compose configuration is stored in GitHub.
- The deployment forms part of the `WutangDev-SelfHosting` Infrastructure as Code repository.

---

# Future Improvements

Future improvements could include:

- Configure monitoring notifications.
- Add email or messaging alerts for service outages.
- Create an internal Uptime Kuma status page.
- Add additional Raspberry Pi services as they are deployed.
- Monitor Prometheus.
- Monitor Grafana.
- Monitor Homepage.
- Monitor Dozzle.
- Add Proxmox infrastructure monitoring.
- Add additional Docker hosts.
- Monitor Windows-based services.
- Configure HTTPS for internal services.
- Introduce reverse proxy monitoring.
- Test simulated service outages.
- Document service recovery procedures in the runbook repository.
- Integrate Uptime Kuma into the homelab Homepage dashboard.

---

# Conclusion

Project 37 successfully introduced centralized availability monitoring into the homelab by deploying Uptime Kuma using Docker Compose.

The Raspberry Pi now hosts both Pi-hole and Uptime Kuma, giving it an increasingly important role as a lightweight network infrastructure and monitoring server.

Uptime Kuma provides a central dashboard for monitoring the BT Router, Pi-hole, Jellyfin, Jellyseerr, the ARR stack, and qBittorrent.

By monitoring each service individually, the environment now has improved visibility and a faster starting point for troubleshooting service outages.

The Docker Compose configuration was committed and pushed to the `WutangDev-SelfHosting` GitHub repository, continuing the transition toward an Infrastructure as Code approach where self-hosted services can be documented, version controlled, and eventually rebuilt from Git.

This project establishes the monitoring foundation for the remainder of the 30-Day Docker and Self-Hosting Roadmap.