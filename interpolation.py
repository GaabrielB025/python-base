#!/usr/bin/env python3

email_tmpl = """\
Olá %(nome)s

Tem interesse em comprar o produto: %(produto)s?

Este produto é ótimo para
%(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d unidades disponíveis!

Preço promocional R$%(preco).2f
"""

clientes = ["João", "Maria", "Marcos", "Karla"]

for cliente in clientes:
    print(
        email_tmpl
        % dict(
            nome=cliente,
            produto="Mouse Gamer",
            texto="Jogar jogos FPS",
            link="https://mousegamer.com",
            quantidade=2,
            preco=100.24,
        )
    )
