from modelos import Atividade, Questao
from autenticacao import Autenticacao


class FormularioUsuario:
    def __init__(self):
        self._modelo = Autenticacao

    def cadastrar(self):
        print("Bem vindo ao sistema de atividades!")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        self._modelo.cadastrar(email, senha)
            
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
        self._modelo.cadastrar(titulo, descricao, usuario, questoes)


class FormularioQuestao:
    def __init__(self):
        self._modelo = Questao

    def cadastrar(self):
        print("Cadastro de questão")
        titulo = input("Digite o título da questão: ")
        descricao = input("Digite a descrição da questão: ")
        self._modelo.cadastrar(titulo, descricao)