#Coded By Tetra
import os
import time
import pyfiglet
from colorama import Fore

r = Fore.RED
g = Fore.GREEN
b = Fore.BLUE
m = Fore.MAGENTA

while True:
    os.system("clear")
    logo = pyfiglet.figlet_format("SiteS DUMP")
    print(r + "\n" + logo)

    print(b + "< > Dev By TETRA </> \n")

    site = input(m + "Site Adresini Girin (Çıkış İçin 'q'): " + r)

    if site.lower() == 'q':
        break

    if site.startswith("https://"):
        site = site.replace("https://", "")

    elif site.startswith("http://"):
        site = site.replace("http://", "")

    if site:
        os.system(f"wget -q -mk http://{site.strip()}")
        print(g + f"Klasör '{site}' Adında Kaydedildi")
    else:
        print(r + "Geçersiz adres.")
    
    time.sleep(2)  
