from datetime import datetime

from preprocessing.extract_data import extract_data_from_url
from preprocessing.save_json_data import save_json


def main():

    today_date = datetime.today().strftime('%Y-%m-%d')
    url = f"https://www.allocine.fr/seance/salle_gen_csalle=P0057.html#shwt_date={today_date}"

    data = extract_data_from_url(url)
    save_json(data)


if __name__ == "__main__":
    main()
