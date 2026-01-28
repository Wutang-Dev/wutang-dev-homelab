# 2026-01-28 – Project 09 – Nginx HTTPS Redirect & Hardening

---

## Overview

In this project, I enforced HTTPS across my Nginx setup by redirecting all HTTP traffic to HTTPS and applying basic security hardening headers.

The objective was to understand how HTTPS enforcement works at the web server level and how common security headers are applied in real-world configurations.

This project builds directly on:

Project 06 – Nginx installation and firewall configuration  
Project 08 – HTTPS with self-signed certificate  

---

## Environment

Host: MacBook  
OS: Ubuntu  
Web Server: Nginx  
Firewall: UFW (enabled)  

---

## What I Implemented

- HTTP to HTTPS redirection using a permanent 301 redirect
- Secure HTTPS listener on port 443
- Reused existing self-signed SSL certificate
- Added basic HTTP security headers
- Validated behaviour using curl and a web browser

---

## Nginx Configuration

The configuration consists of two server blocks:

- Port 80: Redirects all traffic to HTTPS
- Port 443: Serves content securely with TLS and security headers

Security headers applied:

- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy

---

## Validation Steps

Check Nginx configuration syntax:

sudo nginx -t

Reload Nginx:

sudo systemctl reload nginx

Confirm active listeners:

sudo ss -tulpn | grep nginx

Test HTTP redirect:

curl -I http://localhost

Test HTTPS response:

curl -k -I https://localhost

---

## Result

All HTTP traffic is automatically redirected to HTTPS.

HTTPS serves content correctly on port 443 with security headers applied.

The site is accessible via:

- curl (using the -k flag)
- A web browser (with an expected self-signed certificate warning)

---

## Troubleshooting & Lessons Learned

Initially, HTTPS issues appeared to be firewall-related.

By validating listeners and server blocks first, it became clear the problem was configuration-based rather than a network restriction.

This reinforced the importance of checking service state and behaviour before modifying firewall rules.

---

## Key Takeaways

- HTTPS enforcement requires an explicit redirect from port 80
- Security headers are applied at the web server level
- Most HTTPS issues are configuration-related, not firewall-related
- Redirecting HTTP to HTTPS is a baseline security requirement
