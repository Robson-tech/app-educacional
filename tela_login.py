# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(500, 500)
        Login.setMinimumSize(QtCore.QSize(500, 500))
        Login.setMaximumSize(QtCore.QSize(500, 500))
        Login.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.background_login = QtWidgets.QFrame(Login)
        self.background_login.setGeometry(QtCore.QRect(30, 30, 444, 422))
        self.background_login.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(7, 66, 22);")
        self.background_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_login.setObjectName("background_login")
        self.background_foto = QtWidgets.QFrame(self.background_login)
        self.background_foto.setGeometry(QtCore.QRect(140, 30, 170, 170))
        self.background_foto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background_foto.setStyleSheet("border-radius: 85px;\n"
"background-color: rgb(217, 217, 217);")
        self.background_foto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_foto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_foto.setObjectName("background_foto")
        self.botao_login = QtWidgets.QPushButton(Login)
        self.botao_login.setGeometry(QtCore.QRect(266, 375, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setKerning(True)
        self.botao_login.setFont(font)
        self.botao_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_login.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(11, 97, 144);")
        self.botao_login.setObjectName("botao_login")
        self.caixa_senha = QtWidgets.QLineEdit(Login)
        self.caixa_senha.setGeometry(QtCore.QRect(79, 310, 350, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.caixa_senha.setFont(font)
        self.caixa_senha.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(170, 170, 170);")
        self.caixa_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.caixa_senha.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.caixa_senha.setObjectName("caixa_senha")
        self.botao_cadastro = QtWidgets.QPushButton(Login)
        self.botao_cadastro.setGeometry(QtCore.QRect(89, 375, 150, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.botao_cadastro.setFont(font)
        self.botao_cadastro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_cadastro.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(227, 246, 0);")
        self.botao_cadastro.setObjectName("botao_cadastro")
        self.caixa_email = QtWidgets.QLineEdit(Login)
        self.caixa_email.setGeometry(QtCore.QRect(79, 242, 350, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.caixa_email.setFont(font)
        self.caixa_email.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(170, 170, 170);")
        self.caixa_email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.caixa_email.setObjectName("caixa_email")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.botao_login.setText(_translate("Login", "Logar"))
        self.caixa_senha.setPlaceholderText(_translate("Login", "Senha"))
        self.botao_cadastro.setText(_translate("Login", "Cadastrar"))
        self.caixa_email.setPlaceholderText(_translate("Login", "E-mail"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
