import os
import requests
from pathlib import Path

# Crée le dossier data/ s'il n'existe pas
data_dir = Path("data")
data_dir.mkdir(parents=True, exist_ok=True)

# URL du dataset
url = "https://archive.ics.uci.edu/static/public/222/data.csv"
file_path = data_dir / "bank.csv"

# Téléchargement si le fichier n'existe pas déjà
if not file_path.exists():
    print(f"Téléchargement en cours depuis {url}...")
    response = requests.get(url)
    if response.status_code == 200:
        file_path.write_bytes(response.content)
        print(f"✅ Données enregistrées dans {file_path}")
    else:
        print(f"❌ Échec du téléchargement : {response.status_code}")
else:
    print(f"📁 Le fichier existe déjà : {file_path}")
