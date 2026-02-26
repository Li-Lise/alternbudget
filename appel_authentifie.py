import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = "https://jsonplaceholder.typicode.com/users/1"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

try:
    reponse = requests.get(url, headers=headers, timeout=5)
    reponse.raise_for_status()
    data = reponse.json()
    print("✅ Appel réussi")
    print(f"Nom du contact : {data['name']}")
    print(f"Téléphone : {data['phone']}")
    print(f"Entreprise : {data['company']['name']}")
except requests.exceptions.Timeout:
    print("🚨 ALERTE : Le serveur ne répond pas")
except requests.exceptions.HTTPError as e:
    print(f"❌ Erreur HTTP : {e}")
