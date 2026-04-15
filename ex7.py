# Exercício 7
# Uma central de atendimento telefônico gerencia chamadas em espera usando
# uma pilha. Isso significa que a última chamada recebida será a primeira a ser
# atendida.
# • Crie uma pilha vazia para armazenar as chamadas em espera.
# • Empilhe três chamadas com identificadores numéricos.
# • Mostre qual chamada será atendida primeiro.
# • Atenda a última chamada recebida e mostre a nova chamada no topo da
# pilha.
# • Verifique se ainda há chamadas na pilha após os atendimentos.


class PilhaChamadas:
    def __init__(self):
        self.chamadas = []

    def receber_chamada(self, identificador):
        self.chamadas.append(identificador)

    def atender_chamada(self):
        if not self.esta_vazia():
            return self.chamadas.pop()
        return None

    def proxima_chamada(self):
        if not self.esta_vazia():
            return self.chamadas[-1]
        return None

    def esta_vazia(self):
        return len(self.chamadas) == 0


central = PilhaChamadas()

central.receber_chamada(101)
central.receber_chamada(102)
central.receber_chamada(103)

print("Chamada que será atendida primeiro:", central.proxima_chamada())

central.atender_chamada()

print("Nova chamada no topo da pilha:", central.proxima_chamada())
print("Ainda há chamadas na pilha?", not central.esta_vazia())