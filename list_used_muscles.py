import os
import json

muscles = set()
equipment_list = set()
category_list = set()
ex_with_other_equipment = set()

for filename in os.listdir('./exercises/'):
    if filename.endswith('.json'):
        with open(os.path.join('./exercises/', filename), 'r') as f:
            data = json.load(f)
            muscles.update(data.get('primaryMuscles', []))
            muscles.update(data.get('secondaryMuscles', []))
            equipment_list.add(data['equipment'])
            category_list.add(data['category'])
            if data['equipment'] == 'other':
                ex_with_other_equipment.add(data['name'])

print("\nMuscles:")
for muscle in sorted(muscles):
    print(muscle)
    
print("\nListe des équipements distincts :")
for equipment in equipment_list:
    print(equipment)
    
    
print("\nListe des catégories distincts :")
for category in category_list:
    print(category)
    
print("\nListe des exo avec équipment other :")
for n in ex_with_other_equipment:
    print(n)
    
