# Project 27 – Deploying a Windows 11 Virtual Machine in Proxmox

## Overview

The objective of this project was to deploy my first Windows 11 virtual machine within my Proxmox environment, configure the required VirtIO drivers, install the QEMU Guest Agent, and integrate the VM into my Microsoft Intune tenant as an additional managed device for future endpoint management testing.

---

## Installing the QEMU Guest Agent on Ubuntu Server

Before creating the virtual machine, I installed the QEMU Guest Agent on my Ubuntu monitoring server to improve communication between the guest operating system and the Proxmox host.

### Commands Used

```bash
sudo apt install qemu-guest-agent
systemctl status qemu-guest-agent
sudo systemctl start qemu-guest-agent
sudo systemctl enable qemu-guest-agent
```

### Outcome

* Installed the QEMU Guest Agent package.
* Verified service status.
* Started the service manually as it was not running.
* Configured the service to start automatically on boot.

---

## Uploading Installation Media to Proxmox

I uploaded the Windows 11 installation ISO from my central ISO repository stored on Jellyfin.

### Steps

1. Navigated to:

```text
Local (proxmox3)
└── ISO Images
    └── Upload
```

2. Uploaded the Windows 11 ISO.

3. Downloaded and uploaded the Proxmox VirtIO Driver ISO.

### Why VirtIO Drivers?

VirtIO drivers provide improved virtualized hardware performance and allow Windows to recognise virtual disks and network adapters within Proxmox.

---

## Creating the Virtual Machine

I created a new virtual machine using the following configuration.

### VM Configuration

| Setting            | Value             |
| ------------------ | ----------------- |
| VM ID              | 101               |
| Name               | windows-11-01     |
| Guest OS           | Microsoft Windows |
| TPM                | Enabled           |
| TPM Storage        | local-lvm         |
| EFI Storage        | local-lvm         |
| Disk Size          | 64 GB             |
| CPU Cores          | 4                 |
| Memory             | 4 GB              |
| VirtIO Drivers ISO | Attached          |
| QEMU Guest Agent   | Enabled           |

### Outcome

The virtual machine was successfully created and ready for Windows installation.

---

## Installing Windows 11

The Windows installation initially failed to detect a storage device.

### Issue

No disks were available during the Windows installation process.

### Troubleshooting

I initially attempted to install all VirtIO drivers from the mounted VirtIO ISO, but Windows still could not detect the virtual disk.

### Resolution

I manually loaded the storage driver from:

```text
VirtIO ISO
└── vioscsi
    └── w11
        └── amd64
```

After loading the correct storage driver:

* The 64 GB virtual disk became visible.
* Windows installation continued successfully.

---

## Network Connectivity Issue

During setup, Windows 11 required an internet connection before allowing installation to continue.

### Resolution

I added an additional virtual network adapter from the Proxmox web interface.

### Network Adapter Used

```text
Intel E1000
```

After adding the adapter, Windows was able to obtain network connectivity and continue the installation process.

---

## Enrolling the VM into Microsoft Intune

After Windows installation completed, I enrolled the virtual machine into my Microsoft 365 tenant.

### Account Used

```text
rg@rg-wutanglan.co.uk
```

### Device Name

```text
windows-proxmox-vm-01
```

I chose this naming convention to allow future expansion with additional virtual machines.

### Group Membership

The device was added to:

```text
Lab-Devices-Security-Group
```

This group is nested within my Managed Devices security structure and automatically receives assigned applications and policies.

---

## Application Deployment Testing

After enrollment, I installed Company Portal and verified application deployment functionality.

### Available Applications

* Cisco Packet Tracer
* Git
* Google Chrome
* Visual Studio Code
* LibreOffice
* PuTTY
* 7-Zip
* Python

### Outcome

The virtual machine successfully received assigned applications from Intune, validating device enrollment and application deployment functionality.

---

## Driver Remediation

Following installation, Device Manager showed several missing devices.

### Missing Drivers

* Network Controller
* PCI Device
* PCI Simple Communications Controller

### Resolution

Installed the appropriate VirtIO drivers from the mounted VirtIO ISO.

### Outcome

All missing devices were successfully resolved.

---

## Installing the Windows QEMU Guest Agent

To complete integration with Proxmox, I installed the Windows version of the QEMU Guest Agent.

### Installer Used

```text
qemu-ga-x86_64.msi
```

### Outcome

* Guest Agent installed successfully.
* Enhanced communication between Proxmox and the Windows VM enabled.
* VM management features such as IP reporting and graceful shutdown support became available.

---

## Skills Practiced

* Proxmox virtual machine deployment
* Windows 11 installation
* VirtIO storage and network driver installation
* QEMU Guest Agent deployment
* Troubleshooting storage driver issues
* Troubleshooting Windows 11 network requirements
* Microsoft Intune device enrollment
* Application deployment validation
* Endpoint management concepts

---

## Project Outcome

Successfully deployed and configured a Windows 11 virtual machine within Proxmox, integrated it with Microsoft Intune, validated application deployment through Company Portal, installed all required VirtIO drivers, and configured the QEMU Guest Agent for enhanced virtualization management.

This VM will serve as an additional managed endpoint for future Microsoft Intune, Microsoft 365, and endpoint management lab projects.
