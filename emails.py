#!/usr/bin/env python3

import os
import sys

arguments = sys.argv[1:]
MSG_ERR = 'Try this: email.py `email_file` `email_tmpl`'

if not arguments:
    print('Please, enter the name of the email file.')
    print(MSG_ERR)
    sys.exit(1)
elif len(arguments) != 2:
    print('Invalid numbers of arguments!')
    print(MSG_ERR)
    sys.exit()

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

for line in open(filepath):
    # TODO: Substituir por envio de email
    client, email = line.split(',')

    print(f'Mandando email para: {email}')
    with open(templatepath, 'r') as file_:
        print(
            file_.read()
            % dict(
                nome=client,
                produto="Mouse Gamer",
                texto="Jogar jogos FPS",
                link="https://mousegamer.com",
                quantidade=2,
                preco=100.24,
            )
        )
    print('-' * 45)

