import requests
import random
import time
import os
from colorama import Fore

print("   ____          ____       _                    ")
print("  | __ )  __ _  |  _ \ __ _| |_ ___ _ __   __ _  ")
print("  |  _ \ / _' | | |_) / _' | __/ _ \ '_ \ / _' | ")
print("  | |_) | (_| | |  __/ (_| | ||  __/ | | | (_| | ")
print("  |____/ \__, | |_|   \__,_|\__\___|_| |_|\__, | ")
print("         |___/                            |___/  \n")
print("=================================================")
author = "Bg.Pateng"
print("Author: " + author)
script = "Push Rank Discord"
print("Script: " + script)
telegram = "@bangpateng_group"
print("Telegram: " + telegram)
youtube = "Bang Pateng"
print("Youtube: " + youtube)
print("===========================================")
print('PERINGATAN : TIDAK UNTUK DI PERJUAL-BELIKAN')
print("===========================================\n")

time.sleep(1)

channel_id = input("Masukkan ID channel: ").strip()
waktu2 = int(input("Set Waktu Kirim Pesan (detik): "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

# ambil pesan
with open("pesan.txt", "r") as f:
    words = f.readlines()

# ambil token
with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    payload = {
        'content': random.choice(words).strip()
    }

    headers = {
        'Authorization': authorization
    }

    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        data=payload,
        headers=headers
    )

    if r.status_code == 200:
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])
    else:
        print(Fore.RED + f"Gagal kirim pesan: {r.status_code}")

    # delay acak biar lebih natural
    delay = random.randint(waktu2, waktu2 + 5)
    print(Fore.CYAN + f"Tidur {delay} detik...")
    time.sleep(delay)