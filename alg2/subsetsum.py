conjunto = [3, 34, 4, 12, 5, 2]
alvo = 9

def subsetsum(conjunto, alvo, indice_atual, soma_atual) -> bool:
    if (soma_atual == alvo):
        return True
    if (soma_atual > alvo or indice_atual >= len(conjunto)):
        return False
    if (subsetsum(conjunto, alvo, indice_atual+1, soma_atual + conjunto[indice_atual])):
        return True
    if (subsetsum(conjunto, alvo, indice_atual+1, soma_atual)):
        return True
    return False
print(subsetsum(conjunto, alvo, 0, 0))