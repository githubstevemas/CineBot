import html
from datetime import datetime

import requests


def extract_data_from_url(url):
    # From url get movies data, return movies list

    headers = {
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

    body = {
        "filters": []
    }

    response = requests.post(url, json=body, headers=headers)

    films_list = []
    current_time = datetime.now().strftime("%H:%M")

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
                for hour in showtimes.get('local'):

                    hour_starts = hour.get('startsAt')
                    language = hour.get('tags')[0].split('.')[-1]
                    hours = hour_starts.split('T')[-1]

                    if language == "French":
                        language = "VF"
                    elif language == "Original":
                        language = "VO"
                    elif language == "DolbyCinema":
                        language = "Dolby"

                    if current_time < hours:
                        showtime_list.append({
                            'startsAt': hours,
                            'language': language
                        })

            if showtimes.get('original'):
                for hour in showtimes.get('original'):

                    hour_starts = hour.get('startsAt')
                    language = hour.get('tags')[0].split('.')[-1]
                    hours = hour_starts.split('T')[-1]

                    if language == "French":
                        language = "VF"
                    elif language == "Original":
                        language = "VO"
                    elif language == "DolbyCinema":
                        language = "Dolby"

                    if current_time < hours:
                        showtime_list.append({
                            'startsAt': hours,
                            'language': language
                        })

            if showtimes.get('dubbed'):
                for hour in showtimes.get('dubbed'):

                    hour_starts = hour.get('startsAt')
                    language = hour.get('tags')[0].split('.')[-1]

                    hours = hour_starts.split('T')[-1]

                    if language == "French":
                        language = "VF"
                    elif language == "Original":
                        language = "VO"
                    elif language == "DolbyCinema":
                        language = "Dolby"

                    if current_time < hours:
                        showtime_list.append({
                            'startsAt': hours,
                            'language': language
                        })

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
