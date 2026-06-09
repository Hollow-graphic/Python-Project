import requests

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, static_folder="")

def get_random_golden():
    # 1. Get random map (redirect)
    res = requests.get(
        "https://maddie480.ovh/celeste/random-map",
        allow_redirects=False
    )

    if not (300 <= res.status_code < 400):
        raise Exception(f"API down: {res.status_code} {res.text}")

    url = res.headers.get("Location")
    if not url:
        raise Exception("No redirect URL")

    # 2. Extract ID
    mod_id = url.split("/")[-1]

    # 3. Fetch GameBanana data
    gb_res = requests.get(
        f"https://gamebanana.com/apiv11/Mod/{mod_id}/ProfilePage"
    )

    if not gb_res.ok:
        raise Exception(f"GameBanana error: {gb_res.status_code}")

    data = gb_res.json()

    # 4. Extract info
    name = data["_sName"]

    authors = list({
        author["_sName"]
        for credit in data["_aCredits"]
        for author in credit["_aAuthors"]
    })

    images = data["_aPreviewMedia"]["_aImages"]
    thumbnail = (
        f"{images[0]['_sBaseUrl']}/{images[0]['_sFile']}"
        if images else None
    )

    return {
        "url": url,
        "name": name,
        "authors": authors,
        "thumbnail": thumbnail
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/random')
def random():
    try:
        result = get_random_golden()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/clear', methods=['POST'])
def clear():
    return jsonify({"message": "Level cleared!"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=24727)
