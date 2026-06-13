class Solution:
    def Mochila_bb(self, mochila: list[list[int]], espaco: int):
        melhor_densidade = len(mochila) * [-1]
        melhor_densidade[len(mochila)-1] = mochila[len(mochila)-1][1]/mochila[len(mochila)-1][0]
        for i in range(len(mochila)-2, -1, -1):
            if (mochila[i][1]/mochila[i][0] > melhor_densidade[i+1]):
                melhor_densidade[i] = mochila[i][1]/mochila[i][0]
            else:
                melhor_densidade[i] = melhor_densidade[i+1]

        melhor_solucao = -1

        def mochila_rec(item_at, valor_at, espaco_at):
                if item_at == len(mochila):
                    if valor_at > melhor_solucao:
                        melhor_solucao = valor_at
                    return
                if (espaco_at * melhor_densidade[item_at] + valor_at) > melhor_solucao:
                    print(espaco_at)
                    if mochila[item_at][0] <= espaco_at:
                        mochila_rec(item_at+1, valor_at + mochila[item_at][1], espaco_at-mochila[item_at][0])
                    mochila_rec(item_at+1, valor_at, espaco_at)
        mochila_rec(0, 0, espaco)
        print(melhor_solucao)

def test():
    sol = Solution()
    w = 16
    mochila = [[10, 100], [7, 63], [8, 56], [4,12]]
    sol.Mochila_bb(mochila, w)

test()