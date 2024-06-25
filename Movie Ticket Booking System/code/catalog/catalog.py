from typing import List
from cinema.movie import Movie
from cinema.cinema import Cinema

class Catalog:
    def __init__(self):
        self.movies: List[Movie] = []
        self.cinemas: List[Cinema] = []

    def add_movie(self, movie: Movie):
        self.movies.append(movie)

    def remove_movie(self, movie: Movie):
        self.movies.remove(movie)

    def update_movie(self, movie: Movie):
        for i, m in enumerate(self.movies):
            if m.title == movie.title:
                self.movies[i] = movie

    def add_cinema(self, cinema: Cinema):
        self.cinemas.append(cinema)

    def get_cinemas_in_city(self, city_name: str) -> List[Cinema]:
        return [cinema for cinema in self.cinemas if cinema.city.lower() == city_name.lower()]
