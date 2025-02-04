from dataclasses import dataclass
from typing import List

@dataclass
class News:
    news_id: int
    title: str
    content: str
    publish_date: str
    author: str
    category: str

class NewsService:
    def __init__(self):
        self.news_list: List[News] = []

    def publish_news(self, news: News):
        self.news_list.append(news)

    def get_latest_news(self, category: str = None) -> List[News]:
        if category:
            return [news for news in self.news_list if news.category == category][-5:]
        return self.news_list[-5:]