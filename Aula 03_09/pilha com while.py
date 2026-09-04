pilha = []

pilha.append("Venda 1")
pilha.append("Venda 2")
pilha.append("Venda 3")
pilha.append("Venda 4")
pilha.append("Venda 5")

while pilha:
    elemento_atual = pilha.pop()

    print(f"processando:{elemento_atual}")

print("pilha esta vazia")
