'''
    I have a few text files which contains data, to be precise a workflow related data.
    Now, my target here is to clean those text files and then maybe use GPT-3.5 to generate finetuning data.
    As it is a workflow based data I need to create several possible paths in the workflow and then generate data.
'''

import os
import pandas as pd

base_path = os.path.join(os.getcwd(), 'data')

df = pd.DataFrame(columns=['title', 'description'])

for file in os.listdir(base_path):
    with open(os.path.join(base_path, file), 'r') as f:
        data = f.read()
        df = pd.concat([pd.DataFrame({'title': [file[:-4]], 'description': [data]}), df], ignore_index=True)
    os.remove(os.path.join(base_path, file))
df.to_csv(f'{base_path}/data.csv', index=False)
