# Project 06 – Nginx on MacBook

## Summary
In this project, I installed and configured Nginx on my MacBook Linux environment to understand how a web server runs as a system service and how it is exposed securely using a firewall.

I verified the service using systemd and confirmed HTTP connectivity locally.

## What I Practiced
- Installing Nginx on Linux
- Managing services with `systemctl`
- Understanding Nginx master and worker processes
- Enabling and configuring UFW firewall rules
- Allowing `Nginx Full` through the firewall
- Verifying service availability using `curl`

## Validation Steps
- `systemctl status nginx` → Active (running)
- `ufw status` → Firewall enabled
- `curl http://localhost` → Nginx welcome page returned

## Outcome
Nginx is running successfully, enabled on startup, and serving HTTP traffic locally.

