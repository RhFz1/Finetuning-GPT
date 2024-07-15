'''
    I have a few text files which contains data, to be precise a workflow related data.
    Now, my target here is to clean those text files and then maybe use GPT-3.5 to generate finetuning data.
    As it is a workflow based data I need to create several possible paths in the workflow and then generate data.
'''

import os

# Initially converting the .md files to text files.
base_path = os.path.join(os.getcwd(), 'data', 'SymptomFiles')

for file in os.listdir(base_path):
    if file.endswith('.md'):
        with open(f'{base_path}/{file}', 'r', encoding='utf-8') as f:
            data = f.read()
        with open(f'{base_path}/{file[:-3]}.txt', 'w', encoding='utf-8') as f:
            f.write(data)
        os.remove(f'{base_path}/{file}')