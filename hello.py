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
__version__ = "0.0.1"
__author__ = "Gabriel Barbosa"

import os

current_language = str(os.getenv("LANG", "en_US"))[:5]
message = "Hello, World!"

if current_language == "pt_BR":
    message = "Olá, Mundo!"
elif current_language == "it_IT":
    message = "Ciao, Mondo!"
elif current_language == "es_SP":
    message = "Hola mundo"
elif current_language == "fr_FR":
    message = "Bonjour Monde"

print(message)
