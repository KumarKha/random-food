from bs4 import BeautifulSoup

from utils import fetch_menu, load_from_firestore, save_to_firestore


def parse_mcdonalds_data():
    mcdonalds_url = 'https://www.mcdonalds.com/us/en-us/full-menu.html'
    res = fetch_menu(mcdonalds_url,"Mcdonalds")
    soup = BeautifulSoup(res.content, "html.parser")
        
    full_menu= soup.find("div",class_="menu-categories")
    menu_titles = [title.text.strip() for title in full_menu.find_all("div", class_="cmp-title")]

    # menu_items = full_menu.find_all("ul", class_="cmp-category__row")
    menu_items = [[item.text.strip() 
        for item in row.find_all("li")] 
        for row in full_menu.find_all("ul", class_="cmp-category__row")]
    
    
                 
    menu_data = dict(zip(menu_titles,menu_items))
    # menu_items = [{"name" : item} for category in menu_data.values() for item in category]
    save_to_firestore("menus","mcdonalds",menu_data)
    return menu_data
    
def parse_wendys_data():
    url = 'https://api.app.prd.wendys.digital/web-client-gateway/menu/getSiteMenu?lang=en&cntry=US&sourceCode=ORDER.WENDYS&version=24.12.4&siteNum=0&menuChannel=WEB_GUEST'
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = fetch_menu(url,"wendys", headers=headers)
    complete_menu = res.json()
    parsed_menu = {}
    
    sub_menus = complete_menu["menuLists"]["subMenus"]
    
    # saving the category with the item ids 
    for category in sub_menus:
        parsed_menu.update({category["name"]:category["menuItems"]})
    
    menu_items = complete_menu["menuLists"]["menuItems"]
    item_by_id = {item["menuItemId"]:item for item in menu_items}
    
    for category, ids in parsed_menu.items():
        detailed_items = [] # Temp list to store the full item 
        for item_id in ids: 
            if item_id in item_by_id: # Check if item has an id to replace
                detailed_items.append(item_by_id[item_id]) # Save the full item to the list
        parsed_menu[category] = detailed_items # Replace Id with full item
    
        
    save_to_firestore("menus","wendys",parsed_menu)
    parsed_menu
# Need to get images for each item and make a json with the catrgory as key and item name and img as data
# Try to get Calories for each item
def mcdonalds_menu(force_refresh=False) -> dict:
    if not force_refresh:
        cached_data = load_from_firestore("menus","mcdonalds")
        if cached_data:
            print("Data Loaded from cache")
            return cached_data
    return parse_mcdonalds_data()

def wendys_menu(force_refresh=False):
    if not force_refresh:
        cached_data = load_from_firestore("menus","wendys")
        if cached_data:
            print("Data Loaded from cache")
            return cached_data
    
    return parse_wendys_data()
    
    
    



