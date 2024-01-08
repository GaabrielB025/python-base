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
    $ prefixcalc.py
    operação: sum
    n1: 20
    n2: 10
    30

O histórico será salvo em `prefixcalc.log`
"""
__version__ = '0.1.3'
__author__ = 'Gabriel'

import os
from datetime import datetime
import logging

# TODO: Função
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s l:%(lineno)d f:%(filename)s %(message)s',
)

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

while True:
    operation = input('operation: ').strip()
    try:
        n1 = float(input('n1: ').strip())
    except ValueError:
        logging.error('please only provide numbers')
        continue

    try:
        n2 = float(input('n2: ').strip())
    except ValueError:
        logging.error('please only provide numbers')
        continue

    if operation not in operations:
        logging.error('`%s` is not a valid operation', operation)
        print(f'You can choose one of these: {list(operations.keys())}')
        continue

    try:
        result = operations[operation](n1, n2)
    except ZeroDivisionError:
        logging.error("You can't divite by zero!")
        continue

    with open(filepath, 'a') as file_:
        file_.write(f'{current_time} - {user} - {operation} {n1} {n2} = {result}\n')

    print(f'The result is: {result:.1f}')

    if input('Press enter to continue or any key to out '):
        break
