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
    pontos_restantes.sort(key = lambda p:(math.atan2(p[1] - p0[1], p[0] - p0[0]), math.dist(p0, p)))
    pontos_restantes_final = []
    
    if len(pontos_restantes) > 0:
        pontos_restantes_final.append(pontos_restantes[0])
        
    for i in range(1, len(pontos_restantes)):
        ang_atual = math.atan2(pontos_restantes[i][1] - p0[1], pontos_restantes[i][0] - p0[0])
        ang_anterior = math.atan2(pontos_restantes[i-1][1] - p0[1], pontos_restantes[i-1][0] - p0[0])
        
        if ang_atual != ang_anterior:
            pontos_restantes_final.append(pontos_restantes[i])
        else:
            pontos_restantes_final[-1] = pontos_restantes[i]
            
    # Inserindo o p0 na frente
    pontos_restantes_final.insert(0, p0)
    
    return pontos_restantes_final

def graham_scan(pontos):
    """
    Recebe uma lista de pontos (tuplas (x,y)) e retorna a lista de pontos
    que formam a envoltória convexa em sentido anti-horário.
    """
    # Se houver menos de 3 pontos, eles próprios já formam a envoltória
    if len(pontos) < 3:
        return pontos
        
    pontos = organizar_pontos(pontos)
    
    # Após remover pontos na mesma reta, podemos ter ficado com menos de 3 pontos
    if len(pontos) < 3:
        return pontos

    # 1. Inicializa a pilha com os três primeiros pontos
    pilha = [pontos[0], pontos[1], pontos[2]]

    # 2. Varredura com o resto dos pontos
    for i in range(3, len(pontos)):
        # Avaliamos o penúltimo da pilha (pilha[-2]), o último da pilha (pilha[-1]) e o ponto atual (pontos[i]).
        # Queremos APENAS curvas para a esquerda (onde o produto vetorial é True/Positivo).
        # Enquanto o produto vetorial for menor ou igual a zero (False), fazemos pop (desempilhamos)
        while len(pilha) > 1 and not produto_vetorial(pilha[-2], pilha[-1], pontos[i]):
            pilha.pop()
            
        # Adiciona o ponto atual na pilha
        pilha.append(pontos[i])

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