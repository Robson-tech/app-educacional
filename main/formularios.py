from modelos import Atividade, Questao, InfoUsuario


class FormularioUsuario:
    def __init__(self, autenticacao):
        self._modelo = autenticacao

    def cadastrar(self):
        print("Bem vindo ao sistema de atividades!")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        nome = input("Digite seu nome: ")
        sobrenome = input("Digite seu sobrenome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        sexo = input("Digite seu sexo: ")
        info = InfoUsuario(nome, sobrenome, data_nascimento, sexo)
        self._modelo.cadastrar(email, senha, info)
            
    def login(self):
        print("Bem vindo ao sistema de atividades!")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        self._modelo.login(email, senha)


class FormularioAtividade:
    def __init__(self):
        self._modelo = Atividade

    def cadastrar(self, usuario):
        print("Cadastro de atividade")
        titulo = input("Digite o título da atividade: ")
        descricao = input("Digite a descrição da atividade: ")
        questoes = input("Digite as questões da atividade: ")
        return self._modelo.cadastrar(titulo, descricao, usuario, questoes)


class FormularioQuestao:
    def __init__(self):
        self._modelo = Questao

    def cadastrar(self):
        print("Cadastro de questão")
        titulo = input("Digite o título da questão: ")
        descricao = input("Digite a descrição da questão: ")
        return self._modelo.cadastrar(titulo, descricao)