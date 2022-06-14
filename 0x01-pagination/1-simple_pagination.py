#!/usr/bin/env python3
'''implement a simple helper function to paginate a list'''

from typing import Union, Tuple
import csv
import math
from typing import List


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


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    '''return ta tuple of the size of start and end index'''
    if page == 0 and page_size:
        start = 0
        end = page_size
        return start, end
    elif page and page_size:
        start = (page - 1) * page_size
        end = page * page_size
        return start, end
    else:
        return None
