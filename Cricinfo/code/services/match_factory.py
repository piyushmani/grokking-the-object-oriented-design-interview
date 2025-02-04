
from ..models.match import OdiMatch, TestMatch, T20Match
from ..enums.match_type import MatchType

class MatchFactory:
    @staticmethod
    def create_match(match_type: MatchType, *args, **kwargs):
        if match_type == MatchType.ODI:
            return OdiMatch(*args, **kwargs)
        elif match_type == MatchType.TEST:
            return TestMatch(*args, **kwargs)
        elif match_type == MatchType.T20:
            return T20Match(*args, **kwargs)
        else:
            raise ValueError(f"Unknown match type: {match_type}")