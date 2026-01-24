# Project 05 – Ubuntu DevOps Node Setup (MacBook)

## Goal
Repurpose an old MacBook into a secure Ubuntu-based DevOps node for infrastructure, server, and cloud labs.

## Environment
- Ubuntu 24.04 LTS
- Repurposed MacBook hardware
- Wi-Fi connectivity
- Tailscale private mesh network
- GitHub SSH authentication

## What Was Implemented
- Clean Ubuntu Desktop installation
- Secure networking configuration
- SSH enabled for remote administration
- Tailscale installed and joined to an existing tailnet
- Verified private network access to internal services:
  - Pi-hole (DNS / admin dashboard)
  - Jellyfin (media server)
- Google Chrome installed for browser-based labs and documentation
- GitHub SSH keys generated and configured
- `wutang-dev` repository cloned to the node

## Validation
- SSH access confirmed locally and over Tailscale
- Tailnet connectivity verified across multiple devices
- Internal services accessible via private DNS and IPs
- GitHub SSH authentication tested successfully
- Repository state confirmed in sync with origin

## Outcome
This system now functions as a portable, secure DevOps control node. It will be used for future projects involving web servers, containers, CI/CD pipelines, and cloud infrastructure.
