import json

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')


def find_movies_by_similarity(user_input):

    similarity_threshold = 0.6  # Change for better results

    with open('data/movie_data.json', 'r', encoding='utf-8') as file:
        movies = json.load(file)

    movies_with_scores = []
    best_similarity = 0
    best_genre = ""

    embedding_term = model.encode(user_input.lower(), convert_to_tensor=True)

    for movie in movies:
        max_similarity = 0

        for genre in movie["genres"]:

            embedding_genre = model.encode(genre.lower(),
                                           convert_to_tensor=True)

            similarity = util.pytorch_cos_sim(embedding_term,
                                              embedding_genre)[0][0].item()

            if similarity > max_similarity:
                max_similarity = similarity
                # print(f"{genre} : {similarity}")

            if similarity > best_similarity:
                best_similarity = similarity
                best_genre = genre

        movies_with_scores.append((movie, max_similarity))

    movies_with_scores.sort(key=lambda x: x[1], reverse=True)

    top_movies = []
    for movie, score in movies_with_scores:
        if score >= similarity_threshold:
            top_movies.append(movie)
        if len(top_movies) >= 6:
            break

    return top_movies, best_genre
