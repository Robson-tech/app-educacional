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
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, salario=0):
        super().__init__(id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login)
        self._salario = salario
        self._turmas = []

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def turmas(self):
        return self._turmas

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
    
    def add_turma(self, turma):
        self._turmas.append(turma)


class Aluno(Usuario):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, turma, pontuacao=0):
        super().__init__(id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login)
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
    def __init__(self, nome, descricao, professor):
        self._nome = nome
        self._descricao = descricao
        self._professor = professor


class Atividade:
    def __init__(self, materia, autor, titulo, descricao, questoes):
        self._materia = materia
        self._autor = autor
        self._titulo = titulo
        self._descricao = descricao
        self._questoes = questoes
        self._data = datetime.datetime.now()


class Questao:
    def __init__(self, atividade, enunciado, resposta):
        self._atividade = atividade
        self._enunciado = enunciado
        self._resposta = resposta

    def valida_resposta(self, resposta):
        if resposta == self._resposta:
            return True
        else:
            return False


if __name__ == "__main__":
    u = Professor("jorge@example.com", "jorge1234", "jorge", "luis", "2003-09-01")
