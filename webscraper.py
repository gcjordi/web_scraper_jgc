from bs4 import BeautifulSoup
import requests
import msvcrt
r = requests.get("https://store.steampowered.com/app/1091500/Cyberpunk_2077/")
soup = BeautifulSoup(r.content, "lxml")
precio = soup.find('div', class_= "game_purchase_price price").text
print (precio.strip())
nombre = soup.find('div', class_= "apphub_AppName").text
print(nombre)
msvcrt.getch()