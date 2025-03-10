import json


def save_json(movies_to_save):
    # Save json file with movie list

    with open('data/movie_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(movies_to_save, json_file, ensure_ascii=False, indent=4)
