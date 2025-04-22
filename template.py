import os
from pathlib import Path
import logging
import sys

logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    encoding='utf-8',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


project_name = 'bank_mlops'

list_of_files = [".github/workflows/.gitkeep",
 f"src/{project_name}/__init__.py",
 f"src/{project_name}/preprocessing.py",
 f"src/{project_name}/train.py",
 f"src/{project_name}/evaluate.py",

"data"
"models",
"dvc.yaml",
"params.yaml",
"main.py",
"Dockerfile",
 ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, 'w') as file:
            file.write("")
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"File {filename} already exists: {filepath}")

        