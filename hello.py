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

HELP = """
$ hello.py [OPTIONS]

LANG = [pt_BR, 'en_US', 'it_IT', 'fr_FR', 'es_SP']

Options:
    --lang=LANG          print the message in LANG
    --count=n            repeate the print n times
"""

arguments = {
    'lang': None,
    'count': 1,
}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split('=')
    except ValueError as e:
        # TODO: Substituir por logging
        print(f'Invalid argument `{arg}`')
        print(HELP)
        sys.exit(1)

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

# message = messages.get(current_language, messages['en_US'])

try:
    message = messages[current_language]
except KeyError:
    print(f'Invalid language: `{current_language}`')
    print(f'You can try one of these: {list(messages.keys())}')
    sys.exit(1)

try:
    count = int(arguments['count'])
except ValueError:
    print('Please, enter only numbers.')
    sys.exit(1)

print(message * count)
