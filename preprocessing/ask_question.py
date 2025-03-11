from preprocessing.find_similarity import find_movies_by_similarity


def ask_question():

    while True:
        genre_choice = input("\nQuel genre de film cherchez-vous? ")

        matching_movies = find_movies_by_similarity(genre_choice)

        if matching_movies:
            print("\nFilms dans votre cinéma Pathé aujourd'hui :\n")
            for movie in matching_movies:
                print(f" - {movie['title']} // Séances: {movie['hours']}")
            # save_similiraty_results(genre_choice, matching_movies)

        else:
            print("Aucun film ne correspond à votre demande.")
            # save_similiraty_results(genre_choice, matching_movies)

        another_query = input("\nVoulez-vous chercher un autre film? (y/n) ")
        if another_query.lower() != "y":
            break
