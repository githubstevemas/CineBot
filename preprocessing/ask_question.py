import json
from datetime import datetime, timedelta

from preprocessing.find_similarity import find_movies_by_similarity, \
    find_theater


def ask_movie_theater():

    user_town = input("\nWhat is your town ? ")

    choosen_town = ""
    towns_theaters = find_theater(user_town.strip().lower())

    if towns_theaters:

        theater_ref = input("\nType your cinema theater ref (P0057) : ").upper()

        for theater in towns_theaters:
            if theater_ref == theater['ref']:
                choosen_town = theater['name']
                print(theater['name'])

        choosen_theater = {
            "town": choosen_town,
            "cinema_ref": theater_ref
        }
        return choosen_theater


def ask_date():

    user_date = input("When do you want to go to the cinema ? ")

    choosen_date = datetime.today().strftime('%Y-%m-%d')

    if user_date == "tomorrow":
        choosen_date = (datetime.today() +
                        timedelta(days=1)).strftime('%Y-%m-%d')

    return choosen_date


def ask_genre():

    while True:
        genre_choice = input("\nWhat kind of movie are you looking for ? ")

        matching_movies, genre_found = find_movies_by_similarity(genre_choice)

        with open('data/movie_theater.json', 'r', encoding='utf-8') as file:
            theater = json.load(file)

        if matching_movies:
            print(f"\nFilms of the genre {genre_found} in your {theater['town']} cinema :")
            for movie in matching_movies:
                print(f"\n{movie['title']} [{movie['runtime']} - {movie['reviews']}]")
                for seances in movie['showtimes']:
                    print(f"  {seances['startsAt'][0:5]} ({seances['language']})")

        else:
            print("No movies match your request.")

        another_query = input("\nDo you want to search for another movie? (y/n) ")
        if another_query.lower() != "y":
            break
