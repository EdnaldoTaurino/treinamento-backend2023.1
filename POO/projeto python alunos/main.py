class Aluno:
    def __init__(self, matricula, nota1, nota2):
        self.matricula = matricula
        self.nota1 = nota1
        self.nota2 = nota2

    def getMatricula(self):
        return self.matricula

    def setNota1(self, nota):
        self.nota1 = nota

    def setNota2(self, nota):
        self.nota2 = nota

    def getMedia(self):
        return (self.nota1 + self.nota2) / 2

    def mostrarInfo(self):
        print("Matrícula:", self.matricula)
        print("Nota 1:", self.nota1)
        print("Nota 2:", self.nota2)
        print("Média:", self.getMedia())


def menu():
    print("1. Cadastrar aluno")
    print("2. Cadastrar aluno individualmente")
    print("3. Remover aluno")
    print("4. Buscar aluno por matrícula")
    print("5. Mostrar todos os alunos")
    print("6. Calcular média da turma")
    print("7. Sair")
    return int(input("Escolha uma opção: "))


def obterInfo():
    matricula = input("Digite a matrícula do aluno: ")
    nota1 = float(input("Digite a nota 1 do aluno: "))
    nota2 = float(input("Digite a nota 2 do aluno: "))
    return Aluno(matricula, nota1, nota2)


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
