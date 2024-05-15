class Paciente:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Medico:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

class Consulta:
    def __init__(self, paciente, medico, data):
        self.paciente = paciente
        self.medico = medico
        self.data = data

# Função para criar um paciente com dados fornecidos pelo usuário
def criar_paciente():
    nome = input("Nome do paciente: ")
    idade = int(input("Idade do paciente: "))
    sexo = input("Sexo do paciente: ")
    return Paciente(nome, idade, sexo)

# Função para criar um médico com dados fornecidos pelo usuário
def criar_medico():
    nome = input("Nome do médico: ")
    especialidade = input("Especialidade do médico: ")
    return Medico(nome, especialidade)

# Função para agendar uma consulta com dados fornecidos pelo usuário
def agendar_consulta(pacientes, medicos):
    print("Pacientes disponíveis:")
    for i, paciente in enumerate(pacientes, start=1):
        print(f"{i}. {paciente.nome}")

    paciente_idx = int(input("Escolha o paciente (pelo número): ")) - 1
    paciente = pacientes[paciente_idx]

    print("Médicos disponíveis:")
    for i, medico in enumerate(medicos, start=1):
        print(f"{i}. {medico.nome}")

    medico_idx = int(input("Escolha o médico (pelo número): ")) - 1
    medico = medicos[medico_idx]

    data = input("Data da consulta (formato YYYY-MM-DD HH:MM): ")

    return Consulta(paciente, medico, data)