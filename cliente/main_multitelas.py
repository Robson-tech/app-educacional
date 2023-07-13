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
from modelos import Professor, Aluno, Materia, Atividade, Questao
# pyuic5 -x tela_atividade_professor.ui -o tela_atividade_professor.py


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack = []
        self.atividades = {}
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


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        '''Modificadores'''
        self._usuario = None
        self._materias = {}
        ip = 'LOCALHOST'
        port = 5000
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)
        if self._materias == {}:
            resposta = self.client_socket.recv(1024).decode().split('|')
            for materia in resposta[1].split(',')[:-1]:
                materia_id = materia.split('-')[0]
                materia_nome = materia.split('-')[1]
                self._materias.update(
                    {materia_id: Materia(materia_id, materia_nome)})
                atividades = self.get_atividades_materia(materia_id)
                self.tela_principal_aluno.add_materia(
                    materia_nome.capitalize(), atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade)
            self.tela_principal_aluno.inserir_espacamento()
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

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario_id):
        self._usuario = usuario_id

    @property
    def materias(self):
        return self._materias

    def get_materias_id(self, materia_nome):
        for materia in self._materias.values():
            if materia.nome == materia_nome:
                return materia.id
        return None

    def get_atividade(self, id_atividade):
        self.client_socket.send(f'4|{id_atividade}'.encode())
        questoes = self.client_socket.recv(1024).decode().split('|')
        lista_questoes = []
        while questoes[0] == '4':
            lista_questoes.append(Questao(*questoes[1].split(';;')))
            self.client_socket.send('4'.encode())
            questoes = self.client_socket.recv(1024).decode().split('|')
        atividade_campos = questoes[1].split('//')
        if atividade_campos[0] == 'None':
            return None
        return Atividade(*atividade_campos, lista_questoes)

    def criar_pagina_atividade(self, atividade):
        self.atividades.update({atividade.id: Ui_TelaAtividade()})
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        self.atividades[atividade.id].setupUi(self.stack[-1], atividade)
        self.QtStack.addWidget(self.stack[-1])
        for i, questao in enumerate(atividade.questoes.values()) if atividade.questoes else []:
            self.atividades[atividade.id].add_questao(i + 1, questao.enunciado, questao.resposta, [
                questao.letra_a, questao.letra_b, questao.letra_c, questao.letra_d, questao.letra_e])
        self.atividades[atividade.id].add_rodape()

        def voltar_atividade():
            self.QtStack.setCurrentIndex(2)
        self.atividades[atividade.id].botao_voltar.clicked.connect(
            voltar_atividade)

        def ir_para_pagina_atividade():
            self.QtStack.setCurrentWidget(novo)

        def submeter_atividade():
            self.submeter_atividade(atividade.id)

        self.atividades[atividade.id].botao_publicar.clicked.connect(
            submeter_atividade)
        return ir_para_pagina_atividade

    def criar_pagina_atividade_turma(self, turma_id, materia=None, atividade=None):
        titulo = len(self.stack) + 1
        self.atividades_turma[titulo] = Ui_AtividadeProfessor()
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        if atividade:
            self.atividades_turma[titulo].setupUi(self.stack[-1], atividade)
            self.atividades_turma[titulo].input_titulo.setText(
                atividade.titulo)
            self.atividades_turma[titulo].input_descricao.setPlainText(
                atividade.descricao)
            self.atividades_turma[titulo].input_materia.setText(
                self._materias[materia].nome)
        else:
            self.atividades_turma[titulo].setupUi(
                self.stack[-1], Atividade(None, None, None, None, turma_id, materia, None))
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

    def get_atividades_materia(self, materia_id):
        self.client_socket.send(f'3|{materia_id}'.encode())
        atividades = self.client_socket.recv(32784).decode().split('|')
        lista_atividades = {}
        for atividade in atividades[1:]:
            atividade_campos = atividade.split('//')[:6]
            lista_questoes = {}
            for questao in atividade.split('//')[6:]:
                questao_campos = questao.split(';;')
                lista_questoes.update(
                    {questao_campos[0]: Questao(*questao_campos)})
            lista_atividades.update(
                {atividade_campos[0]: Atividade(*atividade_campos, lista_questoes)})
        return lista_atividades

    def get_atividades_turma_professor(self, turma_id, professor_id):
        self.client_socket.send(f'5|{turma_id},{professor_id}'.encode())
        atividades = self.client_socket.recv(32784).decode().split('|')
        if len(atividades) == 1:
            return None
        lista_atividades = []
        for atividade in atividades[1:]:
            atividade_campos = atividade.split('//')[:6]
            lista_questoes = {}
            for questao in atividade.split('//')[6:]:
                questao_campos = questao.split(';;')
                lista_questoes.update(
                    {questao_campos[0]: Questao(*questao_campos)})
            lista_atividades.append(
                Atividade(*atividade_campos, lista_questoes))
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
            self.QtStack.currentIndex() + 1].input_descricao.toPlainText()
        materia = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_materia.text().capitalize()
        turma_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.turma_id
        materia_id = self.get_materias_id(materia)
        if materia_id:
            mensagem = f'6|{atividade_id}|{titulo}|{descricao}|{materia_id}|{turma_id}'
            for num in enumerate(self.atividades_turma[self.QtStack.currentIndex() + 1].questoes):
                enunciado = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_enunciado.toPlainText()
                a = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['a'].text()
                b = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['b'].text()
                c = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['c'].text()
                d = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['d'].text()
                e = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['e'].text()
                alternativa = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].alternativa_correta()
                id_questao = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].questao_id
                mensagem += f'|{id_questao}//{enunciado}//{alternativa}//{a}//{b}//{c}//{d}//{e}'
            if self.enviar_cadastro_atividade(mensagem):
                self.criar_pagina_atividade_turma(turma_id, materia)
                QMessageBox.about(
                    self, "Sucesso", "Tarefa cadastrada com sucesso")
                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.about(self, "Erro", "Erro ao cadastrar tarefa")
        else:
            QMessageBox.about(self, "Erro", "Matéria não encontrada")

    def submeter_atividade(self, atividade_id):
        aluno_id = self.usuario.id
        mensagem = f'7|{atividade_id}|{aluno_id}'
        acertos = 0
        for q in self.atividades[atividade_id].questoes:
            if self.atividades[atividade_id].questoes[q].alternativa_selecionada() == self.atividades[atividade_id].questoes[q].resposta:
                acertos += 1
        mensagem += f'|{acertos}'
        self.client_socket.send(mensagem.encode())
        resposta = self.client_socket.recv(1024).decode()
        if resposta and resposta == '7':
            QMessageBox.about(
                self, "Sucesso", "Atividade submetida com sucesso")
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.about(self, "Erro", "Erro ao submeter atividade")

    def enviar_cadastro(self, mensagem):
        if mensagem.split('|')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '2':
                return True
        return False

    def botao_logoff(self):
        mensagem = '0'
        self.usuario = None
        self.tela_principal_professor.limpar_paginas()
        self.tela_principal_aluno.limpar_paginas()
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
            resposta = self.client_socket.recv(1024).decode().split('|')
            if resposta and resposta[0] == '0':
                return False
            elif resposta and resposta[0] == '1':
                self.usuario = Professor(
                    *resposta[1].split(','), materias_professor=resposta[2].split(',')[:-1])
            elif resposta and resposta[0] == '2':
                self.usuario = Aluno(*resposta[1].split(','))
            resposta = self.client_socket.recv(1024).decode().split('|')
            if resposta and resposta != '0':
                return resposta
        return False

    def botao_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        mensagem = f'1|{email},{senha}'

        if email and senha:
            resposta = self.enviar_login(mensagem)
            if resposta:
                if resposta[0] == '1':
                    for turma in resposta[2].split(',')[:-1]:
                        turma_id = turma.split('-')[0]
                        turma_nome = turma.split('-')[1]
                        atividades = self.get_atividades_turma_professor(
                            turma_id, self._usuario.id)
                        self.tela_principal_professor.add_pagina(
                            f'Turma-{turma_nome}', turma_id, atividades=atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade_turma)
                    self.tela_principal_professor.inserir_espacamento()
                    self.QtStack.setCurrentIndex(3)
                elif resposta[0] == '2':
                    for materia in self.materias.values():
                        atividades = self.get_atividades_materia(materia.id)
                        self.tela_principal_aluno.add_pagina(
                            materia.nome.capitalize(), atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade)
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
        mensagem = f'2|{email},{senha1},{nome},{sobrenome},{nascimento},p'
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
        mensagem = f'2|{email},{senha1},{nome},{sobrenome},{nascimento},{turma},a'
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
