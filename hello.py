#!/usr/bin/env python
"""
Hello World multi languages

depending on the language configured in the environment,
the program displays the corresponding message.

How to use:

You need to have the LANG variable properly configured:

    export LANG=pt_BR

Or enter the argument `--lang`

Or the user will have to type.

Execution:

    python3 hello.py
"""
__version__ = "0.1.3"
__author__ = "Gabriel Barbosa"

import os
import sys

arguments = {
    'lang': None,
    'count': 1,
}

valid_languages = ('pt_BR', 'en_US', 'it_IT', 'fr_FR', 'es_SP')

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split('=')
    value = value.strip()
    key = key.lstrip('-').strip()

    if key not in arguments:
        print(f'`{key}` is not a valid argument!')
        sys.exit(1)

    arguments[key] = value

current_language = arguments['lang']

if current_language is None:
    # TODO: Usar repetição
    if 'LANG' in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input('Choose a language: ').strip()

current_language = str(current_language)[:5]

messages = {
    'pt_BR': 'Olá, mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!',
    'en_US': 'Hello, World!'
}

print(messages[current_language] * int(arguments['count']))

