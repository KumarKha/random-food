from bs4 import BeautifulSoup
import json

from fetcher import fetch_menu

def parse_mcdonalds_menu() -> dict:
    
    mcdonalds_url = 'https://www.mcdonalds.com/us/en-us/full-menu.html'

    
    res = fetch_menu(mcdonalds_url,"Mcdonalds")
    soup = BeautifulSoup(res.content, "html.parser")
        
    full_menu= soup.find("div",class_="menu-categories")
    menu_titles = [title.text.strip() for title in full_menu.find_all("div", class_="cmp-title")]

    # menu_items = full_menu.find_all("ul", class_="cmp-category__row")
    menu_items = [[item.text.strip() for item in row.find_all("li")] for row in full_menu.find_all("ul", class_="cmp-category__row")]

    return dict(zip(menu_titles,menu_items))



def parse_wendys_menu():
    url = 'https://api.app.prd.wendys.digital/web-client-gateway/menu/getSiteMenu?lang=en&cntry=US&sourceCode=ORDER.WENDYS&version=24.12.4&siteNum=0&menuChannel=WEB_GUEST'
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = fetch_menu(url,"wendys", headers=headers)
    menu = res.json()
    save_json(menu,"wendys.json")
    return menu





def save_json(data: dict, filename: str):
    """Save the JSON to a file"""
    try: 
        with open(filename,"w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error saving JSON {e}")
        

