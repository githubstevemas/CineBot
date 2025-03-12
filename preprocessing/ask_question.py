from datetime import datetime, timedelta

from preprocessing.find_similarity import find_movies_by_similarity


def ask_date():

    user_date = input("What day do you want to go to the cinema ? ")

    choosen_date = datetime.today().strftime('%Y-%m-%d')

    if user_date == "tomorrow":
        choosen_date = (datetime.today() +
                        timedelta(days=1)).strftime('%Y-%m-%d')

    return choosen_date


def ask_genre():

    while True:
        genre_choice = input("\nQuel genre de film cherchez-vous? ")

        matching_movies = find_movies_by_similarity(genre_choice)

        if matching_movies:
            print(f"\nFilms dans votre cinéma Pathé :")
            for movie in matching_movies:
                print(f"\n{movie['title']} [{movie['runtime']} - {movie['reviews']}]")
                for seances in movie['showtimes']:
                    print(f"  {seances['startsAt'][0:5]} ({seances['language']})")

            # save_similiraty_results(genre_choice, matching_movies)

        else:
            print("Aucun film ne correspond à votre demande.")
            # save_similiraty_results(genre_choice, matching_movies)

        another_query = input("\nVoulez-vous chercher un autre film? (y/n) ")
        if another_query.lower() != "y":
            break
