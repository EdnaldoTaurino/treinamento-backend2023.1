class Aluno:
    def __init__(self):
        self.matricula = ""
        self.idade = 0
        self.nome = ""
        self.nota1 = 0.0
        self.nota2 = 0.0
        self.media_final = 0.0

    def setMatricula(self, matricula):
        self.matricula = matricula

    def setIdade(self, x):
        if x >= 0 and x <= 100:
            self.idade = x
        else:
            self.idade = 0

    def getIdade(self):
        return self.idade

    def setNome(self, nome):
        self.nome = nome

    def setNotas(self, a, b):
        if a > 0 and a <= 10:
            self.nota1 = a
        else:
            self.nota1 = 0

        if b > 0 and b <= 10:
            self.nota2 = b
        else:
            self.nota2 = 0

    def getNota1(self):
        return self.nota1

    def getNota2(self):
        return self.nota2

    def getMedia(self):
        self.media_final = (self.nota1 + self.nota2) / 2
        return self.media_final

    def AprovadoReprovado(self):
        if self.media_final >= 6:
            return "APROVADO."
        else:
            return "REPROVADO."

    def mostrarInfo(self):
        print("Matrícula:", self.matricula)
        print("Idade:", self.idade)
        print("Nome:", self.nome)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
        print("Média:", self.getMedia())
        print("Situação:", self.AprovadoReprovado())

    def setNota1(self, a):
        if a >= 0 and a <= 10:
            self.nota1 = a

    def setNota2(self, a):
        if a >= 0 and a <= 10:
            self.nota2 = a


def obterInfo():
    aluno = Aluno()

    temp = input("Digite a matrícula: ")
    aluno.setMatricula(temp)

    temp = input("Digite o nome: ")
    aluno.setNome(temp)

    temp2 = int(input("Digite a idade: "))
    aluno.setIdade(temp2)

    temp_nota1, temp_nota2 = map(float, input("Digite as duas notas: ").split())
    aluno.setNotas(temp_nota1, temp_nota2)

    return aluno


def menu():
    print("1 - criar lista")
    print("2 - inserir novo aluno")
    print("3 - remover um aluno")
    print("4 - buscar aluno")
    print("5 - mostrar lista")
    print("6 - media da turma")
    print("7 - sair")
    return int(input("Escolha uma opção: "))


def compara_matricula(a, b):
    return a.getMatricula() > b.getMatricula()


turma = []

while True:
    opcao = menu()

    if opcao == 1:
        while True:
            temp = obterInfo()
            turma.append(temp)
            turma.sort(key=lambda aluno: aluno.getMatricula())

            flag = input("Continuar cadastrando? (sim/não): ")
            if flag != "sim":
                break

    elif opcao == 2:
        temp = obterInfo()
        turma.append(temp)

    elif opcao == 3:
        matricula = input("Digite a matrícula do aluno a ser removido: ")
        turma = [aluno for aluno in turma if aluno.getMatricula() != matricula]

    elif opcao == 4:
        matricula = input("Digite a matrícula do aluno a ser buscado: ")
        for aluno in turma:
            if aluno.getMatricula() == matricula:
                flag22 = input("Mudar nota1, nota2 do aluno? (sim/não): ")
                if flag22 == "sim":
                    flag33 = input("Digite 1 para nota1 e 2 para nota2: ")
                    if flag33 == "1":
                        nota = float(input("Digite a nova nota1: "))
                        aluno.setNota1(nota)
                    elif flag33 == "2":
                        nota = float(input("Digite a nova nota2: "))
                        aluno.setNota2(nota)

    elif opcao == 5:
        for i, aluno in enumerate(turma, start=1):
            print("Índice:", i, "-")
            aluno.mostrarInfo()

    elif opcao == 6:
        acumulador = sum(aluno.getMedia() for aluno in turma)
        if len(turma) > 0:
            media_turma = acumulador / len(turma)
            print("A média da turma é de:", media_turma)
        else:
            print("A turma está vazia.")

    elif opcao == 7:
        break
