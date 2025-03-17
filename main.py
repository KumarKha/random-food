from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

import json

app = Flask(__name__)


def fetch_menu(url,menu_type,**kwargs):
    headers = kwargs.get('headers',None)
    try:
        if headers:
            res  = requests.get(url, headers=headers)
        else:
            res = requests.get(url)
        if res.status_code != 200:
            print(f"Error:Unable to Fetch {menu_type} Menu. Status Code: {res.status_code}")
            return None
        return res
    except requests.RequestException as e:
        print(f"Request error fetching { menu_type} menu: {e}")
        return None

def parse_mcdonalds_menu() -> dict:
    mcdonalds_url = 'https://www.mcdonalds.com/us/en-us/full-menu.html'

    
    res = fetch_menu(mcdonalds_url,"Mcdonalds")
    soup = BeautifulSoup(res.content, "html.parser")
        
    full_menu= soup.find("div",class_="menu-categories")
    menu_titles = [title.text.strip() for title in full_menu.find_all("div", class_="cmp-title")]

    # menu_items = full_menu.find_all("ul", class_="cmp-category__row")
    menu_items = [[item.text.strip() for item in row.find_all("li")] for row in full_menu.find_all("ul", class_="cmp-category__row")]

    return dict(zip(menu_titles,menu_items))
    
    

@app.route('/menu', methods =['GET'])
def get_menu():
    return jsonify(parse_mcdonalds_menu())



def fetch_wendys_menu():
    url = 'https://api.app.prd.wendys.digital/web-client-gateway/menu/getSiteMenu?lang=en&cntry=US&sourceCode=ORDER.WENDYS&version=24.12.4&siteNum=0&menuChannel=WEB_GUEST'
    
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    res = fetch_menu(url,"wendys", headers=headers)
    # menu_data = res.json()
    
    
    

    
        

@app.route('/wendys', methods = ['GET'])
def get_wendys():
    return fetch_wendys_menu()
if __name__ == '__main__':
    app.run(debug=True)

