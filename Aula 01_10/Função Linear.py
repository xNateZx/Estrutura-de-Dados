
#o parametro LISTA indica a lista que vai buscar o ALVO

def busca_linear(lista, alvo):
    for i in range(len(lista)):
#   "FOR I IN RANGE" significa que enquanto tiver item na lista e vai passar um por um

        if lista[i] == alvo:
#   "IF" ele vai perguntar se o item em que ele esta corresponde ao alvo        
    
            return i
#   quando encontrar o mesmo retorna usando o "RETURN"

    return -1
# se nao estiver na lista ele retorna -1