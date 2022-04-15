import names
import requests
from colorama import *
url_base = 'https://github.com/'


amount = int(input(Fore.LIGHTGREEN_EX + 'Ingresa la cantidad de usuarios >  '))

for i in range(amount):
    url = url_base + (names.get_first_name())
    r = requests.get(url)
    

    if r.status_code == 200:
        print(Fore.LIGHTGREEN_EX + "[Válido] => " + Fore.RESET + url)
        open('github.log', 'a+').write(url + "\n")
    else:
        print(Fore.LIGHTBLACK_EX + "[Inválido] => " + Fore.RESET + url , r.status_code)
