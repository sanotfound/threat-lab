# Environment: Kali + Metasploitable2

> Lab topology used for all `metasploitable2/` exercises.

---

## Topology

| Role | OS | IP | Notes |
|---|---|---|---|
| Attacker | Kali Linux 2026.2 | 192.168.10.10 | VirtualBox VM |
| Target | Metasploitable2 | 192.168.10.20 | VirtualBox VM, intentionally vulnerable |
| Secondary target | Alpine Linux ("alpine-endpoint") | 192.168.10.40 | VirtualBox VM, added starting with exercise 05, runs in live/diskless mode (see Setup Notes) |

All VMs run on a VirtualBox internal network named `LabCyber` (192.168.10.0/24), isolated from any external network. Connectivity confirmed via ICMP (`ping`) prior to any scanning.

This internal network was observed to behave like a hub rather than a switch: an interface in promiscuous mode (e.g., Wireshark) receives a copy of every frame on the segment, including ones addressed to a different MAC. This matters for evidence review, passive visibility on a capture is not by itself proof that a host actually processed or relayed a given frame, see [05-arp-poisoning-mitm.md](05-arp-poisoning-mitm.md) for a case where this nearly produced a false positive.

---

## Rules of Engagement (self-imposed)

- Both machines are owned by me and exist solely for this study.
- No exercise here targets anything outside this internal network.
- Every exercise is documented with a defensive angle (detection + mitigation), not exploitation alone.

---

## Setup Notes

- Metasploitable2 has a large number of intentionally vulnerable services, several corresponding to real historical CVEs and, in a few cases, real supply-chain backdoor incidents (e.g., vsftpd 2.3.4, UnrealIRCd).
- DNS resolution is not configured in the Kali VM (`/etc/resolv.conf` absent). This is irrelevant for IP-based scanning against an internal target, but scans are run with `-n` to avoid reverse-DNS lookup attempts/warnings.
- Static IPs on both VMs were originally assigned at runtime with `ifconfig` (e.g. `sudo ifconfig eth0 192.168.10.10 netmask 255.255.255.0`). This assignment does **not** persist across a VM reboot. After a restart, Kali fell back to DHCP (observed as `DHCP Discover` broadcasts in Wireshark) and lost connectivity to the target (`Network is unreachable`).
  - **Fix in place:** both VMs are snapshotted in VirtualBox once the static IP is confirmed working. Each study session starts by restoring that snapshot, rather than re-running `ifconfig` manually.
- **alpine-endpoint** runs from the ISO directly (live/diskless), not installed to disk, because its minimal ISO lacks the `syslinux` package needed for an installed bootloader and the lab has no internet access to fetch it. It has no persistent storage, so its IP (`ip addr add 192.168.10.40/24 dev eth0`) must be reconfigured by hand every time the VM boots, the snapshot fix used for the other two VMs does not apply here.
- The host machine has 8GB of RAM total. Running all three VMs simultaneously alongside Wireshark has caused a VirtualBoxVM.exe crash before. A Wazuh SIEM was attempted and abandoned for the same reason, see [wazuh-siem-attempt.md](../wazuh-siem-attempt.md).
