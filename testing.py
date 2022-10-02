from bs4 import BeautifulSoup
import requests
user = input("Escribe el usuario: ")
website = f'https://minecraftuuid.com/?search={user}'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
box = soup.find('input',placeholder='User UUID')
# nuevo = str(box)
dato = str(box).split(" ")[-1].removeprefix('value="').removesuffix('"/>')
print(f"La UUID del usuario {user} es: {dato}")
