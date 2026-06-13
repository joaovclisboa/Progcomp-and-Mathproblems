class Solution:
    def Mochila_bb(self, mochila: list[list[int]], espaco: int):
        mochila.sort(key= lambda p:((p[1]/p[0]) if p[0] != 0 else float('inf')), reverse=True)
        melhor_solucao = -1

        def mochila_rec(item_at, valor_at, espaco_at):
                nonlocal melhor_solucao
                if item_at == len(mochila):
                    if valor_at > melhor_solucao:
                        melhor_solucao = valor_at
                    return
                peso_atual_item, valor_atual_item = mochila[item_at]
                if (peso_atual_item == 0):
                     densidade_atual = float('inf')
                else:
                     densidade_atual = valor_atual_item/peso_atual_item
                if (espaco_at * densidade_atual + valor_at) > melhor_solucao:
                    if peso_atual_item <= espaco_at:
                        mochila_rec(item_at+1, valor_at + valor_atual_item, espaco_at-peso_atual_item)
                    mochila_rec(item_at+1, valor_at, espaco_at)
        mochila_rec(0, 0, espaco)
        print(melhor_solucao)

def test():
    sol = Solution()
    w = 16
    mochila = [[10, 100], [7, 63], [8, 56], [4,12]]
    sol.Mochila_bb(mochila, w)

test()