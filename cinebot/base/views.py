import json
from datetime import datetime, timedelta
from django.shortcuts import render

from preprocessing.find_similarity import find_movies_by_similarity


def index(request):

    choosen_date = None
    matching_movies = []
    genre_found = None

    with open('../data/movie_theater.json', 'r', encoding='utf-8') as file:
        theater = json.load(file)

    if request.method == "POST":
        user_date = request.POST.get("user_date", "").lower()
        user_genre = request.POST.get("user_genre", "").lower()

        choosen_date = datetime.today().strftime('%Y-%m-%d')
        if user_date == "tomorrow":
            choosen_date = (datetime.today() + timedelta(days=1)).strftime(
                '%Y-%m-%d')

        if user_genre:
            matching_movies, genre_found = find_movies_by_similarity(
                user_genre)

    return render(
        request,
        "home.html",
        {"choosen_date": choosen_date, "matching_movies": matching_movies,
         "genre_found": genre_found, "town": theater['town']}
    )
