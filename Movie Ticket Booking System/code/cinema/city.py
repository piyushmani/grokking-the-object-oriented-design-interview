from dataclasses import dataclass
from typing import List
from .cinema import Cinema

@dataclass
class City:
    name: str
    cinemas: List[Cinema]

    def get_cinemas_showing_movie(self, movie_title: str) -> List[Cinema]:
        return [cinema for cinema in self.cinemas if any(movie.title.lower() == movie_title.lower() for movie in cinema.movies)]
