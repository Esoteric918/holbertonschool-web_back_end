#!/usr/bin/env python3
'''implement a simple helper function to paginate a list'''

from typing import Union, Tuple


def index_range(page: int, page_size: int) -> Union[Tuple[int, int], None]:
    '''return a tuple of the size of start and end index'''
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
