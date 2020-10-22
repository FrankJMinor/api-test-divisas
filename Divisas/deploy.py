# -*- coding: utf-8 -*-

# standar library
import pathlib
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
NAME_FUNCTION = os.path.basename(ROOT_DIR)
CLEAR_CACHE = f"""find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf"""

COMAND = f"gcloud functions deploy {NAME_FUNCTION} --entry-point handler --runtime python37 --trigger-http --allow-unauthenticated"
os.system(CLEAR_CACHE)
#os.system(COMAND)