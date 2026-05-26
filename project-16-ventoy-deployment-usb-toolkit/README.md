# Project 16 — Ventoy Deployment USB Toolkit

## Overview

Created and validated a portable multi-boot deployment USB using Ventoy to support future homelab, virtualization, endpoint, and infrastructure projects.

Goal: maintain a reusable deployment toolkit for operating system installation, recovery, testing, and future lab environments.

---

## Technologies Used

- Ventoy
- Proxmox VE ISO
- Windows 11 ISO
- Windows Server ISO
- Ubuntu Desktop ISO
- Ubuntu Server ISO

---

## Why This Project?

Instead of maintaining multiple bootable USBs, Ventoy allows multiple operating system ISOs to coexist on a single deployment device.

Benefits:

- Faster provisioning
- Centralised deployment media
- Easier ISO management
- Reduced hardware clutter
- Reusable installation toolkit

---

## USB Contents

| ISO | Planned Usage |
|------|----------------|
| Proxmox VE | HP Mini virtualization host |
| Windows 11 | Endpoint projects |
| Windows Server | MSP Lab / AD environments |
| Ubuntu Desktop | Linux learning |
| Ubuntu Server | Server deployments |

---

## Validation Testing

Validation testing performed on Ryzen-Lab.

Test completed:

✅ Ventoy USB booted successfully

✅ Ventoy menu loaded correctly

✅ Proxmox VE ISO launched successfully

No installation was performed to preserve the existing Ryzen-Lab Hyper-V environment.

This confirmed the deployment toolkit is operational and ready for future infrastructure projects.

---

## Planned Usage

Future projects:

- HP Mini → Proxmox deployment
- Endpoint device builds
- MSP Lab rebuilds
- Linux server testing
- Windows Server environments

---

## Lessons Learned

- Multi-boot deployment significantly reduces setup friction.
- Pre-built deployment tooling improves repeatability.
- Validating installation media before production usage reduces deployment risk.
