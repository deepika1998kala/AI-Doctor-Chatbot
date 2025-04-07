
# This Python script automates the creation of a predefined set of files and their necessary directories for a project. 
import os
from pathlib import Path
import logging

# It begins by setting up a logging configuration to provide informative messages throughout the process. 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# The list_of_files contains paths of files to be created. 

list_of_files =[
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# The script iterates over each file path, splitting it into the directory and filename components. 
# If the directory does not exist, it is created using os.makedirs(), ensuring that any intermediate directories are also created. 
# Next, the script checks if the file already exists and whether it has content by verifying its size with os.path.getsize(). 
# If the file doesn't exist or is empty, it is created as an empty file. 

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")

# Throughout these operations, the script logs informative messages about the actions being performed, such as creating directories and files, or noting if a file already exists.
