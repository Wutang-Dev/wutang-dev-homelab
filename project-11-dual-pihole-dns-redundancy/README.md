# Project 11 – Dual Pi-hole DNS Redundancy

## Objective
Implement DNS redundancy within the WuTang homelab to maintain reliable name resolution during single-node failure.

---

## Environment Overview

Two independent Pi-hole instances were deployed within the internal network to provide DNS failover capability.

Primary Node:
- Hostname: `pihole`
- Internal Address: `192.168.x.x`

Secondary Node:
- Hostname: `pihole-2`
- Internal Address: `192.168.x.x`

Router DNS Configuration:
- Primary DNS → Internal Pi-hole (Node 1)
- Secondary DNS → Internal Pi-hole (Node 2)

*Note: Internal addressing intentionally obfuscated for security hygiene.*

---

## Implementation Steps

1. Deployed a second Pi-hole instance on a separate host.
2. Exported configuration from the primary node using the built-in Teleporter feature.
3. Imported configuration into the secondary node.
4. Rebuilt the gravity database on the secondary instance:

```bash
sudo pihole -g
```

5. Verified DNS resolution and filtering behaviour using:

```bash
dig example.com
dig known-ad-domain.com
```

---

## Validation Testing

### DNS Resolution Test
- Legitimate domains resolved to valid public IP addresses.
- Query status returned `NOERROR`.

### Ad-Blocking Test
- Known advertising domains returned `0.0.0.0`.
- Confirmed gravity database loaded successfully (~78k domains).

### Failover Simulation
- Primary Pi-hole node temporarily powered off.
- Secondary node continued resolving DNS requests.
- Internet connectivity remained operational.
- No client-side DNS interruption observed.

---

## Results

- Dual DNS redundancy successfully implemented.
- Blocklists synchronized across both nodes.
- ~78,000 domains active in gravity database.
- Manual configuration sync method retained (Teleporter-based).
- Infrastructure resilience improved.

---

## Future Enhancements

- Automate configuration synchronization via SSH/rsync.
- Implement scheduled gravity synchronization.
- Add monitoring and alerting for node health.
- Explore centralized logging for DNS query analysis.

---

## Key Takeaways

- Redundant DNS significantly improves network reliability.
- Configuration portability simplifies multi-node deployments.
- Controlled failover testing validates infrastructure resilience.
- Security-conscious documentation practices reduce exposure risk.

---

**Status:** Operational  
**Sync Method:** Manual (Teleporter)  
**Redundancy Level:** Functional DNS Failover
