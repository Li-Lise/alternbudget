import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

print("Clé chargée :", api_key)
print("Elle n'est pas écrite dans le code — elle vient du fichier .env ✅")
