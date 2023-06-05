# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Cadastro(object):
    def setupUi(self, Cadastro):
        Cadastro.setObjectName("Cadastro")
        Cadastro.resize(640, 640)
        Cadastro.setMinimumSize(QtCore.QSize(640, 640))
        Cadastro.setMaximumSize(QtCore.QSize(640, 640))
        Cadastro.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.abas = QtWidgets.QTabWidget(Cadastro)
        self.abas.setGeometry(QtCore.QRect(30, 20, 580, 600))
        self.abas.setTabPosition(QtWidgets.QTabWidget.North)
        self.abas.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.abas.setElideMode(QtCore.Qt.ElideNone)
        self.abas.setDocumentMode(True)
        self.abas.setObjectName("abas")
        self.alunos = QtWidgets.QWidget()
        self.alunos.setStyleSheet("background-color: rgb(52, 161, 50);")
        self.alunos.setObjectName("alunos")
        self.alunos_botao_voltar = QtWidgets.QPushButton(self.alunos)
        self.alunos_botao_voltar.setGeometry(QtCore.QRect(100, 530, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.alunos_botao_voltar.setFont(font)
        self.alunos_botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.alunos_botao_voltar.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(227, 246, 0);")
        self.alunos_botao_voltar.setObjectName("alunos_botao_voltar")
        self.alunos_caixa_senha1 = QtWidgets.QLineEdit(self.alunos)
        self.alunos_caixa_senha1.setGeometry(QtCore.QRect(55, 377, 470, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.alunos_caixa_senha1.setFont(font)
        self.alunos_caixa_senha1.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.alunos_caixa_senha1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.alunos_caixa_senha1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alunos_caixa_senha1.setObjectName("alunos_caixa_senha1")
        self.alunos_caixa_senha2 = QtWidgets.QLineEdit(self.alunos)
        self.alunos_caixa_senha2.setGeometry(QtCore.QRect(55, 460, 470, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.alunos_caixa_senha2.setFont(font)
        self.alunos_caixa_senha2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.alunos_caixa_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.alunos_caixa_senha2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alunos_caixa_senha2.setObjectName("alunos_caixa_senha2")
        self.alunos_caixa_nome = QtWidgets.QLineEdit(self.alunos)
        self.alunos_caixa_nome.setGeometry(QtCore.QRect(55, 45, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alunos_caixa_nome.setFont(font)
        self.alunos_caixa_nome.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.alunos_caixa_nome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alunos_caixa_nome.setObjectName("alunos_caixa_nome")
        self.alunos_caixa_email = QtWidgets.QLineEdit(self.alunos)
        self.alunos_caixa_email.setGeometry(QtCore.QRect(55, 294, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alunos_caixa_email.setFont(font)
        self.alunos_caixa_email.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.alunos_caixa_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alunos_caixa_email.setObjectName("alunos_caixa_email")
        self.alunos_caixa_sobrenome = QtWidgets.QLineEdit(self.alunos)
        self.alunos_caixa_sobrenome.setGeometry(QtCore.QRect(55, 128, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.alunos_caixa_sobrenome.setFont(font)
        self.alunos_caixa_sobrenome.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.alunos_caixa_sobrenome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.alunos_caixa_sobrenome.setObjectName("alunos_caixa_sobrenome")
        self.alunos_botao_cadastrar = QtWidgets.QPushButton(self.alunos)
        self.alunos_botao_cadastrar.setGeometry(QtCore.QRect(335, 530, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.alunos_botao_cadastrar.setFont(font)
        self.alunos_botao_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.alunos_botao_cadastrar.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(11, 97, 144);")
        self.alunos_botao_cadastrar.setObjectName("alunos_botao_cadastrar")
        self.dateEdit = QtWidgets.QDateEdit(self.alunos)
        self.dateEdit.setGeometry(QtCore.QRect(55, 211, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"color: rgb(102, 102, 102);")
        self.dateEdit.setObjectName("dateEdit")
        self.abas.addTab(self.alunos, "")
        self.professores = QtWidgets.QWidget()
        self.professores.setStyleSheet("background-color: rgb(52, 161, 50);")
        self.professores.setObjectName("professores")
        self.professores_caixa_email = QtWidgets.QLineEdit(self.professores)
        self.professores_caixa_email.setGeometry(QtCore.QRect(55, 294, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.professores_caixa_email.setFont(font)
        self.professores_caixa_email.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.professores_caixa_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.professores_caixa_email.setObjectName("professores_caixa_email")
        self.professores_caixa_senha1 = QtWidgets.QLineEdit(self.professores)
        self.professores_caixa_senha1.setGeometry(QtCore.QRect(55, 377, 470, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.professores_caixa_senha1.setFont(font)
        self.professores_caixa_senha1.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.professores_caixa_senha1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.professores_caixa_senha1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.professores_caixa_senha1.setObjectName("professores_caixa_senha1")
        self.professores_caixa_senha2 = QtWidgets.QLineEdit(self.professores)
        self.professores_caixa_senha2.setGeometry(QtCore.QRect(55, 460, 470, 53))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.professores_caixa_senha2.setFont(font)
        self.professores_caixa_senha2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.professores_caixa_senha2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.professores_caixa_senha2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.professores_caixa_senha2.setObjectName("professores_caixa_senha2")
        self.professores_caixa_nome = QtWidgets.QLineEdit(self.professores)
        self.professores_caixa_nome.setGeometry(QtCore.QRect(55, 45, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.professores_caixa_nome.setFont(font)
        self.professores_caixa_nome.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.professores_caixa_nome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.professores_caixa_nome.setObjectName("professores_caixa_nome")
        self.professores_caixa_sobrenome = QtWidgets.QLineEdit(self.professores)
        self.professores_caixa_sobrenome.setGeometry(QtCore.QRect(55, 128, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.professores_caixa_sobrenome.setFont(font)
        self.professores_caixa_sobrenome.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);")
        self.professores_caixa_sobrenome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.professores_caixa_sobrenome.setObjectName("professores_caixa_sobrenome")
        self.professores_botao_cadastrar = QtWidgets.QPushButton(self.professores)
        self.professores_botao_cadastrar.setGeometry(QtCore.QRect(335, 530, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.professores_botao_cadastrar.setFont(font)
        self.professores_botao_cadastrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.professores_botao_cadastrar.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(11, 97, 144);")
        self.professores_botao_cadastrar.setObjectName("professores_botao_cadastrar")
        self.professores_botao_voltar = QtWidgets.QPushButton(self.professores)
        self.professores_botao_voltar.setGeometry(QtCore.QRect(100, 530, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.professores_botao_voltar.setFont(font)
        self.professores_botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.professores_botao_voltar.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(227, 246, 0);")
        self.professores_botao_voltar.setObjectName("professores_botao_voltar")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.professores)
        self.dateEdit_2.setGeometry(QtCore.QRect(55, 211, 470, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"color: rgb(102, 102, 102);")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.abas.addTab(self.professores, "")

        self.retranslateUi(Cadastro)
        self.abas.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Cadastro)

    def retranslateUi(self, Cadastro):
        _translate = QtCore.QCoreApplication.translate
        Cadastro.setWindowTitle(_translate("Cadastro", "Cadastro"))
        self.alunos_botao_voltar.setText(_translate("Cadastro", "Voltar"))
        self.alunos_caixa_senha1.setPlaceholderText(_translate("Cadastro", "Senha"))
        self.alunos_caixa_senha2.setPlaceholderText(_translate("Cadastro", "Repetir Senha"))
        self.alunos_caixa_nome.setPlaceholderText(_translate("Cadastro", "Nome"))
        self.alunos_caixa_email.setPlaceholderText(_translate("Cadastro", "E-mail"))
        self.alunos_caixa_sobrenome.setPlaceholderText(_translate("Cadastro", "Sobrenome"))
        self.alunos_botao_cadastrar.setText(_translate("Cadastro", "Cadastrar"))
        self.abas.setTabText(self.abas.indexOf(self.alunos), _translate("Cadastro", "Aluno"))
        self.professores_caixa_email.setPlaceholderText(_translate("Cadastro", "E-mail"))
        self.professores_caixa_senha1.setPlaceholderText(_translate("Cadastro", "Senha"))
        self.professores_caixa_senha2.setPlaceholderText(_translate("Cadastro", "Repetir Senha"))
        self.professores_caixa_nome.setPlaceholderText(_translate("Cadastro", "Nome"))
        self.professores_caixa_sobrenome.setPlaceholderText(_translate("Cadastro", "Sobrenome"))
        self.professores_botao_cadastrar.setText(_translate("Cadastro", "Cadastrar"))
        self.professores_botao_voltar.setText(_translate("Cadastro", "Voltar"))
        self.abas.setTabText(self.abas.indexOf(self.professores), _translate("Cadastro", "Professor"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Cadastro = QtWidgets.QWidget()
    ui = Ui_Cadastro()
    ui.setupUi(Cadastro)
    Cadastro.show()
    sys.exit(app.exec_())
