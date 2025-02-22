# 🛠 ARP Spoofer (Python + Scapy)

A simple **ARP Spoofer** written in Python using the **Scapy** library. This script allows you to perform **ARP poisoning** to intercept network traffic between a target device and a gateway.

## ⚠️ Disclaimer

**This tool is for educational and ethical testing purposes only.**  
Unauthorized use on networks you don’t own or have permission to test is **illegal**.

---

## 🚀 Features

- **ARP Spoofing** : Redirects traffic by poisoning the ARP cache.
- **Auto-Restoration** : Restores ARP tables when the script is stopped.
- **Targeted Attack** : Spoofs only the specified IPs.

---

## 🛠 Installation

Ensure you have Python installed and then install **Scapy** :

```bash
pip install scapy
```

Clone this repository:

```bash
git clone https://github.com/XanderSteyn/ARP-Spoofer.git
cd ARP-Spoofer
```

Run the script with **sudo/admin privileges** :

```bash
sudo python ARPSpoofer.py -t <Target-IP> -g <Gateway-IP>
```

---

## 🎮 Usage

| Argument | Description |
|----------|------------|
| `-t`, `--target` | IP of the target machine |
| `-g`, `--gateway` | IP of the network gateway (router) |

**Example :**
```bash
sudo python ARPSpoofer.py -t 192.168.1.5 -g 192.168.1.1
```

---

## 🛑 How It Works

1. **Get Target MAC** : Sends an ARP request to fetch the MAC address.
2. **Spoof Target & Gateway** : Sends crafted ARP replies to both, making them think the attacker's MAC is legitimate.
3. **Maintain Spoofing** : Repeats the attack every 2 seconds to keep control.
4. **Restore ARP** : When stopped (`CTRL+C`), the script restores the original MAC addresses.

---

## 📌 Notes

- **Requires sudo/admin privileges** to modify network traffic.
- **Use with caution** – Can disrupt network communication if misused.
- **Does NOT work on encrypted networks with ARP protection.**

---
