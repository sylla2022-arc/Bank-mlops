import os
from pathlib import Path

data_dir = Path("data")

# Crée le dossier data/ s'il n'existe pas
data_dir.mkdir(parents=True, exist_ok=True)

# URL du dataset
url = "https://archive.ics.uci.edu/static/public/222/data.csv"
file_path = data_dir / "bank.csv"
print(file_path)
