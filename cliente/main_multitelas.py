import sys
import socket
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cod_tela_principal_aluno import Ui_TelaPrincipalAluno
from cod_tela_principal_professor import Ui_TelaPrincipalProfessor
from cod_tela_atividade_aluno import Ui_TelaAtividade
from cod_tela_atividade_professor import Ui_AtividadeProfessor
from cod_tela_login import Ui_Login
from cod_tela_cadastro import Ui_Cadastro
from modelos import Atividade, Questao
# pyuic5 -x tela_principal_professor.ui -o tela_principal_professor.py


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack = []
        self.atividades = []
        self.atividades_turma = {}

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

    def get_atividade(self, id_atividade):
        self.client_socket.send(f'4|{id_atividade}'.encode())
        questoes = self.client_socket.recv(1024).decode()
        lista_questoes = []
        while questoes[0] == '4':
            lista_questoes.append(Questao(*questoes.split('|')[1:]))
            self.client_socket.send('4'.encode())
            questoes = self.client_socket.recv(1024).decode()
        atividade_campos = questoes.split('|')[1].split('-')
        if atividade_campos[0] == 'None':
            return None
        return Atividade(*atividade_campos, lista_questoes)

    def criar_pagina_atividade(self, id_atividade, titulo):
        self.atividades.append(Ui_TelaAtividade())
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        self.atividades[-1].setupUi(self.stack[-1], titulo)
        atividade = self.get_atividade(id_atividade)
        lista_questoes = atividade.questoes
        self.QtStack.addWidget(self.stack[-1])
        if lista_questoes:
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

    def criar_pagina_atividade_turma(self, materia_id, turma_id, id_atividade=None):
        titulo = len(self.stack) + 1
        self.atividades_turma[titulo] = Ui_AtividadeProfessor()
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        atividade = self.get_atividade(id_atividade)
        if atividade:
            self.atividades_turma[titulo].setupUi(self.stack[-1], atividade)
            self.atividades_turma[titulo].input_titulo.setText(
                atividade.titulo)
            self.atividades_turma[titulo].input_descricao.setText(
                atividade.descricao)
        else:
            self.atividades_turma[titulo].setupUi(
                self.stack[-1], Atividade(None, None, None, materia_id, turma_id, None, None))
        self.QtStack.addWidget(self.stack[-1])
        self.atividades_turma[titulo].botao_publicar.clicked.connect(
            self.cadastrar_tarefa)

        def voltar_atividade():
            self.QtStack.setCurrentIndex(3)
        self.atividades_turma[titulo].botao_voltar.clicked.connect(
            voltar_atividade)

        def ir_para_pagina_atividade():
            self.QtStack.setCurrentWidget(novo)
        return ir_para_pagina_atividade


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        '''Modificadores'''
        self._usuario = None
        ip = 'LOCALHOST'
        port = 5000
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)

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

        self.tela_principal_aluno.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_aluno.botao_sair.clicked.connect(self.botao_sair)
        self.tela_principal_professor.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_professor.botao_sair.clicked.connect(
            self.botao_sair)

    def pegar_atividades(self, nome):
        self.client_socket.send(f'3|{nome}'.encode())
        atividades = self.client_socket.recv(1024).decode()
        return atividades.split('|')[1:]

    def pegar_atividades_turma(self, nome_turma):
        self.client_socket.send(f'5|{nome_turma}'.encode())
        atividades = self.client_socket.recv(4096).decode()
        lista_atividades = []
        for atividade in atividades.split('|')[1:]:
            lista_atividades.append(Atividade(*atividade.split('-')))
        return lista_atividades

    def enviar_cadastro_atividade(self, mensagem):
        if mensagem.split('|')[0] == '6':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '6':
                return True
        return False

    def cadastrar_tarefa(self):
        atividade_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.id
        titulo = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_titulo.text()
        descricao = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_descricao.text()
        materia_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.materia_id
        turma_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.turma_id
        mensagem = f'6|{atividade_id}|{titulo}|{descricao}|{materia_id}|{turma_id}'
        for num, questao in enumerate(self.atividades_turma[self.QtStack.currentIndex() + 1].questoes):
            enunciado = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_enunciado.text()
            a = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_letra['A'].text()
            b = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_letra['B'].text()
            c = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_letra['C'].text()
            d = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_letra['D'].text()
            e = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].input_letra['E'].text()
            id_questao = self.atividades_turma[self.QtStack.currentIndex(
            ) + 1].questoes[num].questao_id
            mensagem += f'|{id_questao}/{enunciado}/{a}/{b}/{c}/{d}/{e}'
        print(mensagem)
        if self.enviar_cadastro_atividade(mensagem):
            self.criar_pagina_atividade_turma(materia_id, turma_id)
            QMessageBox.about(self, "Sucesso", "Tarefa cadastrada com sucesso")
            self.QtStack.setCurrentIndex(3)
        else:
            QMessageBox.about(self, "Erro", "Erro ao cadastrar tarefa")

    def enviar_cadastro(self, mensagem):
        if mensagem.split('|')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '2':
                return True
        return False

    def botao_logoff(self):
        mensagem = '0'
        self.tela_principal_professor.limpar_paginas()
        self.tela_principal_aluno.limpar_paginas()
        self.tela_principal_aluno.limpar_materias()
        self.client_socket.send(mensagem.encode())
        self.QtStack.setCurrentIndex(0)

    def botao_sair(self):
        mensagem = '-1'
        self.client_socket.send(mensagem.encode())
        self.client_socket.close()
        exit()

    def enviar_login(self, mensagem):
        if mensagem.split('|')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta != '0':
                return resposta
        return False

    def botao_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        mensagem = f'1|{email}|{senha}'

        if email and senha:
            resposta = self.enviar_login(mensagem)
            if resposta:
                if resposta[0] == '1':
                    materia_id = resposta.split('|')[1]
                    for turma in resposta.split('|')[2:]:
                        turma_nome = turma.split('-')[0]
                        turma_id = turma.split('-')[1]
                        atividades = self.pegar_atividades_turma(turma_nome)
                        if not atividades:
                            atividades = None
                        self.tela_principal_professor.add_pagina(
                            f'Turma-{turma_nome}', materia_id, turma_id, atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade_turma)
                    self.tela_principal_professor.inserir_espacamento()
                    self.QtStack.setCurrentIndex(3)
                elif resposta[0] == '2':
                    for materia in resposta.split('|')[1:]:
                        materia_id = materia.split('-')[0]
                        materia_nome = materia.split('-')[1]
                        atividades = self.pegar_atividades(materia_id)
                        self.tela_principal_aluno.add_materia(
                            materia_nome.capitalize(), atividades, pilha_paginas=self.QtStack, funcao_criar_pagina_atividade=self.criar_pagina_atividade)
                    self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
        else:
            QMessageBox.about(self, "Erro", "E-mail ou senha não preenchidos")

    def botao_cadastrar_professor(self):
        email = self.tela_cadastro.professores_caixa_email.text()
        senha1 = self.tela_cadastro.professores_caixa_senha1.text()
        senha2 = self.tela_cadastro.professores_caixa_senha2.text()
        nome = self.tela_cadastro.professores_caixa_nome.text()
        sobrenome = self.tela_cadastro.professores_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.professores_caixa_nascimento.text()
        mensagem = f'2|{email}|{senha1}|{nome}|{sobrenome}|{nascimento}|p'
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

    def botao_cadastrar_aluno(self):
        email = self.tela_cadastro.alunos_caixa_email.text()
        senha1 = self.tela_cadastro.alunos_caixa_senha1.text()
        senha2 = self.tela_cadastro.alunos_caixa_senha2.text()
        nome = self.tela_cadastro.alunos_caixa_nome.text()
        sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.alunos_caixa_nascimento.text()
        turma = self.tela_cadastro.alunos_caixa_turma.text()
        mensagem = f'2|{email}|{senha1}|{nome}|{sobrenome}|{nascimento}|{turma}|a'
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
