#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de criaças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.2"

# Data
classes = {
    'class1': ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
    'class2': ['João', 'Antonio', 'Carlos', 'Maria', 'Isolda'],
}             

lessons = {
    'english': ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio'],
    'music': ['Erik', 'Carlos', 'Maria'],
    'dance': ['Gustavo', 'Sofia', 'Joana', 'Antonio'],
}

activities = {
    'English': lessons['english'],
    'Music': lessons['music'],
    'Dance': lessons['dance'],
}

# Program
for activity_name, students in activities.items():
    print(f'{activity_name} students:\n')

    activity_class1 = set(students) & set(classes['class1'])
    activity_class2 = set(students) & set(classes['class2'])

    print(f'Class 1 {activity_class1}')
    print(f'Class 2 {activity_class2}')
    print('-' * 40)

