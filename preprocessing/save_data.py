import json
import os


def save_json(movies_to_save):
    # Save json file with movie list

    if not os.path.exists("data"):
        os.makedirs("data")

    with open('data/movie_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(movies_to_save, json_file, ensure_ascii=False, indent=4)


def save_similiraty_results(user_genre,
                            matching_movies=False,
                            filename="data/results.txt"):

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"\n\nGenre choisi par l'utilisateur: {user_genre}\n")

        if matching_movies:
            for movie in matching_movies:
                title = movie["title"]
                genres = ", ".join(movie["genres"])
                file.write(f"{title} ({genres})\n")

        else:
            file.write("Aucun film ne correspond à votre demande.")
