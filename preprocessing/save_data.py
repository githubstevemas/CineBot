import json
import os


def save_json(movies_to_save):
    # Save json file with movie list

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/movie_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(movies_to_save, json_file, ensure_ascii=False, indent=4)
