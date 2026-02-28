# Project 13 – OPNsense Firewall Deployment with NAT, DHCP and Internet Routing (Hyper-V Lab)

## 🧠 Objective

Deploy a fully functional firewall inside Hyper-V using OPNsense with:

- Dual NIC configuration (WAN + LAN)
- Internal segmented switch
- DHCP server on LAN
- Automatic outbound NAT
- DNS resolution
- Full internet routing from an internal Ubuntu host

This lab simulates a small business edge firewall architecture.

---

## 🏗 Lab Architecture

```
Internet
    ↓
Home Router (192.168.0.x)
    ↓
OPNsense WAN (192.168.0.x)
    ↓
OPNsense LAN (192.168.1.1)
    ↓
fw-internal-switch (Private)
    ↓
Ubuntu Client (192.168.1.x)
```

---

## ⚙️ Hyper-V Configuration

### OPNsense VM
- 2 Network Adapters
  - Adapter 1 → External Virtual Switch (WAN)
  - Adapter 2 → fw-internal-switch (Private LAN)
- 4GB RAM
- 2 vCPU

### Ubuntu VM
- Connected to fw-internal-switch only
- Obtains IP via DHCP from OPNsense

---

## 🔧 OPNsense Configuration Steps

### 1️⃣ Interface Assignment

- WAN → hm1 (External Switch)
- LAN → hm0 (fw-internal-switch)

---

### 2️⃣ LAN Configuration

- LAN IP: `192.168.1.1/24`
- DHCP Server: Enabled
- DHCP Range: `192.168.1.100 – 192.168.1.200`

---

### 3️⃣ WAN Configuration

- WAN received IP from home router (192.168.0.x)
- Default gateway automatically assigned

---

### 4️⃣ NAT Configuration

- Automatic Outbound NAT enabled (default mode)

---

## 🧪 Verification Testing

### ✅ DHCP Working

Ubuntu received dynamic IP:

```
inet 192.168.1.177/24
```

---

### ✅ Gateway Reachable

```
ping 192.168.1.1
```

Successful responses confirm LAN communication.

---

### ✅ NAT Working

```
ping 8.8.8.8
```

Successful replies confirm:

- WAN connectivity
- Outbound NAT translation
- Firewall rules allowing traffic

---

### ✅ DNS Working

```
ping google.com
```

Successful resolution confirms:

- DNS resolver functioning
- Proper DNS forwarding via OPNsense

---

## 🔥 Results

The following services are fully operational:

- DHCP Server
- DNS Resolver
- Stateful Firewall
- Outbound NAT
- LAN to WAN Routing
- Internet Access for Internal Clients

---

## 🎯 Skills Demonstrated

- Hyper-V Virtual Switch configuration
- Dual-NIC firewall deployment
- Interface assignment troubleshooting
- Layer 3 routing validation
- NAT verification
- DNS testing
- End-to-end packet flow analysis

---

## 🚀 Outcome

This project simulates a real-world small business firewall architecture with:

- Segmented internal network
- Routed WAN boundary
- Stateful inspection
- Internet egress control

The lab is now ready for:

- VLAN implementation
- IDS/IPS deployment
- Firewall rule hardening
- Port forwarding
- DMZ configuration
- Multi-subnet routing

---

**Status:** Fully Operational  
**Project:** Completed Successfully
