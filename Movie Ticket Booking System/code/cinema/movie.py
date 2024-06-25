from dataclasses import dataclass
from typing import List
from .showtime import ShowTime

@dataclass
class Movie:
    title: str
    language: str
    genre: str
    release_date: str
    shows: List[ShowTime]

    def get_showtimes_in_city(self, city_name: str, cinemas: List["Cinema"]) -> List[ShowTime]:
        for cinema in cinemas:
            if cinema.city.lower() == city_name.lower() and self in cinema.movies:
                return self.shows
        return []
