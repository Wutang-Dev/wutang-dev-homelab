

# Project 39 – Building a Physical OPNsense Lab Network with Proxmox, Ubuntu, Docker and Tailscale

## Project Overview

In this project, I rebuilt the core networking and compute foundation of my homelab by deploying **OPNsense** on dedicated Protectli hardware.

The objective was to create a separate lab network for infrastructure learning while keeping my production home network isolated and stable.

The final environment includes:

- A Protectli appliance running OPNsense
- A dedicated lab subnet
- A repurposed mini switch acting as the lab switch
- A Ryzen system running Proxmox VE
- An HP Mini running Ubuntu Desktop as a Linux and Docker server
- A Toshiba Ubuntu laptop acting as the lab administration workstation
- Tailscale for secure administration across network boundaries
- Homepage links for centralised service access

This project moved OPNsense away from a virtual machine and onto dedicated physical hardware.

The result is a more realistic lab environment for:

- Networking
- Linux administration
- Docker
- Proxmox
- Windows Server
- Active Directory
- Group Policy
- DNS
- DHCP
- Microsoft Entra ID
- Intune
- Hybrid identity
- Infrastructure troubleshooting

---

# Project Objectives

The objectives of this project were to:

- Install OPNsense on dedicated Protectli hardware
- Create a separate lab IP range
- Keep the production and lab networks isolated
- Repurpose an existing mini switch as the lab switch
- Configure DHCP, DNS, NAT and routing
- Validate internet access through OPNsense
- Create an OPNsense configuration backup
- Repurpose the Ryzen system as a Proxmox host
- Configure Proxmox repositories and storage
- Repurpose the HP Mini as an Ubuntu Linux server
- Install and validate SSH
- Install and validate Tailscale
- Install Docker Engine and Docker Compose
- Enable secure administration from trusted production devices
- Update Homepage to point to the new Proxmox environment
- Document the project without exposing sensitive information

---

# Environment

## Production Network

The production network continues to host existing services including:

- Jellyfin
- Jellyseerr
- Radarr
- Sonarr
- Prowlarr
- qBittorrent
- Pi-hole
- Uptime Kuma
- Grafana
- Dozzle
- Homepage

The production network uses a private address range similar to:

```text
192.168.x.0/24
```

---

## Lab Network

The new lab network uses a separate private address range similar to:

```text
10.x.x.0/24
```

The lab network is routed through OPNsense.

Exact IP addresses, MAC addresses, Tailscale addresses, passwords, API keys, switch port mappings and configuration backups are intentionally excluded from this public documentation.

---

# Hardware Used

## Protectli Appliance

The Protectli device became the dedicated router and firewall.

Its role includes:

- WAN connectivity
- LAN routing
- DHCP
- DNS forwarding
- NAT
- Firewalling
- Lab network isolation

---

## Ryzen Lab

The Ryzen system became the primary virtualization host.

Resources include:

- 12 logical CPU threads
- Approximately 16 GB RAM
- 512 GB NVMe SSD
- Secondary 250 GB NVMe SSD
- Wired Ethernet connectivity

---

## HP Mini

The HP Mini became the dedicated physical Linux and Docker server.

Its role includes:

- Ubuntu administration
- Linux labs
- Docker Engine
- Docker Compose
- SSH
- Tailscale
- Git
- Future self-hosted services

---

## Toshiba Laptop

The Toshiba Ubuntu laptop became the dedicated lab administration node.

Its role includes:

- OPNsense administration
- Proxmox administration
- SSH access
- Tailscale administration
- GitHub documentation
- Visual Studio Code
- Network troubleshooting

---

# Existing Infrastructure

Before this project, OPNsense had been tested virtually inside Proxmox.

The earlier design created a dependency between the firewall and the hypervisor.

```text
Production Network
        │
        ▼
Virtual OPNsense
        │
        ▼
Lab Virtual Machines
```

If the Proxmox host was unavailable, the virtual firewall was also unavailable.

The new design removes that dependency by moving OPNsense onto dedicated physical hardware.

---

# Final Architecture

The final architecture became:

```text
                              Internet
                                  │
                                  ▼
                         ┌────────────────┐
                         │   ISP Router   │
                         │ Production LAN │
                         └───────┬────────┘
                                 │
                                 │ WAN
                                 ▼
                         ┌────────────────┐
                         │   Protectli    │
                         │    OPNsense    │
                         │                │
                         │ Routing        │
                         │ DHCP           │
                         │ DNS            │
                         │ NAT            │
                         │ Firewalling    │
                         └───────┬────────┘
                                 │
                                 │ LAN
                                 ▼
                         ┌────────────────┐
                         │   Lab Switch   │
                         └───────┬────────┘
                                 │
              ┌──────────────────┼──────────────────┐
              │                  │                  │
              ▼                  ▼                  ▼
     ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
     │ Toshiba Admin  │ │ Ryzen Proxmox  │ │ HP Mini Ubuntu │
     │ Ubuntu Desktop │ │ Hypervisor     │ │ Docker Server  │
     └────────────────┘ └────────────────┘ └────────────────┘
```

Trusted production devices can still administer selected lab systems using Tailscale.

```text
Production Device
        │
        ▼
    Tailscale
        │
        ▼
Proxmox / Ubuntu Server
```

---

# Step 1 – Prepare the Ventoy Installation USB

I used an existing Ventoy USB drive containing several operating system images.

The USB contained images for:

- OPNsense
- Proxmox VE
- Ubuntu Desktop
- Ubuntu Server
- Windows Server
- Windows client operating systems

The Protectli, Ryzen Lab and HP Mini were all booted using the same Ventoy drive.

This made it possible to reuse one installation device throughout the project.

---

# Step 2 – Install OPNsense on the Protectli

The Protectli was booted from the Ventoy USB.

The OPNsense installation image was selected.

OPNsense was installed onto the internal SSD.

During installation, I initially experienced difficulty selecting the preferred storage and filesystem options.

I chose UFS rather than ZFS because:

- The Protectli had limited memory
- The internal SSD was small
- The firewall did not require advanced ZFS features
- UFS provided a simpler installation path

---

# Step 3 – Recover the OPNsense Administrator Password

After installation, the expected administrator password was not accepted.

I used the OPNsense console recovery options to reset the root password.

This restored access to:

- The OPNsense console
- The OPNsense web interface
- Interface configuration
- System settings
- Backup functions

This demonstrated the importance of understanding recovery options before making further configuration changes.

---

# Step 4 – Identify the Correct Physical Interfaces

The Protectli appliance contained several Intel Ethernet interfaces.

OPNsense displayed these as interfaces such as:

```text
igb0
igb1
igb2
igb3
```

The physical port labels did not initially match the interface mapping I expected.

---

# Initial Symptoms

The initial symptoms included:

- A physical link light on the WAN cable
- No DHCP address on the OPNsense WAN interface
- The LAN interface not responding on the expected port
- The administration laptop not receiving a lab IP address

---

# Automatic Interface Detection

I used OPNsense automatic interface detection.

The process involved:

1. Disconnecting unnecessary Ethernet cables
2. Starting automatic interface assignment
3. Connecting the WAN cable when prompted
4. Allowing OPNsense to detect the active interface
5. Repeating the process for the LAN interface
6. Confirming the final assignment

The final working interface mapping was:

```text
WAN: igb0
LAN: igb1
```

After correcting the assignments:

- WAN received an address from the production router
- LAN became reachable
- DHCP began working
- Internet access through OPNsense became available

---

# Step 5 – Configure the Lab Network

The OPNsense LAN interface was configured with a dedicated private subnet.

The DHCP service was configured to assign addresses to lab devices.

Lab systems received:

- A private lab IP address
- OPNsense as the default gateway
- DNS through OPNsense
- Internet access through NAT

---

# Step 6 – Validate DHCP, Routing, DNS and NAT

The Toshiba Ubuntu laptop was connected directly to the OPNsense LAN during testing.

I checked its network configuration:

```bash
ip addr
```

I checked the routing table:

```bash
ip route
```

I tested the OPNsense gateway:

```bash
ping -c 4 <lab-gateway>
```

I tested external IP connectivity:

```bash
ping -c 4 8.8.8.8
```

I tested DNS resolution:

```bash
ping -c 4 google.com
```

The tests confirmed:

- DHCP was working
- The Toshiba received a lab IP address
- The default gateway was correct
- OPNsense routing was working
- NAT was working
- DNS resolution was working
- Internet access was working

I also opened a public website to confirm browser connectivity.

---

# Step 7 – Complete the OPNsense Setup Wizard

The OPNsense web interface was opened from the Toshiba administration laptop.

The setup wizard was completed using:

- A custom hostname
- An internal domain
- UK timezone settings
- DHCP on the WAN interface
- A dedicated private LAN subnet
- DHCP for lab clients
- OPNsense DNS services

After completing the wizard, the OPNsense dashboard loaded successfully.

---

# Step 8 – Create an OPNsense Configuration Backup

After confirming the firewall was working, I created a configuration backup.

The backup included:

- Interface assignments
- LAN configuration
- DHCP configuration
- Hostname and domain settings
- Firewall settings
- System settings

The configuration was exported as XML and stored on an external 1 TB drive.

The backup was not added to GitHub because firewall configuration files can contain sensitive information.

---

# Step 9 – Rewire the Mini Switch

The mini switch had previously been connected directly to the production network.

I rewired it so that it became the dedicated lab switch behind OPNsense.

---

# Previous Topology

```text
ISP Router
    │
    ▼
Mini Switch
    │
    ▼
Devices
```

---

# New Topology

```text
ISP Router
    │
    ▼
Protectli WAN
    │
    ▼
OPNsense
    │
    ▼
Protectli LAN
    │
    ▼
Mini Switch
    │
    ▼
Lab Devices
```

Only the HP Mini was connected to the switch before the migration, and it was scheduled to be rebuilt.

This reduced the risk of disrupting important services.

---

# Step 10 – Validate the Rewired Switch

The Toshiba was connected to the rewired lab switch.

The laptop received a new lab address from OPNsense.

The route table showed OPNsense as the default gateway.

The final traffic path was:

```text
Toshiba
    │
    ▼
Lab Switch
    │
    ▼
Protectli LAN
    │
    ▼
OPNsense
    │
    ▼
Protectli WAN
    │
    ▼
Production Router
    │
    ▼
Internet
```

This confirmed that the switch migration was successful.

---

# Step 11 – Configure the Toshiba as the Lab Administration Node

The Toshiba laptop was renamed to reflect its new purpose.

The laptop now acts as the main lab administration workstation.

It is used for:

- OPNsense web administration
- Proxmox web administration
- SSH sessions
- Tailscale administration
- GitHub documentation
- Visual Studio Code
- Network troubleshooting
- Docker testing

The Toshiba can access the lab directly because it is connected to the isolated lab network.

---

# Step 12 – Install Proxmox on Ryzen Lab

The Ryzen system had no important data and had recently been used to test Ventoy and Ubuntu.

The machine was therefore repurposed as the main virtualization server.

The system was booted from Ventoy.

The Proxmox VE ISO was selected.

Proxmox was installed onto the 512 GB NVMe drive.

The network configuration included:

- A reserved management address on the lab subnet
- OPNsense as the gateway
- OPNsense as the DNS server
- A descriptive hostname
- Wired Ethernet as the management interface

---

# Step 13 – Validate the Proxmox Installation

After installation, the Proxmox web interface was opened from the Toshiba.

The host correctly detected:

```text
12 logical CPU threads
Approximately 16 GB RAM
512 GB NVMe SSD
250 GB secondary NVMe SSD
Linux bridge vmbr0
```

The Proxmox web interface was reachable through the local lab network.

---

# Step 14 – Configure Proxmox Repositories

The default Proxmox enterprise repositories generated update errors because the lab does not have a paid subscription.

I disabled:

```text
Proxmox Enterprise Repository
Ceph Enterprise Repository
```

I left the Debian repositories enabled.

I added:

```text
Proxmox No-Subscription Repository
```

The package database then refreshed successfully.

I installed all available updates.

A kernel update was installed, so I rebooted the Proxmox host.

After rebooting, Proxmox reported:

```text
No updates available
```

---

# Step 15 – Configure the Secondary Proxmox Storage

The main 512 GB NVMe contained:

- Proxmox
- The local storage
- The default LVM-Thin storage

The secondary 250 GB NVMe contained an old test partition from a previous Windows or Ubuntu installation.

The old data was no longer required.

Before wiping the drive, I confirmed:

- The 250 GB disk was the correct device
- The 512 GB Proxmox system disk was not selected

I then:

1. Wiped the old partitions
2. Created a new LVM-Thin pool
3. Named the pool `vm-storage`
4. Added it to Proxmox

The final storage layout became:

```text
local
    │
    ├── ISO images
    ├── Templates
    └── Backups

local-lvm
    │
    └── VM disks on the 512 GB NVMe

vm-storage
    │
    └── Additional VM disks on the 250 GB NVMe
```

The storage can be used by both Windows and Linux virtual machines.

The lab will mainly use temporary VMs that are created, tested, documented and deleted.

---

# Step 16 – Install Tailscale on Proxmox

The production and lab networks were intentionally separated.

This meant the Jellyfin PC could not directly reach the private lab addresses.

Instead of removing the isolation, I installed Tailscale on the Proxmox host.

Tailscale was installed directly on the Proxmox node.

DNS acceptance was disabled to reduce the risk of Tailscale modifying Proxmox-managed DNS behaviour.

Tailscale SSH was then enabled.

---

# Step 17 – Validate Proxmox Access from the Production Network

From the production Jellyfin PC, I successfully:

- Opened the Proxmox web interface using Tailscale
- Connected to the Proxmox shell using Tailscale SSH
- Verified the new Proxmox node in the Tailscale admin console
- Removed old Tailscale entries from previous Proxmox builds

The management design became:

```text
Local Administration
        │
        ▼
Toshiba
        │
        ▼
Proxmox Local Address
```

```text
Trusted Remote Administration
        │
        ▼
Jellyfin PC
        │
        ▼
Tailscale
        │
        ▼
Proxmox
```

This preserved network isolation while maintaining manageability.

---

# Step 18 – Update Homepage

The Homepage dashboard contained a shortcut to the old Proxmox environment.

I updated the `services.yaml` file.

The sanitized configuration was similar to:

```yaml
- Infrastructure & Monitoring:
    - Proxmox:
        icon: proxmox.png
        href: https://proxmox-tailscale-hostname:8006
        description: Ryzen Lab Proxmox Machine
```

After updating the configuration and refreshing Homepage, the Proxmox tile successfully opened the new Ryzen Proxmox host.

---

# Step 19 – Install Ubuntu on the HP Mini

The HP Mini was repurposed as the dedicated physical Linux and Docker server.

Ubuntu Desktop was selected instead of Ubuntu Server.

This provides:

- A local graphical interface
- Terminal-based Linux administration
- Easier troubleshooting
- Docker support
- SSH access
- A suitable Linux learning environment

---

# Secure Boot Issue

When the HP Mini attempted to boot the Ventoy USB, it displayed a Secure Boot verification error.

I entered the HP BIOS.

The Secure Boot configuration showed that Ventoy needed to be trusted.

The Ventoy security key was enrolled in the UEFI environment.

After rebooting, the HP Mini successfully loaded the Ventoy menu.

This allowed the Ubuntu ISO to boot.

---

# Step 20 – Complete the Ubuntu Installation

Ubuntu was installed using:

```text
Erase disk and install Ubuntu
```

The HP Mini was assigned a descriptive hostname:

```text
wutanglan-ubuntu-server
```

The system was connected to the lab switch.

OPNsense provided:

- A lab IP address
- Default gateway
- DNS
- Internet access

---

# Step 21 – Install SSH on the HP Mini

OpenSSH Server was installed and enabled.

The SSH service was configured to start automatically.

The HP Mini could then be administered remotely without requiring a monitor and keyboard.

---

# Step 22 – Install Tailscale on the HP Mini

Tailscale was installed on the HP Mini.

The server was added to the existing tailnet.

Tailscale SSH was enabled.

The HP Mini appeared in the Tailscale admin console as an active Linux device.

---

# Step 23 – Validate SSH from the Jellyfin PC

From the Jellyfin PC, I connected to the HP Mini using:

```bash
ssh ravi@wutanglan-ubuntu-server
```

The SSH session confirmed:

- Ubuntu was running correctly
- Tailscale connectivity was working
- Tailscale SSH was working
- The HP Mini could be administered from the production network
- The lab network remained isolated

---

# Step 24 – Update the HP Mini

The HP Mini reported that updates were available.

I updated the package list:

```bash
sudo apt update
```

I installed the updates:

```bash
sudo apt full-upgrade -y
```

The system required a reboot after the update.

I rebooted the HP Mini and reconnected using SSH.

---

# Step 25 – Install Supporting Packages

I installed the packages required for Docker and Git-based workflows:

```bash
sudo apt install ca-certificates curl git -y
```

The installation was validated using:

```bash
curl --version
```

```bash
git --version
```

---

# Step 26 – Install Docker Engine and Docker Compose

Docker Engine and Docker Compose were installed.

Docker was enabled to start automatically:

```bash
sudo systemctl enable --now docker
```

The user was added to the Docker group so Docker commands could run without repeatedly using `sudo`.

---

# Step 27 – Validate Docker

Docker was tested using:

```bash
docker run hello-world
```

The container downloaded successfully and displayed:

```text
Hello from Docker!
```

This confirmed:

- Docker Engine was installed
- Docker Hub connectivity was working
- Container image downloads were working
- Container creation was working
- Container execution was working
- Container output was working

---

# Step 28 – Validate Docker Services

I checked the Docker version:

```bash
docker --version
```

I checked the Docker Compose version:

```bash
docker compose version
```

I confirmed Docker was enabled:

```bash
systemctl is-enabled docker
```

The result was:

```text
enabled
```

I confirmed Docker was active:

```bash
systemctl is-active docker
```

The result was:

```text
active
```

---

# Step 29 – Clone the Homelab Repository

The public homelab repository was cloned onto the HP Mini.

I created a GitHub directory:

```bash
mkdir -p ~/github
```

I entered the directory:

```bash
cd ~/github
```

I cloned the repository:

```bash
git clone https://github.com/Wutang-Dev/wutang-dev-homelab.git
```

I entered the repository:

```bash
cd wutang-dev-homelab
```

The repository will be used to document the Protectli build and the new architecture.

Sensitive infrastructure information will be stored separately in private documentation.

---

# Public and Private Documentation Strategy

The public repository will include:

- Architecture
- Implementation steps
- Troubleshooting
- Skills demonstrated
- Lessons learned
- Sanitized configuration examples
- Project outcomes

The public repository will not include:

- Exact IP addresses
- Exact Tailscale addresses
- MAC addresses
- Passwords
- API keys
- SSH private keys
- OPNsense XML backups
- Switch port assignments
- Cable colour mappings
- Private service inventories

A future private repository can include:

```text
IP Address Plan
Device Register
Switch Port Map
Cable Colour Map
Service Port Register
Change Log
Backup Locations
```

---

# Final Lab Roles

## Protectli

```text
Role: Physical Router and Firewall
Operating System: OPNsense
```

Responsibilities:

- Routing
- DHCP
- DNS
- NAT
- Firewalling
- Lab network isolation

---

## Ryzen Lab

```text
Role: Hypervisor
Operating System: Proxmox VE
```

Responsibilities:

- Windows Server VMs
- Windows client VMs
- Linux VMs
- Active Directory labs
- Hybrid identity labs
- Temporary build-and-destroy environments

---

## HP Mini

```text
Role: Physical Linux and Docker Server
Operating System: Ubuntu
```

Responsibilities:

- Linux administration
- Docker labs
- Docker Compose
- SSH
- Git
- Automation
- Future self-hosted services

---

## Toshiba Laptop

```text
Role: Lab Administration Node
Operating System: Ubuntu Desktop
```

Responsibilities:

- OPNsense administration
- Proxmox administration
- SSH access
- Git documentation
- Tailscale management
- Network troubleshooting

---

## Jellyfin PC

```text
Role: Production Media Server and Trusted Management Device
Operating System: Windows
```

Responsibilities:

- Jellyfin
- Jellyseerr
- ARR services
- Homepage
- Remote Proxmox access
- Remote SSH access through Tailscale

---

# Security Design

The production and lab networks remain separated.

```text
Production Network
        │
        │ No direct access to private lab addresses
        │
        ▼
Trusted Devices
        │
        ▼
Tailscale
        │
        ▼
Selected Lab Systems
```

The security approach includes:

- Separate private subnets
- OPNsense firewalling
- NAT between the lab and internet
- No direct lab management exposure
- Tailscale for trusted administration
- Sensitive details excluded from public GitHub documentation
- Configuration backups stored outside the public repository

---

# Troubleshooting Summary

## OPNsense WAN Did Not Receive an Address

### Cause

The physical WAN interface was assigned incorrectly.

### Resolution

Automatic interface detection was used to identify and assign the correct WAN and LAN ports.

---

## OPNsense Password Was Not Accepted

### Cause

The expected administrator password was not available after installation.

### Resolution

The OPNsense console recovery function was used to reset the root password.

---

## Ventoy Failed Secure Boot Verification

### Cause

The HP Mini did not trust the Ventoy UEFI bootloader.

### Resolution

The Ventoy security key was enrolled in the HP UEFI environment.

The HP Mini was then rebooted and successfully loaded Ventoy.

---

## Proxmox Package Update Error

### Cause

The enterprise repositories were enabled without a paid subscription.

### Resolution

The enterprise repositories were disabled.

The no-subscription repository was enabled.

The package database then refreshed successfully.

---

## Production PC Could Not Reach Lab Addresses

### Cause

The production and lab networks were intentionally isolated.

### Resolution

Tailscale was installed on trusted endpoints.

Tailscale SSH was enabled on Proxmox and the HP Mini.

---

## Old NVMe Partition Detected

### Cause

The secondary NVMe contained an old Windows or Ubuntu test installation.

### Resolution

The correct disk was verified.

The old partition was wiped.

A new LVM-Thin pool was created.

---

# Skills Practised

This project provided practical experience with:

- Physical network design
- Router deployment
- Firewall deployment
- OPNsense
- WAN and LAN interface mapping
- DHCP
- DNS
- NAT
- Private subnetting
- Network isolation
- Switch rewiring
- Secure Boot troubleshooting
- UEFI key enrollment
- Proxmox installation
- Proxmox repository management
- Linux bridges
- LVM-Thin storage
- Kernel updates
- Ubuntu installation
- Linux administration
- OpenSSH
- Tailscale
- Tailscale SSH
- Docker Engine
- Docker Compose
- Git
- GitHub
- Remote administration
- Cross-network management
- Infrastructure documentation
- Security-conscious documentation

---

# Key Commands Used

## Check Network Addresses

```bash
ip addr
```

## Check Routing

```bash
ip route
```

## Test Gateway Connectivity

```bash
ping -c 4 <lab-gateway>
```

## Test External Connectivity

```bash
ping -c 4 8.8.8.8
```

## Test DNS

```bash
ping -c 4 google.com
```

## Update Ubuntu

```bash
sudo apt update
```

```bash
sudo apt full-upgrade -y
```

## Install Supporting Packages

```bash
sudo apt install ca-certificates curl git -y
```

## Enable Docker

```bash
sudo systemctl enable --now docker
```

## Test Docker

```bash
docker run hello-world
```

## Check Docker Version

```bash
docker --version
```

## Check Docker Compose

```bash
docker compose version
```

## Check Docker Startup State

```bash
systemctl is-enabled docker
```

## Check Docker Service State

```bash
systemctl is-active docker
```

## Clone Homelab Repository

```bash
mkdir -p ~/github
```

```bash
cd ~/github
```

```bash
git clone https://github.com/Wutang-Dev/wutang-dev-homelab.git
```

```bash
cd wutang-dev-homelab
```

---

# Key Learning Outcomes

## 1. Dedicated Hardware Removes Firewall Dependencies

Running OPNsense on dedicated hardware means the firewall no longer depends on Proxmox.

The lab network can continue functioning even when the virtualization server is rebooted or rebuilt.

---

## 2. Physical Interface Labels Must Be Validated

The expected physical port order did not match the OPNsense interface mapping.

Automatic interface detection was the most reliable method for identifying the correct WAN and LAN interfaces.

---

## 3. Network Isolation Does Not Have to Reduce Manageability

The production and lab networks remain separate.

Tailscale provides secure administration without exposing private lab addresses or removing the firewall boundary.

---

## 4. Backups Should Be Created After Validation

The OPNsense configuration was backed up immediately after DHCP, DNS, NAT and internet access were validated.

This created a known-good recovery point.

---

## 5. Build-and-Destroy Labs Do Not Require Perfect Storage Separation

The Proxmox system and VM storage share the main 512 GB NVMe.

The secondary 250 GB NVMe provides additional VM storage.

Because VMs will be created and deleted frequently, the current storage layout is suitable for the lab.

---

## 6. Secure Boot Can Be Resolved Without Disabling All UEFI Security

The HP Mini required the Ventoy key to be enrolled.

This allowed the trusted Ventoy USB to boot without clearing all UEFI security settings.

---

## 7. Docker Validation Should Include a Real Container Test

Checking the Docker service was not enough.

Running:

```bash
docker run hello-world
```

confirmed the full container workflow from image download to execution.

---

## 8. Public and Private Documentation Should Be Separated

The public project explains the architecture, implementation and troubleshooting.

Sensitive operational data should remain in private documentation.

This provides portfolio value without exposing the internal environment.

---

# Infrastructure Roles

The new homelab has a clear separation of responsibilities.

```text
Protectli
    │
    └── Networking and Firewalling

Ryzen Lab
    │
    └── Virtualization

HP Mini
    │
    └── Linux and Docker

Toshiba
    │
    └── Administration

Tailscale
    │
    └── Secure Cross-Network Management
```

---

# Future Lab Capabilities

The completed foundation supports future labs involving:

- Windows Server
- Active Directory
- Windows 11
- Group Policy
- DNS
- DHCP
- Linux administration
- Docker
- Docker Compose
- Infrastructure monitoring
- OPNsense firewall rules
- VLANs
- Microsoft Entra ID
- Microsoft 365
- Intune
- Hybrid identity
- Automation
- Infrastructure as Code

---

# Project Outcome

The Protectli was successfully configured as a dedicated physical OPNsense firewall and router.

The lab network was separated from the production network.

The mini switch was converted into the dedicated lab switch.

The Ryzen system was successfully rebuilt as a Proxmox host.

The secondary NVMe was converted into additional LVM-Thin VM storage.

The HP Mini was successfully rebuilt as an Ubuntu Linux and Docker server.

SSH, Tailscale, Tailscale SSH, Docker Engine, Docker Compose, Git and remote administration were validated.

The final environment now provides:

```text
OPNsense
    ↓
Routing, DHCP, DNS, NAT and Firewalling

Proxmox
    ↓
Windows and Linux Virtual Machines

Ubuntu Server
    ↓
Linux and Docker Labs

Tailscale
    ↓
Secure Cross-Network Administration

Toshiba
    ↓
Dedicated Lab Administration
```

This project transformed the homelab from a collection of separate devices into a structured infrastructure platform with clear roles, network isolation and secure administration.

---

# Project Status

```text
[✓] Protectli hardware installed
[✓] OPNsense installed
[✓] Root password recovered
[✓] WAN interface identified
[✓] LAN interface identified
[✓] Dedicated lab subnet created
[✓] DHCP validated
[✓] DNS validated
[✓] NAT validated
[✓] Internet access validated
[✓] OPNsense configuration backed up
[✓] Mini switch rewired as lab switch
[✓] Toshiba configured as lab admin node
[✓] Proxmox installed on Ryzen Lab
[✓] Proxmox repositories corrected
[✓] Proxmox updated
[✓] Secondary NVMe wiped
[✓] Additional LVM-Thin storage created
[✓] Tailscale installed on Proxmox
[✓] Tailscale SSH enabled on Proxmox
[✓] Proxmox accessible from Jellyfin PC
[✓] Homepage updated
[✓] Ubuntu installed on HP Mini
[✓] Ventoy Secure Boot issue resolved
[✓] SSH installed on HP Mini
[✓] Tailscale installed on HP Mini
[✓] Tailscale SSH enabled on HP Mini
[✓] SSH validated from Jellyfin PC
[✓] Docker Engine installed
[✓] Docker Compose installed
[✓] Docker service enabled
[✓] Docker service active
[✓] Hello World container validated
[✓] Homelab repository cloned
[✓] Public documentation sanitised
[✓] Project complete
```

---

# Next Steps

The next stage of the homelab roadmap will build services and lab environments on top of the new foundation.

Planned next steps include:

```text
Windows Server VM
        │
        ▼
Active Directory Domain Services
        │
        ▼
DNS and DHCP
        │
        ▼
Windows 11 Client
        │
        ▼
Group Policy
        │
        ▼
Hybrid Identity
        │
        ▼
Microsoft Entra ID and Microsoft 365
```

Additional infrastructure improvements include:

- OPNsense firewall rule labs
- VLANs
- Proxmox backup configuration
- OPNsense monitoring
- Proxmox monitoring
- Linux VM deployments
- Docker service deployments
- Private IP address register
- Switch port register
- Cable colour map
- Infrastructure diagrams
- Automated build documentation
