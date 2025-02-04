from dataclasses import dataclass
from typing import List
from models.news import News

class NewsService:
    def __init__(self):
        self.news_list: List[News] = []

    def publish_news(self, news: News):
        self.news_list.append(news)

    def get_latest_news(self, category: str = None) -> List[News]:
        if category:
            return [n for n in self.news_list if n.category == category][-5:]
        return self.news_list[-5:]