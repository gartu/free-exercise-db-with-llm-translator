import json
import uuid
import os
import hashlib
import shutil
import datetime
from PIL import Image

########################################## CONFIGURATION ############################################

author = 'admin'
# key is related to language_table variable
instructions_map = { 'English': 'instructions', 'French': 'instructions_fr'}
exercise_folder = './exercises/'
img_output = './media/exercise-images/'

# Initialize those id counters to MAX(id) of your current table
exercise_base_id = 1216
exercise_id = 2183
exercise_base_equipment_id = 276
exercise_base_muscle_id = 448
exercise_base_muscle_secondary_id = 449
exercise_image_id = 1
easy_thumbnails_source_id = 1
easy_thumbnails_thumbnail_id = 1
historicalexercise_id = 6
historicalexercisebase_id = 2
historicalexerciseimage_id = 1

#####################################################################################################


timestamp = f'{datetime.datetime.now().isoformat()}+00'.replace('T', ' ')

# Generate the SQL insert statements
sql_statements = []
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (11, $$Cable$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (12, $$Bands$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (13, $$Machine$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (14, $$Other$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (15, $$EZ curl bar$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (16, $$Foam roll$$);")
sql_statements.append("INSERT INTO public.exercises_equipment (id, name) VALUES (17, $$Medicine ball$$);")

equipment_table = {
    "cable": 11,
    "bands": 12,
    "body only": 7,  # "none (bodyweight exercise)"
    "machine": 13,
    "dumbbell": 3,  # "Dumbbell"
    "other": 14,
    "e-z curl bar": 15,
    "barbell": 1,  # "Barbell"
    "kettlebells": 10,  # "Kettlebell"
    "foam roll": 16,
    "medicine ball": 17,
    "exercise ball": 5,  # "Swiss Ball"
    "None": 7,  # "none (bodyweight exercise)"
}

muscle_table = {
    "abdominals": 6,  # Rectus abdominis
    "abductors": 11,  # Biceps femoris
    "adductors": 11,  # Biceps femoris
    "biceps": 1,  # Biceps brachii
    "calves": 7,  # Gastrocnemius
    "chest": 4,  # Pectoralis major
    "forearms": 13,  # Brachialis
    "glutes": 8,  # Gluteus maximus
    "hamstrings": 11,  # Biceps femoris
    "lats": 12,  # Latissimus dorsi
    "lower back": 16,  # Erector spinae
    "middle back": 9,  # Trapezius
    "neck": 9,  # Trapezius
    "quadriceps": 10,  # Quadriceps femoris
    "shoulders": 2,  # Anterior deltoid
    "traps": 9,  # Trapezius
    "triceps": 5,  # Triceps brachii
}

category_table = {
    "Arms": 8,
    "Legs": 9,
    "Abs": 10,
    "Chest": 11,
    "Back": 12,
    "Shoulders": 13,
    "Calves": 14,
    "Cardio": 15,
}

muscle_to_category = {
    "abdominals": "Abs",
    "abductors": "Legs",
    "adductors": "Legs",
    "biceps": "Arms",
    "calves": "Calves",
    "chest": "Chest",
    "forearms": "Arms",
    "glutes": "Legs",
    "hamstrings": "Legs",
    "lats": "Back",
    "lower back": "Back",
    "middle back": "Back",
    "neck": "Back",
    "quadriceps": "Legs",
    "shoulders": "Shoulders",
    "traps": "Back",
    "triceps": "Arms",
}

language_table = {
    "German": 1,
    "English": 2,
    "Bulgarian": 3,
    "Spanish": 4,
    "Russian": 5,
    "Dutch": 6,
    "Portuguese": 7,
    "Greek": 8,
    "Czech": 9,
    "Swedish": 10,
    "Norwegian": 11,
    "French": 12,
    "Italian": 13,
    "Polish": 14,
    "Ukrainian": 15,
    "Turkish": 16,
    "Arabic": 17,
    "Azerbaijani": 18,
    "Esperanto": 19,
    "Persian": 20,
}

def generate_md5(file_path):
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

for filename in os.listdir(exercise_folder):
    if not filename.endswith('.json'):
        continue
    
    with open(exercise_folder + filename) as f:
        data = json.load(f)

        exercise_base_id = exercise_base_id + 1
        exercise_base_equipment_id = exercise_base_equipment_id + 1
        exercise_image_id = exercise_image_id + 1
        easy_thumbnails_source_id = easy_thumbnails_source_id + 1
        easy_thumbnails_thumbnail_id = easy_thumbnails_thumbnail_id + 1
        historicalexercisebase_id = historicalexercisebase_id + 1
        historicalexerciseimage_id = historicalexerciseimage_id + 1
        
        # olympic weightlifting
        # cardio
        # strongman
        # plyometrics
        # strength
        # stretching
        # powerlifting
        category_id = category_table["Cardio"] if data['category'] == 'cardio' else category_table[muscle_to_category[data['primaryMuscles'][0]]]
        
        # exercises_exercisebase
        exercise_base_uuid = uuid.uuid4()
        sql_statements.append(f"INSERT INTO public.exercises_exercisebase (id, license_author, category_id, license_id, variations_id, uuid, last_update, license_author_url, license_derivative_source_url, license_object_url, license_title, created) VALUES ({exercise_base_id}, $${author}$$, {category_id}, 2, NULL, $${exercise_base_uuid}$$, $${timestamp}$$, $$$$, $$$$, $$$$, $$$$, $${timestamp}$$);")

        # exercises_historicalexercisebase
        sql_statements.append(f"INSERT INTO public.exercises_historicalexercisebase (id, license_author, uuid, created, history_id, history_date, history_change_reason, history_type, category_id, history_user_id, license_id, variations_id, license_author_url, license_derivative_source_url, license_object_url, license_title, last_update) VALUES ({exercise_base_id}, $${author}$$, $${exercise_base_uuid}$$, $${timestamp}$$, {historicalexercisebase_id}, $${timestamp}$$, NULL, $$+$$, {category_id}, 1, 2, NULL, $$$$, $$$$, $$$$, $$$$, $${timestamp}$$);")
        
        for language, instruction_key in instructions_map.items():
            # exercises_exercise
            exercise_id = exercise_id + 1
            exercise_uuid = uuid.uuid4()
            language_id = language_table[language]
            description = '<br/>'.join(data[instruction_key])
            sql_statements.append(f"INSERT INTO public.exercises_exercise (id, license_author, description, name, language_id, license_id, uuid, exercise_base_id, last_update, license_author_url, license_derivative_source_url, license_object_url, license_title, created) VALUES ({exercise_id}, $${author}$$, $${description}$$, $${data['name']}$$, {language_id}, 2, $${exercise_uuid}$$, {exercise_base_id}, $${timestamp}$$, $$$$, $$$$, $$$$, $$$$, $${timestamp}$$);")
            
            # exercises_historicalexercise
            historicalexercise_id = historicalexercise_id + 1
            sql_statements.append(f"INSERT INTO public.exercises_historicalexercise (id, license_author, description, name, created, uuid, history_id, history_date, history_change_reason, history_type, exercise_base_id, history_user_id, language_id, license_id, license_author_url, license_derivative_source_url, license_object_url, license_title, last_update) VALUES ({exercise_id}, $${author}$$, $${description}$$, $${data['name']}$$, $${timestamp}$$, $${exercise_uuid}$$, {historicalexercise_id}, $${timestamp}$$, NULL, $$+$$, {exercise_base_id}, 1, {language_id}, 2, $$$$, $$$$, $$$$, $$$$, $${timestamp}$$);")


        # exercises_exercisebase_equipment
        equipment = data['equipment']
        if equipment is None:
            equipment = 'None'
        sql_statements.append(f"INSERT INTO public.exercises_exercisebase_equipment (id, exercisebase_id, equipment_id) VALUES ({exercise_base_equipment_id}, {exercise_base_id}, {equipment_table[equipment]});")

        # exercises_exercisebase_muscles
        for muscle in data['primaryMuscles']:
            exercise_base_muscle_id = exercise_base_muscle_id + 1
            sql_statements.append(f"INSERT INTO public.exercises_exercisebase_muscles (id, exercisebase_id, muscle_id) VALUES ({exercise_base_muscle_id}, {exercise_base_id}, {muscle_table[muscle]});")

        # exercises_exercisebase_muscles_secondary
        for muscle in data['secondaryMuscles']:
            exercise_base_muscle_secondary_id = exercise_base_muscle_secondary_id + 1
            sql_statements.append(f"INSERT INTO public.exercises_exercisebase_muscles_secondary (id, exercisebase_id, muscle_id) VALUES ({exercise_base_muscle_secondary_id}, {exercise_base_id}, {muscle_table[muscle]});")

        exercise_image_uuid = uuid.uuid4()
        img_folder = data['images'][0].split("/")[0]
        webp = f'{exercise_folder}{img_folder}/exercise.webp'
        md5 = generate_md5(webp)

        # Open the webp image
        img = Image.open(webp)

        # Resize the image to 30x30 pixels
        img.thumbnail((30, 30))

        thumbnail = webp.replace('exercise.webp', 'thumbnail.webp')
        # Save the thumbnail with quality 85
        img.save(thumbnail, quality=85, optimize=True)
        md5_thumbnail = generate_md5(thumbnail)
        
        dst_dir = os.path.join(img_output, f'{exercise_base_id}')
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
    
        shutil.copy(webp, os.path.join(dst_dir, f'{exercise_image_uuid}.webp'))
        shutil.copy(thumbnail, os.path.join(dst_dir, f'{exercise_image_uuid}.webp.30x30_q85_crop-smart.webp'))
        
        sql_statements.append(f"INSERT INTO public.exercises_exerciseimage (id, license_author, image, is_main, exercise_base_id, license_id, uuid, style, license_author_url, license_derivative_source_url, license_object_url, license_title, created, last_update) VALUES ({exercise_image_id}, $$yuhonas$$, $$exercise-images/{exercise_base_id}/{exercise_image_uuid}.webp$$, true, {exercise_base_id}, 2, $${exercise_image_uuid}$$, $$4$$, $$https://github.com/yuhonas$$, $$https://github.com/yuhonas/free-exercise-db$$, $$https://github.com/gartu/free-exercise-db-with-llm-translator$$, $${data['name']}$$, $${timestamp}$$, $${timestamp}$$);")
        sql_statements.append(f"INSERT INTO public.exercises_historicalexerciseimage (id, license_author, uuid, image, is_main, style, history_id, history_date, history_change_reason, history_type, exercise_base_id, history_user_id, license_id, license_author_url, license_derivative_source_url, license_object_url, license_title, created, last_update) VALUES ({exercise_image_id}, $${author}$$, $${exercise_image_uuid}$$, $$exercise-images/{exercise_base_id}/{exercise_image_uuid}.webp$$, true, $$4$$, {historicalexerciseimage_id}, $${timestamp}$$, NULL, $$+$$, {exercise_base_id}, 1, 2, $$https://github.com/yuhonas$$, $$https://github.com/yuhonas/free-exercise-db$$, $$https://github.com/gartu/free-exercise-db-with-llm-translator$$, $${data['name']}$$, $${timestamp}$$, $${timestamp}$$);")
        sql_statements.append(f"INSERT INTO public.easy_thumbnails_source (id, storage_hash, name, modified) VALUES ({easy_thumbnails_source_id}, $${md5}$$, $$exercise-images/{exercise_base_id}/{exercise_image_uuid}.webp$$, $${timestamp}$$);")
        sql_statements.append(f"INSERT INTO public.easy_thumbnails_thumbnail (id, storage_hash, name, modified, source_id) VALUES ({easy_thumbnails_thumbnail_id}, $${md5_thumbnail}$$, $$exercise-images/{exercise_base_id}/{exercise_image_uuid}.webp.30x30_q85_crop-smart.webp$$, $${timestamp}$$, {easy_thumbnails_source_id});")
        
sql_statements.append("SELECT pg_catalog.setval($$public.easy_thumbnails_source_id_seq$$, (SELECT MAX(id) FROM easy_thumbnails_source), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.easy_thumbnails_thumbnail_id_seq$$, (SELECT MAX(id) FROM easy_thumbnails_thumbnail), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exercise_id_seq$$, (SELECT MAX(id) FROM exercises_exercise), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exercisebase_equipment_id_seq$$, (SELECT MAX(id) FROM exercises_exercisebase_equipment), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exercisebase_id_seq$$, (SELECT MAX(id) FROM exercises_exercisebase), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exercisebase_muscles_id_seq$$, (SELECT MAX(id) FROM exercises_exercisebase_muscles), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exercisebase_muscles_secondary_id_seq$$, (SELECT MAX(id) FROM exercises_exercisebase_muscles_secondary), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_exerciseimage_id_seq$$, (SELECT MAX(id) FROM exercises_exerciseimage), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_historicalexercise_history_id_seq$$, (SELECT MAX(id) FROM exercises_historicalexercise), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_historicalexercisebase_history_id_seq$$, (SELECT MAX(id) FROM exercises_historicalexercisebase), true);")
sql_statements.append("SELECT pg_catalog.setval($$public.exercises_historicalexerciseimage_history_id_seq$$, (SELECT MAX(id) FROM exercises_historicalexerciseimage), true);")


with open('output.sql', 'w') as f:
    for statement in sql_statements:
        f.write(statement + '\n')