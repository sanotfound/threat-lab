# Wazuh SIEM Deployment Attempt

> Attempt to add Wazuh as a third VM in the lab, to observe an attack and its detection simultaneously from both sides. Deferred due to a host hardware constraint, not a failure of the configuration itself.

![Status](https://img.shields.io/badge/status-deferred-yellow)

---

## Objective

Deploy Wazuh (a pre-existing OVA from a prior course) as a SIEM alongside Kali and Metasploitable2, to watch an attack and its corresponding detection happen at the same time, from both the attacker's and defender's perspective, rather than reconstructing evidence after the fact as in the numbered exercises.

---

## Environment

- Wazuh v4.14.7 OVA (Amazon Linux based), originally configured with 4096 MB RAM and 4 CPUs
- Placed on the same isolated internal network as Kali and Metasploitable2 (192.168.10.0/24), assigned 192.168.10.30
- Host machine: 8 GB total RAM

---

## What Was Configured

### Network

Static IP assigned at runtime (`ip addr add`), the same non-persistent limitation already documented for the other VMs in [00-environment.md](metasploitable2/00-environment.md). Connectivity to both Kali and Metasploitable2 confirmed via ping.

### Remote Syslog Reception

Two constraints ruled out the standard approach (installing a Wazuh agent on Metasploitable2):

- Metasploitable2's `vsftpd.log` does not use the standard syslog subsystem, it is a custom-format log file written directly to disk (established in [03-vsftpd-backdoor.md](metasploitable2/03-vsftpd-backdoor.md)), so no agent or native forwarding rule would pick it up on its own.
- Metasploitable2's architecture (i686, 32-bit, confirmed via `sysinfo` in exercise 03) is incompatible with the Wazuh agent packages available for Linux, which are only distributed for 64-bit architectures (amd64/aarch64). Installing a modern `rsyslog` as a replacement was also attempted and failed, the isolated lab network has no route to the internet, confirmed by a DNS resolution failure during `apt-get install`.

The workaround used tools already present on Metasploitable2:

1. `tail -F -n0 /var/log/vsftpd.log | while read line; do logger -t vsftpd -p local1.info "$line"; done &`, injecting new log lines into the local syslog subsystem under facility `local1`
2. A line added to `/etc/syslog.conf` (the classic `sysklogd` format already present on this system): `local1.* @192.168.10.30`, forwarding those messages to Wazuh over UDP 514
3. A `<remote>` block added to the Wazuh manager's `/var/ossec/etc/ossec.conf`, accepting syslog on UDP 514, restricted to the lab's /24 subnet via `allowed-ips`

### Verification

- `tcpdump` on the Wazuh VM confirmed syslog packets from Metasploitable2 arriving on port 514 with the expected facility/priority tag, proving the network delivery leg worked correctly.
- Wazuh's own self-monitoring independently generated a real alert, "Interface entered in promiscuous (sniffing) mode" (rule level 8), in response to that same diagnostic `tcpdump` command. This was not planned, but is a genuine demonstration of the platform's detection capability, using its own audit trail.
- A generic test message sent via `logger` did not appear in the Wazuh dashboard's alert view (`wazuh-alerts-*` index). This is expected behavior, not a failure: alerts and raw archived events are different things in Wazuh. Only events that match a detection rule populate the default alerts index; archiving every raw event requires enabling `logall`, a step this attempt did not reach.

---

## The Constraint That Ended the Attempt

The host machine has 8 GB of RAM total. Running all three VMs at once, Wazuh (4096 MB), Kali (2048 MB), and Metasploitable2 (1024 MB), pushed host memory usage to 96%, which caused a `VirtualBoxVM.exe` crash (a Windows-side memory access violation) during an unrelated configuration edit. Reducing allocations (Wazuh to 3072 MB, Metasploitable2 to 512 MB) improved things marginally, to 94% usage, but did not resolve the underlying issue: 8 GB is not enough to comfortably run this specific three-VM topology alongside a modern desktop and its background processes.

A second network adapter on the Wazuh VM (a VirtualBox Host-Only Network) was considered, which would let the host's own browser reach the dashboard without Kali powered on, reducing the simultaneous requirement to two VMs for most purposes. This was deliberately not implemented: it would make Wazuh dual-homed between the isolated lab network, which includes the intentionally vulnerable Metasploitable2 and would include any future malware samples, and the host machine's own network. That is a real pivot risk if Wazuh were ever compromised, however unlikely given it is not an intentionally vulnerable target itself. The convenience was judged not worth that trade-off.

---

## Decision

Wazuh has been removed from the lab for now. The lab continues with Kali and Metasploitable2 only. Revisiting SIEM-based detection is left open for later, contingent on either more host RAM or a deliberately scoped-down architecture, such as a lighter Wazuh configuration or a host-only bridge accepted with its risk explicitly acknowledged and time-boxed.

---

## Lessons

- Resource sizing for a home lab is a real engineering constraint, not just an inconvenience. The same reasoning, budgeting memory across simultaneous workloads, applies in real infrastructure planning.
- A "paused" or "saved state" VM in VirtualBox does not release its reserved RAM back to the host. Only a full power-off does.
- Legacy systems can block modern tooling in non-obvious ways. Metasploitable2's 32-bit architecture ruled out a 64-bit-only agent package entirely, a realistic constraint an analyst would encounter with genuinely old infrastructure, not a configuration mistake.
- A working technical configuration does not automatically translate into project success. Hardware constraints can be the actual limiting factor, and recognizing that early, and documenting it rather than hiding it, is itself a valid engineering decision.
