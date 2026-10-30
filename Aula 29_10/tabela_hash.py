def funcao_hash(chave):
    return chave % 8

print(funcao_hash("x"))

# dentro de "print(funcao_hash(x)" o x e a chave que vai ser inserida, 
# ou o valor que vai divido dentro da funcao, o resultado dessa divisao indica qual "gaveta" 
# esse valor sera inserido.