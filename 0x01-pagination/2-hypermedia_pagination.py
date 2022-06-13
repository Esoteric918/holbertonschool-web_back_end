#!/usr/bin/env python3
'''implement a simple helper function to paginate a list'''

from typing import Dict, Union, Tuple
import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''use assert to verify the page and page_size are valid'''
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''returns a dictionary containing the following key-value pairs'''
        return {
            'page_size': page_size,
            'page': page if page > 0 else 1,
            'data':  self.get_page(page, page_size),
            'next_page': (page + 1) if page < math.ceil(len(self.dataset()) / page_size) else None,
            'prev_page': (page - 1) if page > 1 else None,
            'total_pages':  math.ceil(len(self.dataset()) / page_size),
    }


