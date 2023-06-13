import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cod_tela_principal import Ui_TelaPrincipal
from cod_tela_login import Ui_Login
from cod_tela_cadastro import Ui_Cadastro
from backend.sistema import SistemaEducacional, Professor, Aluno


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main, materias):
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_login = Ui_Login()
        self.tela_login.setupUi(self.stack0)
        self.tela_cadastro = Ui_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        self.tela_principal = Ui_TelaPrincipal()
        self.tela_principal.setupUi(self.stack2, materias)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)


class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)

        '''Modificadores'''
        self.sistema = SistemaEducacional()
        self.setupUi(self, self.sistema.materias)
        self.tela_login.botao_login.clicked.connect(self.botao_login)
        self.tela_login.botao_cadastro.clicked.connect(self.botao_cadastrar)
        self.tela_cadastro.alunos_botao_voltar.clicked.connect(self.botao_voltar_cadastro)
        self.tela_cadastro.professores_botao_voltar.clicked.connect(self.botao_voltar_cadastro)
        self.tela_cadastro.alunos_botao_cadastrar.clicked.connect(self.botao_cadastrar_aluno)
        self.tela_cadastro.professores_botao_cadastrar.clicked.connect(self.botao_cadastrar_professor)
        self.tela_principal.botao_sair.clicked.connect(self.botao_sair)

    def botao_login(self):
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        if self.sistema.login(email, senha):
            if isinstance(self.sistema.usuario, Professor):
                for materia in self.sistema.materias:
                    if materia[1] == self.sistema.usuario.id:
                        self.tela_principal.pushButtons[materia[0]].show()
            else:
                for turma in self.sistema.turmas:
                    if turma[1] == self.sistema.usuario.id:
                        self.tela_principal.pushButtons[turma[0]].show()
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
    
    def botao_sair(self):
        self.sistema.logout()
        self.tela_principal.hide_materias()
        self.QtStack.setCurrentIndex(0)
        
    def botao_cadastrar(self):
        self.QtStack.setCurrentIndex(1)

    def botao_voltar_cadastro(self):
        self.QtStack.setCurrentIndex(0)

    def botao_cadastrar_aluno(self):
        email = self.tela_cadastro.alunos_caixa_email.text()
        senha1 = self.tela_cadastro.alunos_caixa_senha1.text()
        senha2 = self.tela_cadastro.alunos_caixa_senha2.text()
        nome = self.tela_cadastro.alunos_caixa_nome.text()
        sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.alunos_caixa_nascimento.text()
        if senha1 == senha2:
            if self.sistema.cadastrar_aluno(email, senha1, nome, sobrenome, nascimento):
                QMessageBox.about(self, "Sucesso", "Aluno cadastrado com sucesso")
                email = self.tela_cadastro.alunos_caixa_email.clear()
                senha1 = self.tela_cadastro.alunos_caixa_senha1.clear()
                senha2 = self.tela_cadastro.alunos_caixa_senha2.clear()
                nome = self.tela_cadastro.alunos_caixa_nome.clear()
                sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.clear()
                nascimento = self.tela_cadastro.alunos_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))
                email = self.tela_cadastro.professores_caixa_email.clear()
                senha1 = self.tela_cadastro.professores_caixa_senha1.clear()
                senha2 = self.tela_cadastro.professores_caixa_senha2.clear()
                nome = self.tela_cadastro.professores_caixa_nome.clear()
                sobrenome = self.tela_cadastro.professores_caixa_sobrenome.clear()
                nascimento = self.tela_cadastro.professores_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "Erro ao cadastrar aluno")
        else:
            QMessageBox.about(self, "Erro", "Senhas não coincidem")
    
    def botao_cadastrar_professor(self):
        email = self.tela_cadastro.professores_caixa_email.text()
        senha1 = self.tela_cadastro.professores_caixa_senha1.text()
        senha2 = self.tela_cadastro.professores_caixa_senha2.text()
        nome = self.tela_cadastro.professores_caixa_nome.text()
        sobrenome = self.tela_cadastro.professores_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.professores_caixa_nascimento.text()
        if senha1 == senha2:
            if self.sistema.cadastrar_professor(email, senha1, nome, sobrenome, nascimento):
                QMessageBox.about(self, "Sucesso", "Professor cadastrado com sucesso")
                email = self.tela_cadastro.alunos_caixa_email.clear()
                senha1 = self.tela_cadastro.alunos_caixa_senha1.clear()
                senha2 = self.tela_cadastro.alunos_caixa_senha2.clear()
                nome = self.tela_cadastro.alunos_caixa_nome.clear()
                sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.clear()
                nascimento = self.tela_cadastro.alunos_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))
                email = self.tela_cadastro.professores_caixa_email.clear()
                senha1 = self.tela_cadastro.professores_caixa_senha1.clear()
                senha2 = self.tela_cadastro.professores_caixa_senha2.clear()
                nome = self.tela_cadastro.professores_caixa_nome.clear()
                sobrenome = self.tela_cadastro.professores_caixa_sobrenome.clear()
                nascimento = self.tela_cadastro.professores_caixa_nascimento.setDate(QtCore.QDate(2000, 1, 1))
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "Usuário já cadastrado")
        else:
            QMessageBox.about(self, "Erro", "Senhas não coincidem")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())