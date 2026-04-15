## Exercício 2
# Criar uma pilha e manipular seus elementos.
# 1. Crie uma pilha utilizando uma lista.
# 2. Empilhe 3 números inteiros de sua escolha.
# 3. Mostre o topo da pilha.
# 4. Desempilhe o topo e mostre o novo topo.
# 5. Tente desempilhar todos os elementos e mostrar se a pilha ficou vazia.

pilha = []

pilha.append(7)
pilha.append(14)
pilha.append(21)

print("Topo da pilha:", pilha[-1])

pilha.pop()
print("Novo topo da pilha:", pilha[-1])

pilha.pop()
pilha.pop()
print("A pilha ficou vazia?", len(pilha) == 0)