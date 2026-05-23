def permutation (T, n , r):
    #primeiro verificamos se completamos o array (o array fica completo quano conseguimos
    # uma permutação que nenhuma rainha está na mesma linha ou coluna, então
    # precisamos verificar se essa permutacao é valida, ou seja, se nao tem nenhuma
    # rainha na mesma diagonal da outra)
    if (n == r): #se esta completo
        valid = True
        for i in range(n-1):
            for j in range(i+1, n-1):
                if ((T[i] - T[j]) == (i - j)):
                    valid = False
            if not valid:
                break
        if (valid):
            print(T)
        return
    #é um caso classico de backtracking, a gente tenta um valor que nao está ainda, desfaz, depois tenta outro e assim vai criando
    #essas pilha com as variacoes.
    for i in range(n):
        if i not in T[:r]:
            T[r] = i
            permutation(T, n, r+1)
            T[r] = -1
# Exemplo de uso para N = 8 (8 Rainhas):
if __name__ == "__main__":
    n = 8
    T = [-1] * n  # Inicializa o array com -1
    permutation(T, n, 0)