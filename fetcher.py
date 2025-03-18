import requests


def fetch_menu(url: str,menu_type:str,**kwargs):
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