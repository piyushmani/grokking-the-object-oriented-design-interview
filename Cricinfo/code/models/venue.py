from dataclasses import dataclass

@dataclass
class Venue:
    venue_id: int
    name: str
    city: str
    country: str
    capacity: int
    hosted_matches: int

    def get_venue_info(self):
        return f"{self.name}, {self.city} - Capacity: {self.capacity}, Hosted Matches: {self.hosted_matches}"
