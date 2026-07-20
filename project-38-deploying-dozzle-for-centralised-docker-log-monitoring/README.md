# Project 38 – Deploying Dozzle for Centralised Docker Log Monitoring

## Project Overview

In this project, I deployed **Dozzle** as a lightweight, web-based Docker container monitoring and log viewing platform.

Dozzle was deployed on my Raspberry Pi using **Docker Compose** as part of my ongoing self-hosting and Infrastructure-as-Code project.

The Raspberry Pi is gradually being developed into a lightweight infrastructure and monitoring server running several containerised services.

At the completion of this project, the Raspberry Pi was running:

- Pi-hole
- Uptime Kuma
- Dozzle

Each service performs a different infrastructure role:

| Service | Purpose |
|---|---|
| Pi-hole | DNS filtering and network-level ad blocking |
| Uptime Kuma | Centralised service availability and uptime monitoring |
| Dozzle | Centralised Docker container log monitoring |

The Dozzle deployment provides a central web interface where I can view the status and logs of Docker containers running on the Raspberry Pi without manually running `docker logs` from the Linux terminal.

---

# Project Objectives

The objectives of this project were to:

- Deploy Dozzle using Docker Compose
- Continue building my Docker and Linux administration skills
- Implement centralised Docker container log monitoring
- Allow Docker logs to be viewed through a web interface
- Monitor the Pi-hole and Uptime Kuma containers
- Use the Docker socket to allow Dozzle to discover local containers
- Mount the Docker socket as read-only where possible
- Validate the Docker Compose configuration before deployment
- Verify that Dozzle could detect existing Docker containers
- Store the deployment configuration in Git
- Push the Infrastructure-as-Code configuration to GitHub
- Continue developing the Raspberry Pi as a lightweight infrastructure monitoring platform

---

# Environment

## Host

Raspberry Pi running Linux and Docker.

The Raspberry Pi currently acts as a lightweight infrastructure host within my homelab.

The Pi has a reserved IP address:

```text
192.168.1.111
```

The hostname is:

```text
pihole
```

---

# Existing Infrastructure

Before deploying Dozzle, the Raspberry Pi was already running two Docker workloads.

```text
Raspberry Pi
│
├── Docker
│   │
│   ├── Pi-hole
│   │   ├── DNS filtering
│   │   └── Network-level ad blocking
│   │
│   └── Uptime Kuma
│       └── Infrastructure and service availability monitoring
│
└── Git
    └── WutangDev-SelfHosting
```

Pi-hole had been deployed during Day 1 of the self-hosting project.

Uptime Kuma had been deployed during Day 2.

The objective for Day 3 was to introduce centralised Docker log monitoring using Dozzle.

---

# Architecture

The final architecture after deploying Dozzle became:

```text
                         Home Network
                              │
                              │
                    ┌─────────▼─────────┐
                    │     BT Router     │
                    │   192.168.1.254   │
                    └─────────┬─────────┘
                              │
                              │
                    ┌─────────▼─────────┐
                    │   Raspberry Pi    │
                    │   192.168.1.111   │
                    │                   │
                    │      Docker       │
                    │                   │
                    │  ┌─────────────┐  │
                    │  │   Pi-hole   │  │
                    │  │ DNS Filter  │  │
                    │  └─────────────┘  │
                    │                   │
                    │  ┌─────────────┐  │
                    │  │ Uptime Kuma │  │
                    │  │ Monitoring  │  │
                    │  └─────────────┘  │
                    │                   │
                    │  ┌─────────────┐  │
                    │  │   Dozzle    │  │
                    │  │ Docker Logs │  │
                    │  └──────┬──────┘  │
                    │         │         │
                    │         ▼         │
                    │ docker.sock       │
                    │                   │
                    └───────────────────┘
```

Dozzle communicates with the local Docker daemon through:

```text
/var/run/docker.sock
```

This allows Dozzle to discover containers running on the Docker host and display their logs.

---

# Infrastructure-as-Code Repository

The deployment configuration is stored in my dedicated self-hosting repository:

```text
WutangDev-SelfHosting
```

The repository contains Docker Compose configurations for services deployed as part of the self-hosting project.

The Dozzle configuration was created inside:

```text
WutangDev-SelfHosting/dozzle/
```

The deployment file is:

```text
docker-compose.yml
```

This means the service can be recreated in the future using the configuration stored in Git rather than relying on manually documented installation steps.

---

# Step 1 – Create the Dozzle Project Directory

I navigated to the Self-Hosting repository:

```bash
cd ~/github/WutangDev-SelfHosting
```

I created a dedicated directory for Dozzle:

```bash
mkdir -p dozzle
```

I then entered the directory:

```bash
cd dozzle
```

The Docker Compose file was created:

```bash
touch docker-compose.yml
```

The resulting structure was:

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
│   └── docker-compose.yml
│
└── .gitignore
```

---

# Step 2 – Create the Docker Compose Configuration

The following Docker Compose configuration was created:

```yaml
services:
  dozzle:
    image: amir20/dozzle:latest
    container_name: dozzle
    restart: unless-stopped

    ports:
      - "8080:8080"

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
```

---

# Docker Compose Configuration Breakdown

## Container Image

```yaml
image: amir20/dozzle:latest
```

This instructs Docker to use the Dozzle container image.

---

## Container Name

```yaml
container_name: dozzle
```

This assigns the container the name:

```text
dozzle
```

Using a predictable container name makes Docker administration easier.

For example:

```bash
docker logs dozzle
```

or:

```bash
docker restart dozzle
```

---

## Restart Policy

```yaml
restart: unless-stopped
```

This configures Docker to automatically restart Dozzle if:

- The container crashes
- Docker restarts
- The Raspberry Pi reboots

The container will remain stopped only if it is manually stopped.

This is useful for infrastructure services that should automatically recover following a host restart.

---

# Port Configuration

The following port mapping was configured:

```yaml
ports:
  - "8080:8080"
```

This maps:

```text
Raspberry Pi Port 8080
        │
        ▼
Dozzle Container Port 8080
```

Dozzle can therefore be accessed from another device on the local network using:

```text
http://192.168.1.111:8080
```

---

# Docker Socket Access

The most important part of the Dozzle deployment is the Docker socket mount.

```yaml
volumes:
  - /var/run/docker.sock:/var/run/docker.sock:ro
```

The Docker socket is located at:

```text
/var/run/docker.sock
```

This socket allows applications to communicate with the Docker daemon.

By mounting the socket inside the Dozzle container, Dozzle can discover containers running on the Raspberry Pi.

This allows Dozzle to display containers including:

```text
dozzle
pihole
uptime-kuma
```

The mount was configured using:

```text
:ro
```

which specifies a read-only bind mount from the container's perspective.

The Docker socket remains a security-sensitive resource, so access to the Dozzle web interface should still be limited to trusted networks.

---

# Step 3 – Validate the Docker Compose Configuration

Before deploying the container, I validated the Docker Compose configuration.

```bash
docker compose config
```

The validation completed successfully.

Docker expanded the configuration and confirmed:

- The Dozzle service was recognised
- The container image was valid
- Port 8080 was configured
- The restart policy was configured
- The Docker socket bind mount was recognised
- The Docker socket was configured as read-only
- A default Docker network would be created

The validated configuration showed the Docker socket as:

```text
type: bind
source: /var/run/docker.sock
target: /var/run/docker.sock
read_only: true
```

This confirmed that the Compose configuration was syntactically valid before deployment.

---

# Step 4 – Deploy Dozzle

The container was deployed using:

```bash
docker compose up -d
```

The `-d` option runs the container in detached mode.

Docker then:

1. Pulled the Dozzle image
2. Created the Docker network
3. Created the Dozzle container
4. Started the container

---

# Step 5 – Verify the Deployment

The deployment was verified using:

```bash
docker compose ps
```

The Dozzle container was confirmed as running.

The web interface was then accessed using:

```text
http://192.168.1.111:8080
```

The Dozzle dashboard loaded successfully.

---

# Step 6 – Verify Docker Container Discovery

Once Dozzle was running, it automatically discovered the Docker containers running on the Raspberry Pi.

The dashboard displayed three containers:

```text
dozzle
uptime-kuma
pihole
```

All three containers were shown as:

```text
running
```

This confirmed that the Docker socket integration was functioning correctly.

The final Docker environment was:

```text
Docker Host: pihole
│
├── dozzle
│   └── Centralised Docker log monitoring
│
├── uptime-kuma
│   └── Infrastructure availability monitoring
│
└── pihole
    └── DNS filtering
```

---

# Step 7 – Centralised Container Log Monitoring

Before deploying Dozzle, viewing container logs required using commands such as:

```bash
docker logs pihole
```

or:

```bash
docker logs uptime-kuma
```

Logs could also be followed in real time using:

```bash
docker logs -f pihole
```

With Dozzle deployed, container logs can now be accessed from a central web interface.

This provides a simpler method for:

- Troubleshooting container problems
- Viewing application startup logs
- Monitoring container activity
- Investigating container crashes
- Viewing multiple container logs
- Troubleshooting Docker services without maintaining a continuous SSH session

---

# Step 8 – Raspberry Pi Resource Monitoring

Before deploying Dozzle, I had experienced an SSH issue with the Raspberry Pi.

Attempts to connect returned:

```text
fork failed: Resource temporarily unavailable
```

The SSH connection was then closed.

Connecting directly using the Raspberry Pi IP address also resulted in:

```text
client_loop: send disconnect: Connection reset
```

A power cycle restored SSH access.

After reconnecting, I investigated the Raspberry Pi's resource usage.

---

# Memory Check

I ran:

```bash
free -h
```

The Raspberry Pi reported approximately:

```text
Total Memory:      905 MiB
Used Memory:       373 MiB
Free Memory:        94 MiB
Buff/Cache:        504 MiB
Available Memory:  532 MiB
Swap:              904 MiB
Swap Used:           0 B
```

This showed that the Raspberry Pi still had more than 500 MiB of available memory after reboot.

Swap was also available but unused.

The SSH problem therefore did not appear to be caused by a persistent lack of available RAM.

---

# Docker Resource Check

I also ran:

```bash
docker stats --no-stream
```

The containers showed very low CPU utilisation.

However, Docker reported:

```text
0B / 0B
```

for container memory statistics.

The same behaviour was visible in Dozzle, which showed the Raspberry Pi's total memory but displayed:

```text
0 Bytes
```

for individual container memory consumption.

This appears to be a container memory-accounting limitation or configuration issue on the Raspberry Pi rather than the containers genuinely consuming zero memory.

CPU statistics continued to function correctly.

---

# Process Count Check

To investigate whether the earlier SSH issue could have been related to process exhaustion, I checked the number of running processes:

```bash
ps -e --no-headers | wc -l
```

The Raspberry Pi reported approximately:

```text
183
```

At the time of testing, this did not indicate an obvious process explosion.

Because the reboot cleared the issue before diagnostic data could be captured, the exact cause of the earlier SSH failure remains unconfirmed.

Potential causes could include temporary:

- Process exhaustion
- PID limits
- Resource limits
- Kernel-level resource exhaustion
- Service instability

If the issue occurs again, further diagnostics should be collected before rebooting the Raspberry Pi.

Useful commands include:

```bash
free -h
```

```bash
uptime
```

```bash
ps -e --no-headers | wc -l
```

```bash
docker stats --no-stream
```

```bash
systemctl status ssh
```

```bash
journalctl -u ssh
```

```bash
dmesg | tail -100
```

This would help identify the root cause rather than relying on a reboot to recover the host.

---

# Step 9 – Store the Deployment in Git

Once Dozzle was successfully deployed and tested, I returned to the root of the Self-Hosting repository.

```bash
cd ~/github/WutangDev-SelfHosting
```

I checked the repository status:

```bash
git status
```

The new Dozzle directory appeared as an untracked directory.

The configuration was staged:

```bash
git add dozzle/
```

The deployment was committed:

```bash
git commit -m "Deploy Dozzle for centralised Docker log monitoring"
```

The changes were then pushed to GitHub:

```bash
git push
```

The push completed successfully.

This means the Dozzle deployment configuration is now version controlled and stored remotely.

---

# Infrastructure-as-Code Workflow

The workflow used for this project was:

```text
Create Service Directory
        │
        ▼
Create docker-compose.yml
        │
        ▼
Write Docker Compose Configuration
        │
        ▼
docker compose config
        │
        ▼
Validate Configuration
        │
        ▼
docker compose up -d
        │
        ▼
Verify Container
        │
        ▼
Test Web Interface
        │
        ▼
Verify Docker Log Access
        │
        ▼
git add
        │
        ▼
git commit
        │
        ▼
git push
        │
        ▼
Configuration Stored in GitHub
```

---

# Final Infrastructure

After completing Day 3, the Raspberry Pi runs three core infrastructure services.

```text
Raspberry Pi – 192.168.1.111
│
├── Pi-hole
│   │
│   ├── DNS filtering
│   ├── Network-level ad blocking
│   └── DNS query visibility
│
├── Uptime Kuma
│   │
│   ├── Service availability monitoring
│   ├── BT Router monitoring
│   ├── Pi-hole monitoring
│   ├── Jellyfin monitoring
│   ├── Jellyseerr monitoring
│   └── ARR stack monitoring
│
└── Dozzle
    │
    ├── Docker container discovery
    ├── Centralised container logs
    ├── Real-time log viewing
    └── Container troubleshooting
```

---

# Monitoring Architecture

The combination of Uptime Kuma and Dozzle provides two different layers of monitoring.

```text
                 Homelab Infrastructure
                         │
            ┌────────────┴────────────┐
            │                         │
            ▼                         ▼
       Uptime Kuma                  Dozzle
            │                         │
            │                         │
     Is the service up?       What is the container
     Is it responding?        actually doing?
     How long has it          What errors are in
     been available?          the logs?
            │                         │
            └────────────┬────────────┘
                         │
                         ▼
              Infrastructure Visibility
```

Uptime Kuma provides service-level monitoring.

Dozzle provides container-level log visibility.

Together they improve my ability to detect and troubleshoot issues within the homelab.

---

# Skills Practised

This project provided practical experience with:

- Linux administration
- Raspberry Pi administration
- Docker
- Docker Compose
- Container deployment
- Docker socket integration
- Bind mounts
- Read-only Docker volume mounts
- Container networking
- Port mapping
- Docker logging
- Centralised log monitoring
- Infrastructure monitoring
- Linux resource troubleshooting
- Memory monitoring
- Process monitoring
- SSH troubleshooting
- Git
- GitHub
- Infrastructure as Code
- Configuration validation
- Version-controlled infrastructure

---

# Key Commands Used

## Navigate to Repository

```bash
cd ~/github/WutangDev-SelfHosting
```

## Create Project Directory

```bash
mkdir -p dozzle
```

## Enter Directory

```bash
cd dozzle
```

## Create Compose File

```bash
touch docker-compose.yml
```

## Validate Configuration

```bash
docker compose config
```

## Deploy Dozzle

```bash
docker compose up -d
```

## Check Container Status

```bash
docker compose ps
```

## Check Docker Resources

```bash
docker stats --no-stream
```

## Check System Memory

```bash
free -h
```

## Check Process Count

```bash
ps -e --no-headers | wc -l
```

## Stage Configuration

```bash
git add dozzle/
```

## Commit Configuration

```bash
git commit -m "Deploy Dozzle for centralised Docker log monitoring"
```

## Push Configuration

```bash
git push
```

---

# Key Learning Outcomes

## 1. Docker Logs Can Be Centralised

Instead of connecting to the Raspberry Pi through SSH every time I need to investigate a container, Dozzle provides a central interface for viewing Docker logs.

---

## 2. The Docker Socket Provides Powerful Container Visibility

Mounting:

```text
/var/run/docker.sock
```

allows Dozzle to communicate with the Docker daemon and automatically discover local containers.

However, access to the Docker socket is security-sensitive and should only be provided to trusted containers.

---

## 3. Docker Compose Validation Should Be Part of the Deployment Workflow

Running:

```bash
docker compose config
```

before deployment provides a quick way to identify configuration errors before creating containers.

This has become part of my standard Docker deployment workflow.

---

## 4. Monitoring Requires Multiple Layers

Uptime Kuma and Dozzle solve different monitoring problems.

Uptime Kuma answers:

```text
Is the service available?
```

Dozzle answers:

```text
What is happening inside the container?
```

Using both provides better visibility than relying on either tool individually.

---

## 5. Resource Monitoring Is Important on Small Hosts

The Raspberry Pi has approximately 1 GB of RAM.

Although Pi-hole, Uptime Kuma and Dozzle are relatively lightweight services, resource utilisation needs to be considered as additional containers are deployed.

The earlier SSH issue demonstrated why monitoring:

- RAM
- Swap
- CPU
- Processes
- Container resources

is important when using resource-constrained hardware.

---

## 6. Infrastructure as Code Improves Recoverability

The Dozzle configuration is stored in GitHub.

If the Raspberry Pi needs to be rebuilt, the configuration can be cloned and redeployed using:

```bash
docker compose up -d
```

This reduces reliance on manually remembering how each service was originally configured.

---

# Project Outcome

Dozzle was successfully deployed on the Raspberry Pi using Docker Compose.

The deployment was validated before launch, and Dozzle successfully discovered all three containers running on the host:

```text
dozzle
pihole
uptime-kuma
```

The Raspberry Pi now provides three complementary infrastructure services:

```text
Pi-hole
    ↓
DNS Filtering

Uptime Kuma
    ↓
Service Availability Monitoring

Dozzle
    ↓
Docker Log Monitoring
```

The Docker Compose configuration was committed and pushed to the `WutangDev-SelfHosting` GitHub repository, providing a version-controlled Infrastructure-as-Code definition for the deployment.

This project continues the development of the Raspberry Pi from a single-purpose Pi-hole server into a lightweight, containerised infrastructure and monitoring platform.

---

# Project Status

```text
[✓] Dozzle directory created
[✓] Docker Compose configuration created
[✓] Docker Compose configuration validated
[✓] Docker socket mounted
[✓] Docker socket configured read-only
[✓] Dozzle container deployed
[✓] Web interface accessible
[✓] Pi-hole container discovered
[✓] Uptime Kuma container discovered
[✓] Dozzle container discovered
[✓] Centralised Docker log monitoring operational
[✓] Raspberry Pi resources checked
[✓] Configuration committed to Git
[✓] Configuration pushed to GitHub
[✓] Infrastructure-as-Code deployment complete
```

---

# Next Steps

The next stage of the self-hosting roadmap will continue expanding the Raspberry Pi monitoring platform.

Planned services include:

```text
Day 4
Prometheus + Grafana
        │
        ▼
Metrics Collection and Visualisation

Day 5
Homepage
        │
        ▼
Centralised Homelab Service Dashboard
```

The longer-term monitoring architecture will therefore develop into:

```text
Pi-hole
    │
    └── DNS and Network Filtering

Uptime Kuma
    │
    └── Availability Monitoring

Dozzle
    │
    └── Container Log Monitoring

Prometheus
    │
    └── Metrics Collection

Grafana
    │
    └── Metrics Visualisation

Homepage
    │
    └── Centralised Service Access
```

This creates the foundation for a lightweight observability and infrastructure management platform running entirely within the homelab.
