import json
import os

from preprocessing.ask_question import ask_genre, ask_date, ask_movie_theater
from preprocessing.extract_data import extract_data_from_url
from preprocessing.save_data import save_movies_json, save_movie_theater


def main():

    while True:

        print("\n[1] scrap")
        print("[2] ask")
        print("[3] setup")
        print("[0] quit\n")
        choice = input("Your choice ? ")

        if int(choice) == 1:

            if not os.path.exists("data/movie_theater.json"):
                print("Json not found, you must setup before scrap")
                break

            date = ask_date()

            with open('data/movie_theater.json', 'r', encoding='utf-8') as file:
                movie_theater = json.load(file)

            url = f"https://www.allocine.fr/_/showtimes/theater-{movie_theater}/d-{date}/"

            print("Retrieving information...")

            data = extract_data_from_url(url)

            save_movies_json(data)

        elif int(choice) == 2:

            if not os.path.exists("data/movie_data.json"):
                print("Json not found, you must scrap before ask")
                break

            ask_genre()

        elif int(choice) == 3:

            choosen_theater = ask_movie_theater()
            save_movie_theater(choosen_theater)

        elif int(choice) == 0:

            print("Bye...")
            break


main()
