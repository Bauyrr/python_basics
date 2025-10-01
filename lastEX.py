# movies.py
movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

def is_high_score(movie, threshold=5.5):
    """Возвращает True если imdb > threshold."""
    return movie.get("imdb", 0) > threshold

def high_score_movies(movie_list, threshold=5.5):
    """Возвращает список фильмов с imdb > threshold."""
    return [m for m in movie_list if m.get("imdb", 0) > threshold]

def movies_by_category(movie_list, category):
    """Возвращает список фильмов из category (регистронезависимо)."""
    return [m for m in movie_list if m.get("category", "").lower() == category.lower()]

def average_score(movie_list):
    """Средний IMDB по списку (0 если список пуст)."""
    if not movie_list:
        return 0.0
    return sum(m.get("imdb", 0) for m in movie_list) / len(movie_list)

def average_score_by_category(movie_list, category):
    """Средний IMDB по категории (0 если фильмов в категории нет)."""
    cat = movies_by_category(movie_list, category)
    return average_score(cat)