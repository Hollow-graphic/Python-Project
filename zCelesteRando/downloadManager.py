import re
import requests
import json
import os

def get_allowed_fields(item_type="Mod"):
    url = f"http://api.gamebanana.com/Core/Item/Data/AllowedFields?itemtype={item_type}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def download_first_zip(mod_url):
    # Extraire l'ID du mod
    match = re.search(r'/mods/(\d+)', mod_url)
    if not match:
        raise ValueError("URL invalide")
    mod_id = match.group(1)

    # Récupérer les champs valides
    fields = get_allowed_fields("Mod")

    # Récupérer les données du mod
    api_url = "http://api.gamebanana.com/Core/Item/Data"
    params = {
        "itemtype": "Mod",
        "itemid": mod_id,
        "fields": ",".join(fields)
    }
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()

    # Créer le dossier si nécessaire
    os.makedirs("gamebanana", exist_ok=True)

    # Sauvegarder le JSON complet
    with open("gamebanana/response.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    # Chercher les fichiers dans le JSON
    files_dict = None
    for entry in data:
        if isinstance(entry, dict) and all(isinstance(v, dict) for v in entry.values()):
            files_dict = entry
            break

    if not files_dict:
        return None  # aucun fichier trouvé

    # Télécharger le premier .zip trouvé
    for file_id, file_data in files_dict.items():
        if isinstance(file_data, dict) and file_data.get("_sFile", "").endswith(".zip"):
            zip_url = file_data["_sDownloadUrl"]
            zip_name = os.path.join("gamebanana", file_data["_sFile"])
            
            r = requests.get(zip_url)
            r.raise_for_status()
            with open(zip_name, "wb") as f_zip:
                f_zip.write(r.content)
            
            return zip_name

    return None  # aucun .zip trouvé

# Exemple d'utilisation
mod_url = "https://gamebanana.com/mods/592773"
zip_file = download_first_zip(mod_url)
