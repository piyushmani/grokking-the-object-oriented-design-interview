from dataclasses import dataclass
from typing import List
from .hall import Hall
from .movie import Movie
from .showtime import ShowTime

@dataclass
class Cinema:
    name: str
    city: str
    halls: List[Hall]
    movies: List[Movie]

    def get_showtimes(self, movie_title: str) -> List[ShowTime]:
        for movie in self.movies:
            if movie.title.lower() == movie_title.lower():
                return movie.shows
        return []

