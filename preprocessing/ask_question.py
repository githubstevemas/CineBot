from datetime import datetime, timedelta

from preprocessing.find_similarity import find_movies_by_similarity


def ask_movie_theater():

    user_choice = input("Which cinema do you want to use (ex : P0057)? ")
    return user_choice


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

        if matching_movies:
            print(f"\nFilms of the genre {genre_found} in your Pathé cinema :")
            for movie in matching_movies:
                print(f"\n{movie['title']} [{movie['runtime']} - {movie['reviews']}]")
                for seances in movie['showtimes']:
                    print(f"  {seances['startsAt'][0:5]} ({seances['language']})")

        else:
            print("No movies match your request.")

        another_query = input("\nDo you want to search for another movie? (y/n) ")
        if another_query.lower() != "y":
            break
