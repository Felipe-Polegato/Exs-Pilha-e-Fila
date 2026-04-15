# Exercício 3
# Você foi contratado para desenvolver uma funcionalidade de “Desfazer/Refazer"
# para um editor de texto simples. O editor permite que o usuário escreva palavras
# em um documento, e, caso cometa um erro, pode desfazer a última ação ou
# refazê-la caso mude de ideia.

documento = []
pilha_desfazer = []
pilha_refazer = []

def escrever(palavra):
    documento.append(palavra)
    pilha_desfazer.append(("escrever", palavra))
    pilha_refazer.clear()

def desfazer():
    if pilha_desfazer:
        acao, palavra = pilha_desfazer.pop()
        if acao == "escrever":
            documento.pop()
            pilha_refazer.append((acao, palavra))
    else:
        print("Nada para desfazer.")
    
def refazer():
    if pilha_refazer:
        acao, palavra = pilha_refazer.pop()
        if acao == "escrever":
            documento.append(palavra)
            pilha_desfazer.append((acao, palavra))
    else:
        print("Nada para refazer.")

# Teste
escrever("Olá")
escrever("mundo")
escrever("Python")

print("Documento atual:", " ".join(documento))

desfazer()
print("Após desfazer:", " ".join(documento))

refazer()
print("Após refazer:", " ".join(documento))

