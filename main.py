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

channel_id = input("Masukkan ID channel: ")
min_delay = int(input("Set Waktu Minimum Delay (detik): "))
max_delay = int(input("Set Waktu Maksimum Delay (detik): "))

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

with open("pesan.txt", "r") as f:
    words = f.readlines()

with open("token.txt", "r") as f:
    authorization = f.readline().strip()

while True:
    channel_id = channel_id.strip()

    payload = {
        'content': random.choice(words).strip()
    }

    headers = {
        'Authorization': authorization,
        'Content-Type': 'application/json'
    }

    r = requests.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        json=payload,
        headers=headers
    )

    if r.status_code == 200:
        print(Fore.WHITE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])
    else:
        print(Fore.RED + f"Gagal mengirim pesan: {r.status_code} - {r.text}")

    # random delay antara min_delay dan max_delay
    delay = random.randint(min_delay, max_delay)
    print(Fore.CYAN + f"Tunggu {delay} detik sebelum pesan berikutnya...")
    time.sleep(delay)