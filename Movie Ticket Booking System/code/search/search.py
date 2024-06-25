from typing import List
from cinema.movie import Movie
from cinema.cinema import Cinema

class Search:
    @staticmethod
    def search_movies(catalog: List[Movie], title: str = "", language: str = "", genre: str = "", release_date: str = "", city_name: str = "", cinemas: List[Cinema] = []) -> List[Movie]:
        filtered_movies = []
        for movie in catalog:
            if (not title or title.lower() in movie.title.lower()) and \
               (not language or language.lower() == movie.language.lower()) and \
               (not genre or genre.lower() == movie.genre.lower()) and \
               (not release_date or release_date.lower() == movie.release_date.lower()) and \
               (not city_name or any(cinema.city.lower() == city_name.lower() and movie in cinema.movies for cinema in cinemas)):
                filtered_movies.append(movie)
        return filtered_movies
