#!/usr/bin/env python3
import sys

try:
    names = open('names.txt').readlines()
except FileNotFoundError:
    print('File not found.')
    sys.exit(1)
    # TODO: Usar retry
else:
    print('Sucesso!')
finally:
    print('Execute isso sempre.')

try:
    print(names[2])
except IndexError as e:
    print('Missing argument required.')
    sys.exit(1)
