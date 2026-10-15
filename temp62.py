import requests

url = "https://fr.wikipedia.org/w/api.php"

headers = {
    "User-Agent": "RandomWikiPage/1.0 (Python learning project)"
}

params = {
    "action": "query",
    "list": "random",
    "rnnamespace": 0,
    "rnlimit": 1,
    "format": "json"
}

try:
    response = requests.get(
        url,
        params=params,
        headers=headers,
        timeout=10
    )
    response.raise_for_status()

    data = response.json()
    page = data["query"]["random"][0]

    title = page["title"]
    link = f"https://fr.wikipedia.org/wiki/{requests.utils.quote(title.replace(' ', '_'))}"

    print(title)
    print(link)

    #webbrowser.open(link)

except requests.RequestException as e:
    print(f"Erreur HTTP : {e}")
except (ValueError, KeyError, IndexError) as e:
    print(f"Erreur lors de la lecture de la réponse : {e}")
    
params = {
    "action": "query",
    "prop": "extracts",
    "explaintext": 1,
    "titles": title,
    "redirects": 1,
    "format": "json",
    "formatversion": 2
}

response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)
response.raise_for_status()

data = response.json()

if "error" in data:
    print("Erreur API :", data["error"])
elif "pages" in data["query"]:
    page_data = data["query"]["pages"][0]

    if "extract" in page_data:
        print(page_data["extract"])
    else:
        print("Aucun contenu trouvé pour :", title)