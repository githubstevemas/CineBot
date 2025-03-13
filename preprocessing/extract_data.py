import html
from datetime import datetime

import requests

from preprocessing.format_data import format_language


CURRENT_TIME = datetime.now().strftime("%H:%M")

HEADERS = {
    "accept": "*/*",
    "accept-language": "fr-FR,fr;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Brave\";v=\"134\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://www.allocine.fr/seance/salle_gen_csalle=P0057.html",
    "referrerPolicy": "strict-origin-when-cross-origin"
}

BODY = {
    "filters": []
}


def get_showtimes(local):

    showtime_list = []
    for hour in local:

        hour_starts = hour.get('startsAt')
        language = hour.get('tags')[0].split('.')[-1]
        hours = hour_starts.split('T')[-1]

        formated_language = format_language(language)

        if CURRENT_TIME < hours:
            showtime_list.append({
                'startsAt': hours,
                'language': formated_language
            })

    return showtime_list


def extract_data_from_url(url):
    # From url get movies data, return movies list

    response = requests.post(url, json=BODY, headers=HEADERS)

    films_list = []

    if response.status_code == 200:
        raw_json = response.json()

        films_data = raw_json.get('results', [])

        for film_entry in films_data:

            film = film_entry.get('movie', {})

            title = html.unescape(film.get('title', 'NA'))
            synopsis = html.unescape(film.get('synopsis', 'NA'))

            reviews = 'NA'
            if film.get('stats').get('pressReview'):
                reviews = film.get('stats').get('pressReview').get('score') * 2

            showtimes = film_entry.get('showtimes', [])
            showtime_list = []

            if showtimes.get('local'):
                showtime_list = get_showtimes(showtimes.get('local'))

            if showtimes.get('original'):
                showtime_list = get_showtimes(showtimes.get('original'))

            if showtimes.get('dubbed'):
                showtime_list = get_showtimes(showtimes.get('dubbed'))

            film_details = {
                'title': title,
                'runtime': film.get('runtime', 'NA'),
                'countries': [
                    countries.get('name', 'NA') for countries in
                    film.get('countries', [])
                ],
                'synopsis': synopsis,
                'genres': [
                    genre.get('translate', '') for genre in
                    film.get('genres', [])
                ],
                'showtimes': showtime_list,
                'reviews': f"{reviews}/10"

            }
            films_list.append(film_details)

    else:
        print(f"Error {response.status_code}")

    return films_list
