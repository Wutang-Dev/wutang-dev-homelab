# 2026-01-26 – Project 07 – Nginx Reverse Proxy (Local + Remote Services)

## Summary

Today I implemented a functional Nginx reverse proxy on my Ubuntu MacBook.

The objective was to route traffic to multiple backend services using path-based routing, including both a local Python HTTP test server and a remote Pi-hole instance accessed via Tailscale.

This project built directly on my previous Nginx installation and firewall configuration work.

---

## What I Implemented

- Installed and validated Nginx service
- Enabled and configured UFW firewall
- Created a reverse proxy configuration
- Proxied:
  - `/app/` → Python HTTP server (localhost:9000)
  - `/pihole/` → Pi-hole admin interface (Raspberry Pi via Tailscale)
- Tested routing via browser and curl
- Verified DNS remained unaffected
- Corrected directory structure mistake before final push

---

## What I Learned

- Reverse proxy architecture and traffic flow
- Importance of trailing slashes in `proxy_pass`
- Difference between DNS service (port 53) and web admin interface (port 80)
- Safe change validation using:
  - `nginx -t`
  - `systemctl reload nginx`
- How to safely restructure a Git repository without breaking history

---

## Mistakes & Fixes

- Initially saved the project in the wrong directory (`projects/`)
- Moved the folder to the correct root level
- Removed unused directory
- Committed structural correction cleanly

---

## Reflection

This was the first time I routed multiple services through a single reverse proxy entry point.

It feels like I’m moving from basic Linux practice into actual infrastructure design thinking.

This project mirrors real-world DevOps routing patterns used in production environments.

