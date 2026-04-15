# Exercício 4
# Criar uma implementação simples de uma fila (Queue) usando listas.
# 1. Crie uma fila vazia.
# 2. Enfileire 3 números inteiros na fila.
# 3. Mostre o primeiro elemento da fila.
# 4. Desenfileire o primeiro elemento e mostre o novo primeiro elemento.
# 5. Verifique se a fila está vazia após as remoções.

class Fila:
    def __init__(self):
        self.itens = []

    def enfileirar(self, valor):
        self.itens.append(valor)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.itens.pop(0)
        return None

    def primeiro(self):
        if not self.esta_vazia():
            return self.itens[0]
        return None

    def esta_vazia(self):
        return len(self.itens) == 0


fila = Fila()

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)

print("Primeiro elemento da fila:", fila.primeiro())

fila.desenfileirar()

print("Novo primeiro elemento:", fila.primeiro())
print("A fila está vazia?", fila.esta_vazia())