import os
import json
import ollama

###########################################################################################
###################################### Configuration ######################################
###########################################################################################
start_at = 1

output_language='french'
# use {'instructions': 'instructions'} to replace current instructions
keys_map = {'instructions': 'instructions_fr'}

# aya 35b was the best model for french translation comparing to following ones : llam3 8b, llava1.1 8b, phi3 14b q6, stablelm2 12b
model_name = 'aya:35b-23-q3_K_M'

system_prompt = f'''You are an experienced translator specializing in fitness exercises.
Guidelines:
- Your task is to translate the provided English text into {output_language}.
- Provide a direct translation of the input text without adding any comments or notes.
- Ensure accuracy, clarity, and cultural relevance in your translations.
'''
prompts = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': 'One-Arm Kettlebell Row'},
        {'role': 'assistant', 'content': 'Tirage unilatéral à la Kettlebell'},
        {'role': 'user', 'content': 'Perform 3 sets of 12 reps of bicep curls with 10-pound dumbbells.'},
        {'role': 'assistant', 'content': 'Exécutez 3 séries de 12 répétitions de curls de biceps avec des haltères de 10 livres.'}
    ]
###########################################################################################


dest_dir = f'exercises_{output_language}'

def read_json_files():
    dataset = []
    # parse all json files
    for root, dirs, files in os.walk('exercises'):
        for file in files:
            if file.endswith('.json'):
                # open and read json file
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                    dataset.append({ 'filename': file, 'data': data})
    return dataset

def translate(text) -> str:
    print(text)
    messages = [
        *prompts,
        {'role': 'user', 'content': f'{text}'}
    ]
    output = ollama.chat(model_name, messages=messages)
    return output['message']['content']

##############################

dataset = read_json_files()

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

i = 0
for entry in dataset:
    i += 1
    if start_at > i:
        continue
    print(f'Translating element n°{i}/{len(dataset)}')
    translations = []
    filename = entry['filename']
    data = entry['data']
    for instruction in data['instructions']:
        res = translate(instruction)
        translations.append(res)
        print(res)
        print('')
        
    data[keys_map['instructions']] = translations
    
    dest_file_path = os.path.join(dest_dir, filename)
    with open(dest_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
