#!/usr/bin/env python
"""
Hello World multi languages

depending on the language configured in the environment,
the program displays the corresponding message.

How to use:

You need to have the LANG variable properly configured:

    export LANG=pt_BR

Execution:

    python3 hello.py
"""
__version__ = "0.1.2"
__author__ = "Gabriel Barbosa"

import os

current_language = str(os.getenv("LANG", "en_US"))[:5]

messages = {
    'pt_BR': 'Olá, mundo!',
    'it_IT': 'Ciao, Mondo!',
    'es_SP': 'Hola, Mundo!',
    'fr_FR': 'Bonjour, Monde!',
    'en_US': 'Hello, World!'
}

msg = messages.get(current_language)
print(msg)

