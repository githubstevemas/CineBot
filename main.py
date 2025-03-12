import json

from preprocessing.ask_question import ask_genre, ask_date
from preprocessing.extract_data import extract_data_from_url
from preprocessing.save_data import save_json


def main():

    while True:

        print("\n[1] scrap")
        print("[2] ask")
        print("[0] quit\n")
        choice = input("Your choice ? ")

        if int(choice) == 1:

            date = ask_date()

            url = f"https://www.allocine.fr/_/showtimes/theater-P0057/d-{date}/"

            print("Running scrap...")

            data = extract_data_from_url(url)

            save_json(data)

        elif int(choice) == 2:

            try:
                with open('data/movie_data.json', 'r',
                          encoding='utf-8') as file:
                    movies = json.load(file)

                print("Running ask...")
                ask_genre()

            except Exception as e:
                print("Data not found")

        elif int(choice) == 3:

            print("Bye...")
            break


main()
