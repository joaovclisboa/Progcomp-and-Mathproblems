import math
import matplotlib.pyplot as plt

def produto_vetorial(p0, p1, p2):
    #Se o produto vetorial de p0p1 x p0p2 > 0 : indo pra esquerda
    #se o prduto vetorial de p0p1 x p0p2 < 0 : indo pra direita
    # se for igual a zero sao colineares.
    vetor_1 = (p1[0] - p0[0], p1[1] - p0[1])
    vetor_2 = (p2[0] - p0[0], p2[1] - p0[1])
    dir = (vetor_1[0]*vetor_2[1]) - vetor_1[1]*vetor_2[0]
    if (dir > 0):
        return True
    return False


def organizar_pontos(pontos):
    p0 = min(pontos, key= lambda p:(p[1], p[0]))
    pontos_restantes = [p for p in pontos if p != p0]
    for ponto in pontos_restantes:
        ponto.append()
    # a implementar

def graham_scan(pontos):
    """
    Recebe uma lista de pontos (tuplas (x,y)) e retorna a lista de pontos
    que formam a envoltória convexa em sentido anti-horário.
    """
    # Se houver menos de 3 pontos, eles próprios já formam a envoltória
    if len(pontos) < 3:
        return pontos
    
    return pilha


# ==========================================================
# ÁREA DE TESTE E VISUALIZAÇÃO (NÃO PRECISA ALTERAR)
# ==========================================================
def testar_graham_scan():
    # Conjunto de pontos de teste
    pontos = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]

    # Chamada da sua função
    envoltoria = graham_scan(pontos)

    # Preparando as coordenadas de todos os pontos para o gráfico
    px = [p[0] for p in pontos]
    py = [p[1] for p in pontos]

    plt.figure(figsize=(8, 6))
    plt.scatter(px, py, color='blue', s=50, label='Pontos do Conjunto', zorder=5)

    # Se a sua função retornar a envoltória, desenhamos as linhas
    if envoltoria and len(envoltoria) >= 3:
        # Fechar o polígono ligando o último ponto ao primeiro
        envoltoria_fechada = envoltoria + [envoltoria[0]]
        hx = [p[0] for p in envoltoria_fechada]
        hy = [p[1] for p in envoltoria_fechada]
        
        plt.plot(hx, hy, color='red', linestyle='-', linewidth=2, label='Envoltória Convexa')
        # Destacar os vértices que fazem parte da envoltória
        plt.scatter(hx, hy, color='red', s=80, zorder=6)
    else:
        print("A envoltória não foi calculada ou possui menos de 3 pontos.")

    plt.title('Teste da Implementação do Graham Scan')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()

if __name__ == '__main__':
    testar_graham_scan()