import json
import os


def save_movie_theater(movie_theater):
    # Save json file with movie theater to use

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/movie_theater.json', 'w', encoding='utf-8') as json_file:
        json.dump(movie_theater, json_file)


def save_movies_json(movies_to_save):
    # Save json file with movie list

    if not os.path.exists("data"):
        os.makedirs("data")
    try:

        with open('../data/movie_data.json', 'w', encoding='utf-8') as json_file:
            json.dump(movies_to_save, json_file, ensure_ascii=False, indent=4)
        print("Writting json OK")

    except Exception as e:
        print(e)
