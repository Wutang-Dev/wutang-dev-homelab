# WuTang Homelab 
## Overview
Private homelab project built using WSL2,Docker, and Tailscaile.
Documenting deployments, networking, and DevOps learning

## Environment
- Host: Ryzen 3600 workstation (wutang-dev(machine name)
- OS : Windows 11 + WLS2
- Networking: Pi hole + Tailacale Integration
- Access: Private LAN + remote Tailscale

  ## Current Stack
  - Docker Installed and verified (`hello-world`)
  - Test container deployed (`nginx` on port 8080)
  - Git + SHH configured for GitHub access
  - Private GitHub repo for documentation
 
    ## Progress Log
    **2026-01-20**
    - Rebuilt WuTang-Dev workstation
    - Installed WSl2 + Ubuntu 24.04
    - Enabled systemd inside WSL2
    - installed toolchain (git ,curl , gcc)
    - Installed Docker + verified container functionality
    - Deployed nginx container mapped to 8080
    - Configured Git + SSH keys for GitHub
    - Created private repo + intial commit
    
    **2026-01-22**
    - Started learning Linux
 
      
	**2026-01-24**
	- Repurposed MacBook into Ubuntu 24.04 DevOps node
	- Configured Wi-Fi networking and enabled SSH
	- Installed and joined device to Tailscale tailnet
	- Verified private access to Pi-hole admin dashboard
	- Verified Jellyfin access over tailnet
	- Installed Google Chrome for browser-based labs
	- Generated and configured GitHub SSH keys on Ubuntu
	- Cloned wutang-dev repository onto the DevOps node
	- Created and documented Project 05 – Ubuntu DevOps node setup

 
   **2026-01-25**
   - Completed Project 06 – Nginx on MacBook
   - Installed and validated Nginx service
   - Enabled UFW and configured web firewall rules
   - Verified HTTP access using curl
 
   **2026-01-26**
- Implemented Nginx reverse proxy
- Routed local Python HTTP app via /app/
- Routed remote Pi-hole via /pihole/ using Tailscale
- Enabled and configured UFW firewall
- Verified DNS stability across WuTangLAN
- Restructured project directory for clean repo hygiene

  **2026-01-27**
- Configured HTTPS on Nginx using a self-signed SSL certificate
- Generated and installed SSL certificate under `/etc/nginx/ssl`
- Configured Nginx to listen on port 443 (HTTPS)
- Served a static site securely from `/var/www/project08`
- Validated HTTPS using curl and web browser
- Debugged port 443 issues by verifying active listeners and enabled sites

 **2026-01-28**
- Implemented permanent HTTP → HTTPS redirection using a 301 redirect
- Hardened Nginx HTTPS configuration with security-focused headers
- Reused existing self-signed SSL certificate for HTTPS enforcement
- Added HTTP security headers:
  - Strict-Transport-Security (HSTS)
  - X-Content-Type-Options
  - X-Frame-Options
  - Referrer-Policy
- Validated redirect and HTTPS behaviour using curl headers
- Confirmed HTTPS access via web browser
- Verified Nginx configuration integrity with nginx -t
- Reloaded Nginx to apply hardened HTTPS configuration
- Completed Project 09 – Nginx HTTPS Hardening


**2026-01-29**

- Installed and validated Docker on Ubuntu
- Built a Docker image for a Python HTTP application
- Containerised a Python web app using a Dockerfile
- Ran the container with explicit port mapping (8080 → 5000)
- Verified container runtime using docker ps
- Validated application access via browser and curl
- Troubleshot and resolved Docker image naming issues
- Completed Project 10 – Dockerised Python Application


	   
    ## Future Work / TODO
    - LAN + Tailscale container access testing
    - Migrate pi-hole into docker
    - Explore self-hoting media stak (Jellyfin, ect)
    - Architecture diagrams + Topology notes
    - Automation + SCripts + deployment workflow 



