import string


# ==========================================================
# 1. FORÇA BRUTA (NAIVE STRING MATCHER)
# ==========================================================
def naive_string_matcher(padrao, texto):
    n = len(texto)
    m = len(padrao)
    ocorrencias = []
    for i in range(n-m+1): #vai do tamanho de 1 ate tamanho do texto - tamanho do padrao + 1 pra na ultima iteração o i estar exatamente no inicio da ultima casa que o padrao pode
        for j in range(m): #passamos por todos elementos do padrão
                if (padrao[j] == texto[i+j]): #se o padrao na posição j é igual ao texto na posicao i + j, ou seja, o caractere bateu
                     if (j == m-1): #se estamos no ultimo elemento do padrao e ele bateu
                          ocorrencias.append(i) #adicionamos na ocorrencia onde ele iniciou
                     continue
                break
    return ocorrencias

# ==========================================================
# 2. RABIN-KARP
# ==========================================================
def rabin_karp(padrao, texto, d=256, q=101) -> list[int]:
    """
    d: número de caracteres no alfabeto
    q: um número primo para calcular o hash
    """
    ocorrencias = []
    # a implementar
    return ocorrencias

# ==========================================================
# 3. AUTÔMATO FINITO (FASA)
# ==========================================================
def compute_transition_function(padrao) -> dict:
     # a implementar
     pass

def FASA(padrao, texto) -> list[int]: 
     """Finite Automaton String-Matching Algorithm"""
     ocorrencias = []
     # a implementar
     return ocorrencias

# ==========================================================
# 4. KNUTH-MORRIS-PRATT (KMP)
# ==========================================================
def prefixFunc(padrao) -> list[int]:
     prefix = [0] * len(padrao)
     if (len(padrao) < 3):
          return prefix # alterado para retornar prefix em vez de vazio
     j = 0
     for i in range(2, len(padrao)):
          if (padrao[i] == padrao[j]):
               prefix[i] = prefix[i-1] + 1
               j += 1
          else:
               j = 0
               if (padrao[i] == padrao[j]):
                    prefix[i] = 1
                    j += 1
     return prefix

def KMP(padrao, texto) -> list[int]: 
     """Knuth-Morris-Pratt (KMP) Algorithm"""
     ocorrencias = []
     # a implementar (lembre-se de chamar prefixFunc)
     return ocorrencias

# ==========================================================
# 5. BOYER-MOORE-HORSPOOL
# ==========================================================
def shift_table_horspool(padrao) -> dict:
    """Pré-processamento da tabela de saltos (Shift Table) do Horspool"""
    # a implementar
    pass

def boyer_moore_horspool(padrao, texto) -> list[int]:
    """Algoritmo de Horspool para busca de substring"""
    ocorrencias = []
    # a implementar
    return ocorrencias

# ==========================================================
# 6. TRIE / AHO-CORASICK (MÚLTIPLOS PADRÕES)
# ==========================================================
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        # Para Aho-Corasick, você pode adicionar 'fail_link' ou 'output_link'
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        # a implementar
        pass

    def search(self, word: str) -> bool:
        # a implementar
        pass

def trie_string_match(padroes: list[str], texto: str) -> dict:
    """Busca de multipadrões em texto usando Trie (ou Aho-Corasick)"""
    # a implementar
    pass

# ==========================================================
# ÁREA DE TESTES
# ==========================================================
def main():
    texto = "ababbabbabbababbabb"
    padrao = "abb"
    
    #print("Teste Prefix Function (KMP) em 'ababbabb':", prefixFunc("ababbabb"))
    print("Naive String Matcher:", naive_string_matcher(padrao, texto))


if __name__ == "__main__":
    main()
