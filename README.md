# 🔥 **ScreenPulse -- Windows Recon & Screenshot Dropper**

ScreenPulse is a Windows exclusive recon operator that sweeps the
system, fingerprints the machine, snaps a desktop screenshot every 2
minutes, and ships everything straight to your webhook without getting
Discord rate-limited or banned.

Clean. Silent. Automated.\
Built for red team simulations and cyber research.

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

  Feature                    Details
  -------------------------- -------------------------------------------
  🖥 System Recon             Username, hostname, OS, architecture, CPU
  🧠 System Stats            RAM, disk usage, uptime, active sessions
  🔋 Battery Data            Battery %, charge state
  🌐 Network                 Private IP + Public IP via ipify
  📡 WiFi Info               SSID via netsh (Windows only)
  🪪 Hardware Fingerprints   MAC address
  📸 Screenshot Capture      Full desktop PNG every 2 minutes
  🎨 Random Embed Colors     Looks cleaner in Discord
  🔁 Auto Loop               Sends data forever



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

# 🛠️ **Installation**

### Install Python modules:

    pip install -r requirements.txt

# ⚙️ **Configuration**

Inside the script:

    WEBHOOK_URL = "YOUR_WEBHOOK_HERE"

Paste your Discord webhook.

# ▶️ **Run ScreenPulse**

    python screenpulse.py

Runs forever --- sends a full recon packet every **120 seconds**.

To change delay:

    time.sleep(120)


# ⚠ **Disclaimer**

ScreenPulse is created for **Windows forensic research, red team
simulations, and educational purposes only**.

Do not run this tool on systems without explicit permission.

## **Contributors:**

* [AnonKryptiQuz](https://github.com/AnonKryptiQuz)
* [Hghost0x00](https://github.com/Hghost0x00)


## **Author**

**Created by:** [Nuknov](https://github.com/Nuknov)


