#!/bin/evn python3

'''duck-typed anonymous function'''

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns the first element of a list or None if the list is empty'''
    if lst:
        return lst[0]
    else:
        return None
