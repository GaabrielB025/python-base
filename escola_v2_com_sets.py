#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de criaças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.1"

# Data
class1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
class2 = ['João', 'Antonio', 'Carlos', 'Maria', 'Isolda']

english_lesson = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
music_lesson = ['Erik', 'Carlos', 'Maria']
dance_lesson = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

activities = [
    ('English', english_lesson),
    ('Music', music_lesson),
    ('Dance', dance_lesson),
]

# Program
for activity_name, students in activities:
    print(f'{activity_name} students:\n')

    activity_class1 = set(students) & set(class1)
    activity_class2 = set(students) & set(class2)

    print(f'Class 1 {activity_class1}')
    print(f'Class 2 {activity_class2}')
    print('-' * 40)

