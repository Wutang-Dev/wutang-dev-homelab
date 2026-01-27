# 2026-01-27 – Project 08 – Nginx HTTPS (Self-Signed) ---


## Overview

In this project, I configured HTTPS on Nginx using a self-signed SSL certificate.

The objective was to understand how TLS works at the web server level, including certificate generation, secure listeners on port 443, and validating HTTPS using both command-line tools and a web browser.

This project builds directly on:

Project 06 – Nginx installation and firewall configuration

Project 07 – Reverse proxy fundamentals


## Environment

Host: MacBook

OS: Ubuntu

Web Server: Nginx

Firewall: UFW (enabled)



## What I Implemented

Generated a self-signed SSL certificate

Configured Nginx to listen on port 443 (HTTPS)

Served a static website securely over HTTPS

Validated service using curl and a web browser

Debugged port and service issues using system tools

SSL Certificate

Self-signed certificate created and stored at:

/etc/nginx/ssl/



## Files:

project08.crt

project08.key



## Web Root

Static site served from:

/var/www/project08




## Files:

index.html

Permissions set for Nginx:

sudo chown -R www-data:www-data /var/www/project08


## Nginx Configuration

HTTPS site defined under sites-available

Enabled via symbolic link in sites-enabled

Nginx configured with:

listen 443 ssl

Certificate and key paths

Document root pointing to /var/www/project08

Validation Steps

Check Nginx configuration:

sudo nginx -t

Reload Nginx:

sudo systemctl reload nginx


Confirm active listeners:

sudo ss -tulpn | grep nginx


Test HTTPS locally (ignoring certificate warning):

curl -k https://localhost


## Result

HTTPS is successfully enabled and serving content on port 443.

The site is accessible via:

curl using -k

Web browser (with expected self-signed certificate warning)

Troubleshooting & Lessons Learned

Initially, HTTPS failed because Nginx was not listening on port 443.

Instead of assuming a firewall issue, I verified:

Enabled sites

Active listeners

Nginx configuration syntax

This reinforced the importance of checking service state and ports before modifying firewall rules.

-

## Key Takeaways

HTTPS requires an explicit listener on port 443

Certificates must be correctly referenced in Nginx configs

Most HTTPS issues are configuration-related, not firewall-related

Self-signed certificates are ideal for lab and learning environments

