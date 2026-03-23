import string

def naive_string_matcher(padrao, texto) -> string:
    n = len(texto)
    m = len(padrao)
    for i in range(n-m):
        for j in range(m):
                if (padrao[j] == texto[i]):
                     continue
                else:
                     break

def FASA(padrao, texto) -> list[int]: #Finite Automaton String-Matching Algorithm
     return [1, 2, 3]
def CPF(padrao) -> list[int]: #compute prefix function
     return[1, 2, 3]

def prefixFunc(padrao) -> list[int]:
     prefix = [0] * len(padrao)
     if (len(padrao) < 3):
          return
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


     return [1,2,3]
def KMP(padrao, texto) -> list[int]: #Knuth-Morris-Pratt
     return [1, 2, 3]


def main():
    texto = "ababbabbabbababbabb"
    print(prefixFunc(texto))


if __name__ == "__main__":
    main()
