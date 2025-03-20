
import firebase_admin
from firebase_admin import credentials, firestore

import requests
import json



cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_to_firestore(collection: str, document:str, data:dict):
    doc_ref =db.collection(collection).document(document)
    doc_ref.set(data)
    print(f"Data saved to Firestore: {collection}/{document}")
    
    
def load_from_firestore(collection: str, document:str)-> dict:
    doc_ref = db.collection(collection).document(document)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    return {}


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
    
    

def save_json(data: dict, filename: str):
    """Save the JSON to a file"""
    try: 
        with open(filename,"w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Successfully saved {filename}")
    except Exception as e:
        print(f"Error saving JSON {e}")
        
