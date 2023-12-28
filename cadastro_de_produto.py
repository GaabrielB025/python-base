#!/usr/bin/env python3
"""Cadastro de produtos"""
__version__ = "0.1.0"

produto = {
    'nome': 'Caneta',
    'cores': ['azul', 'branco'],
    'preco': 3.23,
    'dimensao': {
        'altura': 12.1,
        'largura': 0.8,
    },
    'estoque': True,
    'codigo': 45678,
    'codebar': None,
}

cliente = {
    'nome': 'Gabriel',
}

compra = {
    'cliente': cliente,
    'produto': produto,
    'quantidade': 3,
}

# Dados
nome_cliente = compra['cliente']['nome']
nome_produto = compra['produto']['nome']
quantidade = compra['quantidade']
preco = compra['produto']['preco']
total = quantidade * preco

print(
    f'O cliente {nome_cliente} comprou um(a) {nome_produto} e pagou R${total}'
)


