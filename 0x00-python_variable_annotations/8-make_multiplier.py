#!/usr/bin/env python3

'''  type-annotated function'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' type-annotated function that takes a float multiplier as argument'''
    def multiplier_func(n: float) -> float:
        '''returns a float n multiplied by multiplier'''
        return n * multiplier
    return multiplier_func
