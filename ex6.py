# Exercício 6
# Uma impressora trabalha com um sistema de fila para processar documentos
# enviados para impressão. Cada documento enviado entra no final da fila e será
# impresso na ordem em que chegou.
# • Crie uma fila vazia para representar a fila de impressão.
# • Enfileire três documentos (nomes de arquivos) na fila.
# • Mostre qual documento será impresso primeiro.
# • Desenfileire o primeiro documento e mostre o próximo da fila.
# • Verifique se ainda há documentos na fila após as remoções.

class FilaImpressao:
    def __init__(self):
        self.documentos = []

    def adicionar_documento(self, nome_arquivo):
        self.documentos.append(nome_arquivo)

    def imprimir_documento(self):
        if not self.esta_vazia():
            return self.documentos.pop(0)
        return None

    def proximo_documento(self):
        if not self.esta_vazia():
            return self.documentos[0]
        return None

    def esta_vazia(self):
        return len(self.documentos) == 0


impressora = FilaImpressao()

impressora.adicionar_documento("trabalho.pdf")
impressora.adicionar_documento("foto.png")
impressora.adicionar_documento("relatorio.docx")

print("Documento que será impresso primeiro:", impressora.proximo_documento())

impressora.imprimir_documento()

print("Próximo documento da fila:", impressora.proximo_documento())
print("Ainda há documentos na fila?", not impressora.esta_vazia())