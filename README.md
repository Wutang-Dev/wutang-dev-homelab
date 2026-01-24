# WuTang Homelab (private Repo)
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
	   
    ## Future Work / TODO
    - LAN + Tailscale container access testing
    - Migrate pi-hole into docker
    - Explore self-hoting media stak (Jellyfin, ect)
    - Architecture diagrams + Topology notes
    - Automation + SCripts + deployment workflow 
