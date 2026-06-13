from typing import List

class Solution:
    def graphColoring(self, n: int, edges: List[List[int]], m: int = 3) -> bool:
        # 1. construir lista de adjacência
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 2. vetor de cores (0 = não colorido)
        #vamos usar cor 1, cor 2 e cor3
        color = [0] * n

        # 3. função de verificação
        def is_valid(node: int, c: int) -> bool:
            for nei in graph[node]:
                if color[nei] == c:
                    return False
            return True

        # 4. backtracking
        def backtrack(node: int) -> bool:
            if node == len(graph):
                return True
            for i in range(1, 4):
                if (is_valid(node, i)):
                    color[node] = i
                    if(backtrack(node+1)):
                        return True
            color[node] = 0
            return False

        # 5. iniciar do primeiro vértice
        return backtrack(0)
    

def test():
    sol = Solution()

    # Caso 1: triângulo (não é 2-colorível, mas é 3-colorível)
    n1 = 3
    edges1 = [[0,1],[1,2],[2,0]]
    print(sol.graphColoring(n1, edges1))  # True

    # Caso 2: grafo do enunciado (Neapolitan 5.18)
    n2 = 6
    edges2 = [
        (0,1),(0,3),
        (1,2),(1,4),
        (2,5),
        (3,4),
        (4,5)
    ]
    print(sol.graphColoring(n2, edges2))  # True ou False dependendo da estrutura (sem resolver aqui)

    # Caso 3: grafo completo K4 (não é 3-colorível)
    n3 = 4
    edges3 = [
        (0,1),(0,2),(0,3),
        (1,2),(1,3),
        (2,3)
    ]
    print(sol.graphColoring(n3, edges3))  # False

test()
