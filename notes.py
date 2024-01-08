#!/usr/bin/env python3
"""Bloco de notas

$ notes.py write
title: My title
tag: tech
text:
Anotação geral sobre carreira de tecnologia

$ notes.py read TAG
"""
__version__ = '0.1.1'

import os
import sys

HELP = """
$ notes.py [OPTION] [ARGS]

OPTIONS
    write         create e new note
    read TAG     read a note from a tag TAG
"""
path = os.curdir
filepath = os.path.join(path, 'notes.txt')

while True:
    arguments = sys.argv[1:]

    if not arguments:
        print('Error! You need to pass an argument!')
        print(HELP)
        sys.exit(1)

    if arguments[0] not in ['write', 'read']:
        print(f'Invalid argument `{arguments[0]}`')
        sys.exit(1)

    if arguments[0] == 'write':
        text = [
            input('title: ').strip(),
            input('tag: ').strip(),
            input('text:\n'),
        ]

        with open(filepath, 'a') as file_:
            file_.write('\t'.join(text) + '\n')

    if arguments[0] == 'read':
        try:
            arg_tag = arguments[1]
        except IndexError:
            arg_tag = input('tag: ').lower().strip()

        try:
            for line in open(filepath):
                title, tag, text = line.split('\t')

                if tag.lower() == arg_tag.lower():
                    print(f'Title: {title}\nText: {text}')
                    print('-' * 30)
        except FileNotFoundError:
            print('No file notes to read. Please create a note first.')
            sys.exit(1)
        
    cont = input(f'Continue to {arguments[0]}? [N/y] ').strip().lower()
    if cont != 'y':
        break
