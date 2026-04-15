## Exercício 1
# Implementar uma pilha simples utilizando uma lista.
# 1. Crie uma pilha vazia (utilizando uma lista).
# 2. Empilhe (adicione) os números 5, 10 e 15 na pilha.
# 3. Mostre o topo da pilha (último elemento).
# 4. Desempilhe (remova) o topo da pilha e mostre o novo topo.
# 5. Verifique se a pilha está vazia e imprima o resultado.


pilha = []

pilha.append(5)
pilha.append(10)
pilha.append(15)

print("Topo da pilha:", pilha[-1])

pilha.pop()

print("Novo topo da pilha:", pilha[-1])
print("A pilha está vazia?", len(pilha) == 0)