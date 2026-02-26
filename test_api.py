import requests

url = "https://jsonplaceholder.typicode.com/users/1"

reponse = requests.get(url)

print("Code de réponse :", reponse.status_code)
print("Données reçues :", reponse.json())
