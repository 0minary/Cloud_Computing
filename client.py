import requests

# L'URL de votre API FastAPI
api_url = "http://127.0.0.1:8000"

# Fonction pour consommer l'endpoint "/"
def consume_index():
    response = requests.get(f"{api_url}/")
    if response.status_code == 200:
        print(f"Réponse de l'API / : {response.text}")
    else:
        print(f"Erreur {response.status_code} lors de la requête sur /")

# Fonction pour consommer l'endpoint "/test"
def consume_test():
    response = requests.get(f"{api_url}/test")
    if response.status_code == 200:
        print(f"Réponse de l'API /test : {response.text}")
    else:
        print(f"Erreur {response.status_code} lors de la requête sur /test")

# Consommer les deux endpoints
if __name__ == "__main__":
    consume_index()
    consume_test()
