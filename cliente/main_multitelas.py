import sys
import socket
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cod_tela_principal import Ui_TelaPrincipalAluno
from cod_tela_principal_professor import Ui_TelaPrincipalProfessor
from cod_tela_atividade import Ui_TelaAtividade
from cod_tela_login import Ui_Login
from cod_tela_cadastro import Ui_Cadastro
from modelos import Questao
# pyuic5 -x tela_atividade.ui -o tela_atividade.py


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack = []
        self.atividades = []

        self.tela_login = Ui_Login()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_login.setupUi(self.stack[0])
        self.tela_cadastro = Ui_Cadastro()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_cadastro.setupUi(self.stack[1])
        self.tela_principal_aluno = Ui_TelaPrincipalAluno()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_principal_aluno.setupUi(self.stack[2])
        self.tela_principal_professor = Ui_TelaPrincipalProfessor()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_principal_professor.setupUi(self.stack[3])

        self.QtStack.addWidget(self.stack[0])
        self.QtStack.addWidget(self.stack[1])
        self.QtStack.addWidget(self.stack[2])
        self.QtStack.addWidget(self.stack[3])


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        '''Modificadores'''
        # self.sistema = SistemaEducacional()
        ip = 'localhost'
        port = 5000
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)
        self.materias = self.client_socket.recv(1024).decode()
        self.tela_login.botao_login.clicked.connect(self.botao_login)
        self.tela_login.botao_cadastro.clicked.connect(self.botao_cadastrar)
        self.tela_cadastro.alunos_botao_voltar.clicked.connect(
            self.botao_voltar_cadastro)
        self.tela_cadastro.professores_botao_voltar.clicked.connect(
            self.botao_voltar_cadastro)
        self.tela_cadastro.alunos_botao_cadastrar.clicked.connect(
            self.botao_cadastrar_aluno)
        self.tela_cadastro.professores_botao_cadastrar.clicked.connect(
            self.botao_cadastrar_professor)

        for materia in self.materias.split(',')[1:]:
            atividades = self.pegar_atividades(materia)
            self.tela_principal_aluno.add_materia(
                materia.capitalize(), atividades, pilha_paginas=self.QtStack, funcao_criar_pagina_atividade=self.criar_pagina_atividade)

        self.tela_principal_aluno.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_aluno.botao_sair.clicked.connect(self.botao_sair)
        self.tela_principal_professor.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_professor.botao_sair.clicked.connect(
            self.botao_sair)

    def pegar_atividades(self, nome):
        self.client_socket.send(f'3,{nome}'.encode())
        atividades = self.client_socket.recv(1024).decode()
        return atividades.split(',')[1:]

    def pegar_questoes(self, id_atividade):
        self.client_socket.send(f'4,{id_atividade}'.encode())
        questoes = self.client_socket.recv(1024).decode()
        lista_questoes = []
        while questoes[0] == '4':
            lista_questoes.append(Questao(*questoes.split('|')[1:]))
            self.client_socket.send('4'.encode())
            questoes = self.client_socket.recv(1024).decode()
        return lista_questoes

    def criar_pagina_atividade(self, id_atividade, titulo):
        self.atividades.append(Ui_TelaAtividade())
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        self.atividades[-1].setupUi(self.stack[-1], titulo)
        self.QtStack.addWidget(self.stack[-1])
        lista_questoes = self.pegar_questoes(id_atividade)
        for i, questao in enumerate(lista_questoes):
            self.atividades[-1].add_questao(i + 1, questao.enunciado, [
                                            questao.letra_a, questao.letra_b, questao.letra_c, questao.letra_d, questao.letra_e])
        self.atividades[-1].add_rodape()
        def voltar_atividade():
            self.QtStack.setCurrentIndex(2)
        self.atividades[-1].botao_voltar.clicked.connect(voltar_atividade)
        def ir_para_pagina_atividade():
            self.QtStack.setCurrentWidget(novo)
        return ir_para_pagina_atividade

    def enviar_cadastro(self, mensagem):
        if mensagem.split(',')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '1':
                return True
        return False

    def enviar_login(self, mensagem):
        if mensagem.split(',')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta != '0':
                return resposta
        return False

    def botao_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        mensagem = f'1,{email},{senha}'

        if email and senha:
            resposta = self.enviar_login(mensagem)
            if resposta:
                if resposta[0] == '1':
                    for turma in resposta.split(',')[1:]:
                        self.tela_principal_professor.add_turma(
                            f'Turma-{turma.upper()}')
                    self.tela_principal_professor.inserir_espacamento()
                    self.QtStack.setCurrentIndex(3)
                elif resposta[0] == '2':
                    self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
        else:
            QMessageBox.about(self, "Erro", "E-mail ou senha não preenchidos")

    def botao_cadastrar_aluno(self):
        email = self.tela_cadastro.alunos_caixa_email.text()
        senha1 = self.tela_cadastro.alunos_caixa_senha1.text()
        senha2 = self.tela_cadastro.alunos_caixa_senha2.text()
        nome = self.tela_cadastro.alunos_caixa_nome.text()
        sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.alunos_caixa_nascimento.text()
        turma = self.tela_cadastro.alunos_caixa_turma.text()
        mensagem = f'2,{email},{senha1},{nome},{sobrenome},{nascimento},{turma},a'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(
                        self, "Sucesso", "Aluno cadastrado com sucesso")
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.about(
                        self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def botao_cadastrar_professor(self):
        email = self.tela_cadastro.professores_caixa_email.text()
        senha1 = self.tela_cadastro.professores_caixa_senha1.text()
        senha2 = self.tela_cadastro.professores_caixa_senha2.text()
        nome = self.tela_cadastro.professores_caixa_nome.text()
        sobrenome = self.tela_cadastro.professores_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.professores_caixa_nascimento.text()
        mensagem = f'2,{email},{senha1},{nome},{sobrenome},{nascimento},p'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(
                        self, "Sucesso", "Professor cadastrado com sucesso")
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.about(
                        self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def botao_logoff(self):
        mensagem = '0'
        self.tela_principal_professor.limpar_turmas()
        self.client_socket.send(mensagem.encode())
        self.QtStack.setCurrentIndex(0)

    def botao_sair(self):
        mensagem = '-1'
        self.client_socket.send(mensagem.encode())
        self.client_socket.close()
        exit()

    def botao_cadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def botao_voltar_cadastro(self):
        self.QtStack.setCurrentIndex(0)

    def limpar_campos(self):
        self.tela_cadastro.alunos_caixa_email.clear()
        self.tela_cadastro.alunos_caixa_senha1.clear()
        self.tela_cadastro.alunos_caixa_senha2.clear()
        self.tela_cadastro.alunos_caixa_nome.clear()
        self.tela_cadastro.alunos_caixa_sobrenome.clear()
        self.tela_cadastro.alunos_caixa_nascimento.setDate(
            QtCore.QDate(2000, 1, 1))
        self.tela_cadastro.alunos_caixa_turma.clear()
        self.tela_cadastro.professores_caixa_email.clear()
        self.tela_cadastro.professores_caixa_senha1.clear()
        self.tela_cadastro.professores_caixa_senha2.clear()
        self.tela_cadastro.professores_caixa_nome.clear()
        self.tela_cadastro.professores_caixa_sobrenome.clear()
        self.tela_cadastro.professores_caixa_nascimento.setDate(
            QtCore.QDate(2000, 1, 1))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())
