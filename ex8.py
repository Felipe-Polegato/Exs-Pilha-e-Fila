# Exercício 8 - Extra
# Um navegador de internet usa uma pilha para armazenar o histórico de
# navegação. Cada vez que o usuário acessa uma nova página, ela é adicionada
# ao histórico. O usuário pode voltar para a página anterior ou avançar
# novamente.
# • Crie uma pilha para armazenar as páginas visitadas.
# • Empilhe três páginas acessadas pelo usuário.
# • Mostre a última página visitada.
# • O usuário clica no botão "Voltar", então desempilhe a última página
# visitada e mostre a nova página no topo.
# • O usuário decide avançar novamente. Como o histórico de páginas
# acessadas foi modificado, implemente um sistema para refazer a
# navegação caso necessário.

class Navegador:
    def __init__(self):
        self.historico = []
        self.refazer = []

    def acessar_pagina(self, pagina):
        self.historico.append(pagina)
        self.refazer.clear()

    def pagina_atual(self):
        if len(self.historico) > 0:
            return self.historico[-1]
        return None

    def voltar(self):
        if len(self.historico) > 1:
            pagina_removida = self.historico.pop()
            self.refazer.append(pagina_removida)
        else:
            print("Não há página anterior para voltar.")

    def avancar(self):
        if len(self.refazer) > 0:
            pagina = self.refazer.pop()
            self.historico.append(pagina)
        else:
            print("Não há página para avançar.")


nav = Navegador()

nav.acessar_pagina("google.com")
nav.acessar_pagina("youtube.com")
nav.acessar_pagina("github.com")

print("Última página visitada:", nav.pagina_atual())

nav.voltar()
print("Página atual após voltar:", nav.pagina_atual())

nav.avancar()
print("Página atual após avançar:", nav.pagina_atual())