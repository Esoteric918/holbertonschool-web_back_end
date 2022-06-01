#!/bin/bash/python3

'''  type-annotated function make_multiplier that takes
a float multiplier as argument and
returns a function that multiplies a float by multiplier.'''

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' type-annotated function that takes a float multiplier as argument'''
    def multiplier_func(n: float) -> float:
        '''returns a float n multiplied by multiplier'''
        return n * multiplier
    return multiplier_func
    return lambda x: x * multiplier
