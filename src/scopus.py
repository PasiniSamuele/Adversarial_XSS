import os
import pandas as pd
import json
from dotenv import load_dotenv

from pyscopus import Scopus

load_dotenv()

scopus_key = os.environ.get("SCOPUS_KEY")

attack_list = ["xss", "'cross site scripting'", "'cross-site scripting'"]
task_list = ["detection", "classification", "detector", "classifier", "sanitization", "sanitizer", "sanitizing", "detecting", "classifying"]

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

all_outputs = os.path.join(output_folder, "all_v2.csv")


attack = " OR ".join(attack_list)
task = " OR ".join(task_list)
query = f"TITLE-ABS-KEY({attack}) AND TITLE-ABS-KEY({task})"
print(query)

scopus = Scopus(scopus_key)

search_df = scopus.search(query, count=99999)

print(f"Found {len(search_df)} papers")

search_df.to_csv(all_outputs)
