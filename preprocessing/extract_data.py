import requests
from bs4 import BeautifulSoup


def extract_data_from_url(url):
    # From url get movies data, return movies list

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    films = soup.find_all('div',
                          class_='card entity-card entity-card-list movie-card-theater cf hred')

    movies = []

    for film in films:
        title = film.find('h2', class_='meta-title').text.strip()

        genres = film.find_all(
            'span',
            class_=lambda class_name: class_name and class_name.endswith('w== dark-grey-link')
        )
        genres_text = []
        for genre in genres:
            genres_text.append(genre.text.strip())

        hours = film.find_all('span', class_='showtimes-hour-item-value')
        hours_text = []
        for hour in hours:
            hours_text.append(hour.text.strip())

        movie_data = {
            "title": title,
            "genres": genres_text,
            "hours": hours_text
        }

        movies.append(movie_data)

    return movies
