#!/usr/bin/env python3

''' type-annotated function'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' return a tuple of key-value pair squared '''
    return k, v ** 2
