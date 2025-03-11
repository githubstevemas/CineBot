import json
from datetime import datetime

from preprocessing.ask_question import ask_question
from preprocessing.extract_data import extract_data_from_url
from preprocessing.save_data import save_json


def main():

    while True:

        print("\n[1] scrap")
        print("[2] ask")
        print("[0] quit\n")
        choice = input("Your choice ? ")

        if int(choice) == 1:

            print("Running scrap...")

            today_date = datetime.today().strftime('%Y-%m-%d')
            url = (f"https://www.allocine.fr/seance/"
                   f"salle_gen_csalle=P0057.html#shwt_date={today_date}")

            data = extract_data_from_url(url)
            save_json(data)

        if int(choice) == 2:

            try:
                with open('data/movie_data.json', 'r',
                          encoding='utf-8') as file:
                    movies = json.load(file)

                print("Running ask...")
                ask_question()

            except Exception as e:
                print("Data not found")

        if int(choice) == 3:

            print("Bye...")
            break


main()
