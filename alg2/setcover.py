

def calcular_cobertura(conjunto: set[str], palavra: str) -> int:
    return len(conjunto & set(palavra))


palavras = ["arid", "dash", "drain", "heard", "lost", "nose", "shun", "slate", "snare", "thread"]

solucao = []
letras_nao_cobertas = set()
palavras_restantes = sorted(palavras)
for palavra in palavras:
    for letra in palavra:
        letras_nao_cobertas.add(letra)

print(letras_nao_cobertas)

while letras_nao_cobertas:
    melhor_palavra = max(palavras_restantes, key= lambda p:(calcular_cobertura(letras_nao_cobertas, p)))
    if calcular_cobertura(letras_nao_cobertas, melhor_palavra) == 0:
        print("nao é possivel cobrir todo o universo")
        break
    solucao.append(melhor_palavra)
    letras_nao_cobertas = letras_nao_cobertas - set(melhor_palavra)
    palavras_restantes.remove(melhor_palavra)

print(solucao)