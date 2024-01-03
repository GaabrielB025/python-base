#!/usr/bin/env python3
"""Bloco de notas

$ notes.py write "Minha nota"
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read TAG
"""
__version__ = '0.1.0'

import os
import sys

HELP = """
$ notes.py [OPTION] [ARGS]

OPTIONS
    write TITLE         create e new note with name TITLE
    read TAG     read a note from a tag TAG
"""
arguments = sys.argv[1:]
path = os.curdir
filepath = os.path.join(path, 'notes.txt')

if not arguments:
    print('Error! You need to pass an argument!')
    print(HELP)
    sys.exit(1)
elif len(arguments) != 2:
    print('Invalid number of arguments!')
    print(HELP)
    sys.exit(1)

option, argument = arguments

if option not in ('write', 'read'):
    print(f'Invalid argument `{option}`')
    sys.exit(1)

if option == 'write':
    title = argument
    text = [
        f'{title}',
        input('tag: ').strip(),
        input('text:\n'),
    ]

    with open(filepath, 'a') as file_:
        file_.write('\t'.join(text) + '\n')

if option == 'read':
    for line in open(filepath):
        title, tag, text = line.split('\t')

        if tag.lower() == argument.lower():
            print(f'Title: {title}\nText: {text}')
            print('-' * 30)
    
