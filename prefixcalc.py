#!/usr/bin/env python3
"""Calculadora prefix

Funcionamento:

    [operação] [n1] [n2]

Operações:
    sum -> +
    sub -> -
    mul -> *
    div -> /

Uso:
    $ prefixcalc.py sum 5 2
    7

    $ prefixcalc.py mul 10 5
    50

    $ prefixcalc.py
    operação: sum
    n1: 20
    n2: 10
    30

O histórico será salvo em `prefixcalc.log`
"""
__version__ = '0.1.1'
__author__ = 'Gabriel'

import sys
import os
from datetime import datetime


current_time = datetime.now().ctime()
user = os.getenv('USER')
path = os.curdir
filepath = os.path.join(path, 'prefixcalc.log')

operations = {
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

valid_operations = ('sum', 'sub', 'mul', 'div')

arguments = sys.argv[1:]

# TODO: Exceptions
if not arguments:
    operation = input('operation: ').strip()
    n1 = input('n1: ').strip()
    n2 = input('n2: ').strip()
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print('Number of invalid arguments!')
    print('You can try: `sum 5 10`')
    sys.exit(1)

operation, *numbers = arguments

if operation not in operations:
    print(f'`{operation}` is not a valid operation')
    print(f'You can choose one of these: {valid_operations}')
    sys.exit(1)

validated_numbers = []
for num in numbers:
    # TODO: Repetição while + exceptions
    if not num.replace('.', '').isdigit():
        print(f'Invalid number `{num}`')
        sys.exit(1)

    if '.' in num:
        num = float(num)
    else:
        num = int(num)

    validated_numbers.append(num)

n1, n2 = validated_numbers
result = operations[operation](n1, n2)

with open(filepath, 'a') as file_:
    file_.write(f'{current_time} - {user} - {operation} {n1} {n2} = {result}\n')

print(f'The result is: {result:.1f}')
