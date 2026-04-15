# Exercício 5
# Um consultório odontológico precisa gerenciar a ordem de atendimento dos
# pacientes. Para isso, foi decidido implementar uma fila onde os pacientes são
# chamados na ordem em que chegaram (FIFO – First In, First Out).

class FilaPacientes:
    def __init__(self):
        self.pacientes = []

    def chegar_paciente(self, nome):
        self.pacientes.append(nome)

    def atender_paciente(self):
        if not self.esta_vazia():
            return self.pacientes.pop(0)
        return None

    def proximo_paciente(self):
        if not self.esta_vazia():
            return self.pacientes[0]
        return None

    def esta_vazia(self):
        return len(self.pacientes) == 0


consultorio = FilaPacientes()

consultorio.chegar_paciente("Ana")
consultorio.chegar_paciente("Bruno")
consultorio.chegar_paciente("Carlos")

print("Primeiro paciente a ser atendido:", consultorio.proximo_paciente())

consultorio.atender_paciente()

print("Próximo paciente:", consultorio.proximo_paciente())
print("A fila está vazia?", consultorio.esta_vazia())