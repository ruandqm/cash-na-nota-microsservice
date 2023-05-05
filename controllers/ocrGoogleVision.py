import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

AUTH_KEY = os.getenv("AUTH_KEY")


def ocrGoogleVisionApi(image: str):
    url = url = f"https://vision.googleapis.com/v1/images:annotate?key={AUTH_KEY}"

    data = {
        "requests": [
            {
                "image": {"content": image},
                "features": [{"type": "TEXT_DETECTION"}],
            }
        ]
    }

    r = requests.post(url=url, data=json.dumps(data))

    if r.status_code != 200:
        print("Erro ao processar imagem. Código de status: ", r.status_code)
        return []

    response = r.json()

    if "responses" not in response:
        print("Não foi possível encontrar a chave 'responses' na resposta da API.")
        return []

    texts = response["responses"][0]["textAnnotations"]

    results = []

    for t in texts:
        results.append(t["description"])

    return results
