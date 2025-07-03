import requests
import re
import time
from bs4 import BeautifulSoup
from colorama import Fore, init

init(autoreset=True)

def save(data, filename):
    with open(filename, "a") as file:
        file.write(data + "\n")

def get_list_domain(content, saveas):
    soup = BeautifulSoup(content, "html.parser")
    domains = set()
    
    for td in soup.find_all("td"):
        match = re.search(r"(https?://)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", td.text)
        if match:
            domain = match.group(2)
            domains.add(domain)
    
    for domain in sorted(domains):
        print(f"{Fore.GREEN}[✓] {domain}")
        save(domain, saveas)

def get_page(from_url):
    start_page = int(input('Grab From Page (example: 1): '))
    end_page = int(input('Grab To Page (Max Page 50): '))
    saveas = input('Save As (example.txt): ')
    
    if end_page > 50:
        print(f"{Fore.RED}Max Page Is 50!!")
        return
    
    for page in range(start_page, end_page + 1):
        page_url = f"{from_url}?page={page}"
        print(f"{Fore.YELLOW}[*] Grabbing from {page_url}...")
        
        try:
            response = requests.get(page_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
            if response.status_code == 200:
                get_list_domain(response.text, saveas)
            else:
                print(f"{Fore.RED}[!] Failed to retrieve {page_url}")
        except requests.RequestException as e:
            print(f"{Fore.RED}[!] Request failed: {e}")
        
        time.sleep(2)
    
    print(f"{Fore.CYAN}[✓] Grab List Domain Success")

def choose():
    print(f"{Fore.RED}\n╭──>> {Fore.WHITE}Defacer.id {Fore.RED}Grabber")
    print(f"│  {Fore.YELLOW}Created by RehanHaxor")
    print(f"│────────────────────────────")
    print(f"│({Fore.YELLOW}1{Fore.RED}). => {Fore.WHITE}Grab From Archive")
    print(f"│({Fore.YELLOW}2{Fore.RED}). => {Fore.WHITE}Grab From Onhold")
    print(f"│({Fore.YELLOW}3{Fore.RED}). => {Fore.WHITE}Grab From Special")
    print(f"│({Fore.YELLOW}4{Fore.RED}). => {Fore.WHITE}Grab From Team")
    print(f"│({Fore.YELLOW}5{Fore.RED}). => {Fore.WHITE}Grab From Attacker/Defacer")
    print(f"│({Fore.YELLOW}0{Fore.RED}). => {Fore.WHITE}Exit")
    print(f"╰────────────────────────────")
    
    choice = input(f"{Fore.YELLOW}[ pilih menu ]~# ")
    
    if choice == '1':
        url = 'https://defacer.id/archive'
        get_page(url)
    elif choice == '2':
        url = 'https://defacer.id/onhold'
        get_page(url)
    elif choice == '3':
        url = 'https://defacer.id/special'
        get_page(url)
    elif choice == '4':
        team_name = input('Team Name: ').replace(' ', '%20')
        url = f"https://defacer.id/archive/team/{team_name}"
        get_page(url)
    elif choice == '5':
        attacker_name = input('Name Attacker/Defacer: ').replace(' ', '%20')
        url = f"https://defacer.id/archive/attacker/{attacker_name}"
        get_page(url)
    elif choice == '0':
        print(f"{Fore.CYAN}Exiting...")
        return False
    else:
        print(f"{Fore.RED}Choose 1-5!!")
    return True

if __name__ == "__main__":
    while choose():
        print(f"{Fore.CYAN}\nReturning to main menu...\n")
