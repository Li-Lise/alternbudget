import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("CX3_SERVER_URL")
USERNAME = os.getenv("CX3_USERNAME")
PASSWORD = os.getenv("CX3_PASSWORD")

url_auth = f"{SERVER}/webclient/api/Login/GetAccessToken"

body = {
    "SecurityCode": "",
    "Username": USERNAME,
    "Password": PASSWORD
}

reponse = requests.post(url_auth, json=body, timeout=10)
data = reponse.json()

if data["Status"] == "AuthSuccess":
    token = data["Token"]["access_token"]
    print("Connexion reussie ✅")
    print(f"Token recupere : {token[:20]}...")
else:
    print("Echec connexion ❌")
