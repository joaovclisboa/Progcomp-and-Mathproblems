# ==========================================================
# 1. BACKTRACKING
# ==========================================================
# Útil para problemas de busca exaustiva (força bruta inteligente).
# Exemplo clássico: Problema das N-Rainhas ou Subconjuntos.

def solve_n_queens_backtracking(n: int) -> list[list[str]]:
    """Resolve o problema das N rainhas usando Backtracking."""
    solucoes = []
    # a implementar (criar o tabuleiro, função de validação, e a busca recursiva)
    return solucoes

def subset_sum_backtracking(nums: list[int], target: int) -> list[list[int]]:
    """Encontra todos os subconjuntos de 'nums' que somam 'target'."""
    subconjuntos = []
    # a implementar
    return subconjuntos

# ==========================================================
# 2. BRANCH AND BOUND (RAMIFICAÇÃO E LIMITAÇÃO)
# ==========================================================
# Evolução do Backtracking para problemas de otimização.
# Poda os caminhos que logicamente não podem superar a melhor solução atual.
# Exemplo clássico: Mochila 0/1 (Knapsack) ou Caixeiro Viajante (TSP).

def knapsack_branch_and_bound(pesos: list[int], valores: list[int], capacidade: int) -> int:
    """Resolve o problema da Mochila 0/1 maximizando o valor."""
    max_valor = 0
    # a implementar (definir estrutura do nó, calcular bound/limite superior, usar fila de prioridade)
    return max_valor

def tsp_branch_and_bound(grafo: list[list[int]]) -> tuple[int, list[int]]:
    """Resolve o Caixeiro Viajante (TSP) encontrando o caminho de menor custo."""
    custo_minimo = float('inf')
    melhor_caminho = []
    # a implementar
    return custo_minimo, melhor_caminho

# ==========================================================
# 3. ALGORITMOS APROXIMATIVOS E HEURÍSTICAS
# ==========================================================
# Usados em problemas NP-Difíceis onde a solução exata demora muito tempo.
# Retornam uma solução "boa o suficiente" (com garantias de proximidade do ótimo) de forma rápida.
# Exemplo clássico: Cobertura de Vértices (Vertex Cover) ou TSP em grafos métricos.

def vertex_cover_aprox(grafo: dict[int, list[int]]) -> set[int]:
    """
    Encontra uma cobertura de vértices aproximada (fator de aproximação 2).
    grafo: dicionário representando lista de adjacência.
    """
    cobertura = set()
    # a implementar (escolher arestas arbitrariamente, adicionar extremos, remover incidentes)
    return cobertura

def tsp_aprox_2(grafo: list[list[int]]) -> tuple[int, list[int]]:
    """
    Solução aproximada para o Caixeiro Viajante (TSP) em grafos métricos.
    Garante um resultado no máximo 2x pior que o ótimo.
    """
    # a implementar (envolve achar a Árvore Geradora Mínima (MST) e fazer percurso em pré-ordem)
    pass


# ==========================================================
# ÁREA DE TESTES
# ==========================================================
def main():
    print("Testando Backtracking...")
    # n_queens_res = solve_n_queens_backtracking(4)
    # print("N-Queens (4):", len(n_queens_res), "soluções")
    
    print("\nTestando Branch and Bound...")
    # pesos = [10, 20, 30]
    # valores = [60, 100, 120]
    # cap = 50
    # print("Knapsack (B&B):", knapsack_branch_and_bound(pesos, valores, cap))
    
    print("\nTestando Algoritmos Aproximativos...")
    # grafo = {0: [1, 2], 1: [0, 2], 2: [0, 1, 3], 3: [2]}
    # print("Vertex Cover (Aprox):", vertex_cover_aprox(grafo))

if __name__ == "__main__":
    main()
