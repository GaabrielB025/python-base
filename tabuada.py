#!/usr/bin/env python3
"""Prints the table from 1 to 10."""
__version__ = '0.1.0'
__author__ = 'Gabriel'

for first_factor in range(1, 11):
    print(f'Table of {first_factor}:\n')
    for second_factor in range(1, 11):
        product = first_factor * second_factor
        print(f'{first_factor} X {second_factor} = {product}')
    print('-' * 15)
