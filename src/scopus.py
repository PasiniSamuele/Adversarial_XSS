import os
import pandas as pd
import json
from dotenv import load_dotenv

from pyscopus import Scopus

load_dotenv()

scopus_key = os.environ.get("SCOPUS_KEY")

attack_list = ["'code completion'", "'code completing'", "'code generation'", "'code generating'", "'code recommender'", 
               "'code recommending'", "'code recommendation'"]
task_list = ["poison", "poisoning", "backdoor", "backdooring", "altering", "alteration", "trigger", "triggering"]
#attack_list = ["code"]
#task_list = ["generation"]
output_folder = "output_code_generation"
os.makedirs(output_folder, exist_ok=True)

all_outputs = os.path.join(output_folder, "all.csv")


attack = " OR ".join(attack_list)
task = " OR ".join(task_list)
query = f"TITLE-ABS-KEY({attack}) AND TITLE-ABS-KEY({task})"
print(query)

scopus = Scopus(scopus_key)

search_df = scopus.search(query, count=9999)

print(f"Found {len(search_df)} papers")

search_df.to_csv(all_outputs)
