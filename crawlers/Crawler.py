"""Base class for all Crawlers."""
from abc import ABC
from typing import Dict

class Crawler(ABC):
    """Base class for all Crawlers.""" 
    def __init__(self, query, output_dir):
        """Initializes the Crawler and begins crawling."""
        raise NotImplemented
    
