import abc
import datetime


class Usuario(abc.ABC):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login):
        self._id = id
        self._email = email
        self._senha = senha
        self._nome = nome
        self._sobrenome = sobrenome
        self._nascimento = nascimento
        self._data_cadastro = data_cadastro
        self._ultimo_login = ultimo_login

    def __str__(self):
        return self.email

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    @property
    def ultimo_login(self):
        return self._ultimo_login

    @id.setter
    def id(self, id):
        self._id = id

    @abc.abstractmethod
    def validar_email(self, email):
        pass

    @abc.abstractmethod
    def validar_senha(self, senha):
        pass


class Diretor(Usuario):
    def __init__(self, email, senha, nome, sobrenome, nascimento):
        super().__init__(email, senha, nome, sobrenome, nascimento)

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Professor(Usuario):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, materias_professor=[], turmas_professor=[], atividades_professor=[], salario=1320):
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._materias_professor = materias_professor
        self._turmas_professor = turmas_professor
        self._atividades_professor = atividades_professor
        self._salario = salario
    
    def __str__(self):
        return f'{self._id}\n{self._email}\n{self._senha}\n{self._nome}\n{self._sobrenome}\n{self._nascimento}\n{self._data_cadastro}\n{self._ultimo_login}\n{self._materias_professor}\n{self._turmas_professor}\n{self._atividades_professor}\n{self._salario}'

    @property
    def materias(self):
        enviar = ''
        for materia in self._materias_professor:
            enviar += f"|{materia[0]}-{materia[1]}"
        return enviar
    
    def add_materia(self, materia):
        self._materias_professor.append(materia)

    @property
    def turmas(self):
        enviar = ''
        for turma in self._turmas_professor:
            enviar += f'|{turma[0]}-{turma[1]}'
        return enviar

    def add_turma(self, turma):
        self._turmas_professor.append(turma)

    @property
    def atividades(self):
        enviar = ''
        for atividade in self._atividades_professor:
            enviar += f'|{atividade[0]}-{atividade[1]}-{atividade[2]}'
        return enviar

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Aluno(Usuario):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, turma, pontuacao=0):
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._turma = turma
        self._pontuacao = pontuacao

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Materia:
    def __init__(self, id, nome, atividades=[], professores=[]):
        self._id = id
        self._nome = nome.capitalize()
        self._atividades = atividades
        self._professores = professores

    def __str__(self):
        return f'{self._id}-{self._nome}'

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self._nome

    @property
    def atividades(self):
        return self._atividades
    
    def add_atividade(self, atividade):
        self._atividades.append(atividade)
    
    def abrir(self):
        for num, atividade in enumerate(self._atividades):
            print(f'{num} - {atividade.titulo}')
        opc = int(input('Digite o número da atividade: '))
        while opc:
            if opc < 0 or opc > len(self._atividades):
                print('Atividade não encontrada')
                opc = int(input('Digite o número da atividade: '))
            else:
                self._atividades[opc].abrir()


class Atividade:
    def __init__(self, id, titulo, descricao, professor_id, turma_id, materia_id, questoes=[]):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._professor_id = professor_id
        self._turma_id = turma_id
        self._materia_id = materia_id
        self._questoes = questoes
        self._respondidas = 0

    def __str__(self):
        return f'{self._id}-{self._titulo}-{self._descricao}-{self._materia_id}-{self._turma_id}-{self._professor_id}'
    
    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def descricao(self):
        return self._descricao

    @property
    def questoes(self):
        return self._questoes

    def add_questao(self, questao):
        self._questoes.append(questao)

    def abrir(self):
        for num, questao in enumerate(self._questoes):
            print(f'{num+1} - {questao.enunciado}')
            print(f'A) {questao.letra_a}')
            print(f'B) {questao.letra_b}')
            print(f'C) {questao.letra_c}')
            print(f'D) {questao.letra_d}')
            print(f'E) {questao.letra_e}')
        while self._respondidas < len(self._questoes):
            num, resposta = input('Digite o número da questão e a resposta: ').split()
            if not questao[num-1].respondida:
                questao[num-1].validar_resposta(resposta)
            else:
                print('Questão já respondida')


class Questao:
    def __init__(self, id, atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e):
        self._id = id
        self._atividade_id = atividade_id
        self._resposta = resposta
        self.enunciado = enunciado
        self.letra_a = letra_a
        self.letra_b = letra_b
        self.letra_c = letra_c
        self.letra_d = letra_d
        self.letra_e = letra_e
        self.respondida = False

    def __str__(self):
        return f'{self.id}|{self.atividade_id}|{self.enunciado}|{self.resposta}|{self.letra_a}|{self.letra_b}|{self.letra_c}|{self.letra_d}|{self.letra_e}'

    @property
    def id(self):
        return self._id

    @property
    def atividade_id(self):
        return self._atividade_id

    @property
    def resposta(self):
        return self._resposta

    def validar_resposta(self, resposta):
        if not self.respondida:
            self.respondida = True
            if resposta == self._resposta:
                return True
            else:
                return False
        else:
            print('Questão já respondida')
            return False


if __name__ == "__main__":
    u = Professor("jorge@example.com", "jorge1234",
                  "jorge", "luis", "2003-09-01")
