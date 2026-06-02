import math

# ==========================================================
# 0. ESTRUTURAS BÁSICAS E FUNÇÕES AUXILIARES
# ==========================================================
class Ponto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def orientacao(p: Ponto, q: Ponto, r: Ponto) -> int:
    a1 = q.x - p.x
    b1 = r.x - p.x
    
    a2 = q.y - p.y
    b2 = r.y - p.y
    det = a1*b2 - b1*a2 #produto vetorial
    if (det == 0): #colineares
        return 0
    if (det > 0):
        return 1 #sentido horario
    return 2 #sentido antihorario



def distancia(p1: Ponto, p2: Ponto) -> float:
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


# ==========================================================
# 1. INTERSEÇÃO DE SEGMENTOS DE RETA
# ==========================================================

#verifica se um ponto esta contido em um segmento (necessario verificar o prod vetorial antes)
def on_segment(p1 : Ponto, p2: Ponto, p3: Ponto) -> bool:
    if (p3.x >= min(p1.x, p2.x) and p3.x <= max(p1.x, p2.x)):
        if (p3.y >= min (p1.y, p2.y) and p3.y <= max(p1.y, p2.y)):
            return True
    return False


def do_intersect(p1: Ponto, q1: Ponto, p2: Ponto, q2: Ponto) -> bool:
    """
    Verifica se o segmento de reta 'p1q1' e 'p2q2' se cruzam.
    """
    d1 = orientacao(p1, q1, q2) #se a reta p1q2 ta a esquerda ou a direita de p1q1
    d2 = orientacao(p1, q1, p2) #se a reta p1p2 ta a esquerda ou direita de p1q1
    d3 = orientacao(q2, p2, p1) 
    d4 = orientacao(q2, p2, q1)

    #agora temos as direcoes relativas temos que verificar se elas de fatp
    #se cruzam ou nao
    if (d1 + d2 == 3 and d3 + d4 == 3):
        return True
    if (d1 == 0 and on_segment(p1, q1, q2)):
        return True
    if (d2 == 0 and on_segment(p1, q1, p2)):
        return True
    if (d3 == 0 and on_segment(q2, p2, p1)):
        return True
    if (d4 == 0 and on_segment(q2, p2, q1)):
        return True
    return False

# ==========================================================
# 2. FECHO CONVEXO (CONVEX HULL)
# ==========================================================
def graham_scan(pontos: list[Ponto]) -> list[Ponto]:
    """
    Encontra o fecho convexo de um conjunto de pontos usando o Algoritmo de Graham.
    Complexidade: O(n log n)
    """
    pontos.sort(key=lambda p: (p.y, p.x))
    p0 = pontos[0]
    pontos = pontos[1:]
    # Ordenar por ângulo polar usando math.atan2(dy, dx)
    # math.atan2 retorna o ângulo em radianos entre o vetor (dx, dy) e o eixo X positivo
    # Se os ângulos forem iguais (colineares), o critério de desempate comum é a distância
    pontos.sort(key=lambda p: (math.atan2(p.y - p0.y, p.x - p0.x), distancia(p0, p)))
    
    #agora temos o p0 e todos os pontos organizados por angulo polar.
    fecho = [p0, pontos[0]]

    for i in range(1, len(pontos)):
        while (len(fecho) > 1 and orientacao(fecho[-2], fecho[-1], pontos[i]) != 2):
            fecho.pop()
        fecho.append(pontos[i])
    return fecho

def jarvis_march(pontos: list[Ponto]) -> list[Ponto]:
    """
    Encontra o fecho convexo usando a Marcha de Jarvis (Mapeamento de Embrulho/Gift Wrapping).
    Complexidade: O(n * h), onde h é o número de pontos no fecho.
    """
    fecho = []
    # a implementar
    return fecho

# ==========================================================
# 3. PAR DE PONTOS MAIS PRÓXIMO (CLOSEST PAIR OF POINTS)
# ==========================================================
def closest_pair(pontos: list[Ponto]) -> tuple[Ponto, Ponto, float]:
    """
    Encontra o par de pontos com a menor distância entre si usando Divisão e Conquista.
    Complexidade: O(n log n)
    """
    # a implementar
    pass

# ==========================================================
# 4. ÁREA DE UM POLÍGONO (FÓRMULA DE SHOELACE)
# ==========================================================
def polygon_area(pontos: list[Ponto]) -> float:
    """
    Calcula a área de um polígono simples dado pelas coordenadas de seus vértices em ordem.
    """
    area = 0.0
    # a implementar
    return area

# ==========================================================
# 5. PONTO DENTRO DO POLÍGONO (RAY CASTING)
# ==========================================================
def is_inside_polygon(pontos: list[Ponto], p: Ponto) -> bool:
    """
    Verifica se um ponto 'p' está estritamente dentro do polígono especificado.
    Algoritmo clássico de Ray Casting (lançar um raio horizontal infinito e contar interseções).
    """
    # a implementar
    pass

# ==========================================================
# ÁREA DE TESTES
# ==========================================================
def main():
    print("Testando Algoritmos Geométricos...")
    
    # Exemplo simples de uso da classe Ponto
    # p1 = Ponto(0, 0)
    # p2 = Ponto(3, 4)
    # print(f"Distância entre {p1} e {p2}: {distancia(p1, p2)}")

if __name__ == "__main__":
    main()
