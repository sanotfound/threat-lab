# Environment: Kali + Metasploitable2

> Lab topology used for all `metasploitable2/` exercises.

---

## Topology

| Role | OS | IP | Notes |
|---|---|---|---|
| Attacker | Kali Linux 2026.2 | 192.168.10.10 | VirtualBox VM |
| Target | Metasploitable2 | 192.168.10.20 | VirtualBox VM, intentionally vulnerable |

Both VMs run on a VirtualBox host-only/internal network, isolated from any external network. Connectivity confirmed via ICMP (`ping`) prior to any scanning.

---

## Rules of Engagement (self-imposed)

- Both machines are owned by me and exist solely for this study.
- No exercise here targets anything outside this internal network.
- Every exercise is documented with a defensive angle (detection + mitigation), not exploitation alone.

---

## Setup Notes

- Metasploitable2 has a large number of intentionally vulnerable services, several corresponding to real historical CVEs and, in a few cases, real supply-chain backdoor incidents (e.g., vsftpd 2.3.4, UnrealIRCd).
- DNS resolution is not configured in the Kali VM (`/etc/resolv.conf` absent) — irrelevant for IP-based scanning against an internal target, but scans are run with `-n` to avoid reverse-DNS lookup attempts/warnings.
- Static IPs on both VMs were originally assigned at runtime with `ifconfig` (e.g. `sudo ifconfig eth0 192.168.10.10 netmask 255.255.255.0`). This assignment does **not** persist across a VM reboot — after a restart, Kali fell back to DHCP (observed as `DHCP Discover` broadcasts in Wireshark) and lost connectivity to the target (`Network is unreachable`).
  - **Fix in place:** both VMs are snapshotted in VirtualBox once the static IP is confirmed working. Each study session starts by restoring that snapshot, rather than re-running `ifconfig` manually.
