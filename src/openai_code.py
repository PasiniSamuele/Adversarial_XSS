import os, sys, json
import openai
#from llm_api import *
from dotenv import load_dotenv

load_dotenv()


openai.organization = os.environ.get("OPENAI_ORGANIZATION")
openai.api_key = os.environ.get("OPENAI_API_KEY")


N_repeat = 10
pnum = sys.argv[1]
llm_model = sys.argv[2]
temperature = float(sys.argv[3])
 
output_dir = f"./prompt_v1_results/output/{llm_model}/{pnum}/{temperature}"
os.makedirs(output_dir, exist_ok=True)
 
if llm_model == "gpt-3.5-turbo" or llm_model == "gpt-4":
    mode = "chat"
elif llm_model in ["text-davinci-003"]:
    mode = "completion"
 
with open("./prompts/task_types.json", "r") as f:
    task_types = json.load(f)
 
if pnum not in task_types:
    print("Invalid pnum")
    exit()
 
task = task_types[pnum]["task"]
dataset = task_types[pnum]["dataset"]
goal = task_types[pnum]["goal"]
 
with open(f"./prompts/code/{pnum}.txt", "r") as f:
    code = f.read()
 
if temperature == 0.0:
    N_repeat = 1
   
for i in range(N_repeat):      
    output_file_path = os.path.join(output_dir, f"{pnum}_{i}.txt")
    if os.path.exists(output_file_path):
        continue
   
    prompt =  f'''The following code is designed for a {task} trained on {dataset}. Please repair it in order to {goal}. The code repair consists of replacing one or more of the hyperparameters with an alternative value, currently represented in a "config" dictionary, in the form of  config["PARAM"] . Please only show me config values in a json format so that I can save it directly in a json file format. Give me only one solution.
Code:
{code}
    '''
    print(i)
    if mode == "chat":
        chat_completion = openai.ChatCompletion.create(
            model=llm_model,       
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}]
        )
        output = chat_completion.choices[0].message.content
    elif mode == "completion":
        completion = openai.Completion.create(
            model=llm_model,
            prompt=prompt,
            max_tokens=1000,
            temperature=temperature
        )
        output = completion.choices[0].text
 
   
    print(output)
    with open(output_file_path, "w") as f:
        f.write(output) 