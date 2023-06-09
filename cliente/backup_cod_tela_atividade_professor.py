# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_AtividadeProfessor_professor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modelos import Questao


class Ui_AtividadeProfessor(object):
    def setupUi(self, AtividadeProfessor, atividade_id=None, materia_id=None, turma_id=None):
        self.atividade_id = atividade_id
        self.materia_id = materia_id
        self.turma_id = turma_id
        self.questoes_bd = {}
        AtividadeProfessor.setObjectName("AtividadeProfessor")
        AtividadeProfessor.resize(900, 580)
        AtividadeProfessor.setMinimumSize(QtCore.QSize(900, 580))
        AtividadeProfessor.setMaximumSize(QtCore.QSize(900, 580))
        AtividadeProfessor.setStyleSheet("background-color: rgb(51, 51, 51);")
        qtRectangle = AtividadeProfessor.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        AtividadeProfessor.move(qtRectangle.topLeft())
        self.scrollArea = QtWidgets.QScrollArea(AtividadeProfessor)
        self.scrollArea.setGeometry(QtCore.QRect(20, 20, 861, 491))
        self.scrollArea.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -38, 843, 577))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input_titulo = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_titulo.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.input_titulo.setFont(font)
        self.input_titulo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_titulo.setText("")
        self.input_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.input_titulo.setObjectName("input_titulo")
        self.verticalLayout.addWidget(self.input_titulo)
        self.input_descricao = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.input_descricao.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_descricao.setFont(font)
        self.input_descricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_descricao.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input_descricao.setObjectName("input_descricao")
        self.verticalLayout.addWidget(self.input_descricao)
        self.num_questoes = 0
        self.questoes = {}
        self.input_enunciado = {}
        self.input_A = {}
        self.input_B = {}
        self.input_C = {}
        self.input_D = {}
        self.input_E = {}
#         self.questoes[num] = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
#         self.questoes[num].setMinimumSize(QtCore.QSize(825, 300))
#         self.questoes[num].setMaximumSize(QtCore.QSize(825, 16777215))
#         self.questoes[num].setStyleSheet("background-color: rgb(52, 161, 50);")
#         self.questoes[num].setTitle("")
#         self.questoes[num].setObjectName("questoes[num]")
#         self.num_questao = QtWidgets.QLabel(self.questoes[num])
#         self.num_questao.setGeometry(QtCore.QRect(10, 10, 30, 30))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.num_questao.setFont(font)
#         self.num_questao.setStyleSheet("border-radius: 15px;\n"
# "background-color: rgb(252, 88, 20);")
#         self.num_questao.setAlignment(QtCore.Qt.AlignCenter)
#         self.num_questao.setObjectName("num_questao")
#         self.input_enunciado[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_enunciado[self.num_questoes].setGeometry(QtCore.QRect(50, 20, 761, 81))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_enunciado[self.num_questoes].setFont(font)
#         self.input_enunciado[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_enunciado[self.num_questoes].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
#         self.input_enunciado[self.num_questoes].setObjectName("input_enunciado[self.num_questoes]")
#         self.input_enunciado[self.num_questoes]
#         self.input_A[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_A[self.num_questoes].setGeometry(QtCore.QRect(50, 140, 113, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_A[self.num_questoes].setFont(font)
#         self.input_A[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_A[self.num_questoes].setText("")
#         self.input_A[self.num_questoes].setObjectName("input_A[self.num_questoes]")
#         self.input_B[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_B[self.num_questoes].setGeometry(QtCore.QRect(50, 170, 113, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_B[self.num_questoes].setFont(font)
#         self.input_B[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_B[self.num_questoes].setText("")
#         self.input_B[self.num_questoes].setObjectName("input_B[self.num_questoes]")
#         self.input_C[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_C[self.num_questoes].setGeometry(QtCore.QRect(50, 200, 113, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_C[self.num_questoes].setFont(font)
#         self.input_C[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_C[self.num_questoes].setText("")
#         self.input_C[self.num_questoes].setObjectName("input_C[self.num_questoes]")
#         self.input_D[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_D[self.num_questoes].setGeometry(QtCore.QRect(50, 230, 113, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_D[self.num_questoes].setFont(font)
#         self.input_D[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_D[self.num_questoes].setText("")
#         self.input_D[self.num_questoes].setObjectName("input_D")
#         self.input_E[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
#         self.input_E[self.num_questoes].setGeometry(QtCore.QRect(50, 260, 113, 20))
#         font = QtGui.QFont()
#         font.setPointSize(12)
#         self.input_E[self.num_questoes].setFont(font)
#         self.input_E[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
#         self.input_E[self.num_questoes].setText("")
#         self.input_E[self.num_questoes].setObjectName("input_E")
#         self.selecao_A = QtWidgets.QRadioButton(self.questoes[num])
#         self.selecao_A.setGeometry(QtCore.QRect(30, 140, 16, 16))
#         self.selecao_A.setText("")
#         self.selecao_A.setObjectName("selecao_A")
#         self.selecao_B = QtWidgets.QRadioButton(self.questoes[num])
#         self.selecao_B.setGeometry(QtCore.QRect(30, 170, 16, 16))
#         self.selecao_B.setText("")
#         self.selecao_B.setObjectName("selecao_B")
#         self.selecao_C = QtWidgets.QRadioButton(self.questoes[num])
#         self.selecao_C.setGeometry(QtCore.QRect(30, 200, 16, 16))
#         self.selecao_C.setText("")
#         self.selecao_C.setObjectName("selecao_C")
#         self.selecao_D = QtWidgets.QRadioButton(self.questoes[num])
#         self.selecao_D.setGeometry(QtCore.QRect(30, 230, 16, 16))
#         self.selecao_D.setText("")
#         self.selecao_D.setObjectName("selecao_D")
#         self.selecao_E = QtWidgets.QRadioButton(self.questoes[num])
#         self.selecao_E.setGeometry(QtCore.QRect(30, 260, 16, 16))
#         self.selecao_E.setText("")
#         self.selecao_E.setObjectName("selecao_E")
#         self.verticalLayout.addWidget(self.questoes[num])
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_voltar = QtWidgets.QPushButton(AtividadeProfessor)
        self.botao_voltar.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_voltar.setFont(font)
        self.botao_voltar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_voltar.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.botao_voltar.setObjectName("botao_voltar")
        self.layoutWidget = QtWidgets.QWidget(AtividadeProfessor)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 530, 861, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botao_add = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_add.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_add.setFont(font)
        self.botao_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_add.setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
"background-color: rgb(255, 255, 255);")
        self.botao_add.setObjectName("botao_add")
        self.horizontalLayout_2.addWidget(self.botao_add)
        self.botao_publicar = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_publicar.setMinimumSize(QtCore.QSize(0, 30))
        self.botao_publicar.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.botao_publicar.setFont(font)
        self.botao_publicar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_publicar.setStyleSheet("border: none;\n"
"border-radius: 15px;\n"
"background-color: rgb(0, 166, 202);")
        self.botao_publicar.setObjectName("botao_publicar")
        self.horizontalLayout_2.addWidget(self.botao_publicar)

        self._translate = QtCore.QCoreApplication.translate
        # self.num_questao.setText(self._translate("AtividadeProfessor", str(self.num_questoes)))
        # self.input_enunciado[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "Enunciado"))
        # self.input_A[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "A"))
        # self.input_B[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "B"))
        # self.input_C[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "C"))
        # self.input_D[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "D"))
        # self.input_E[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "E"))
        self.botao_add.clicked.connect(self.add_questao)
        self.retranslateUi(AtividadeProfessor)
        QtCore.QMetaObject.connectSlotsByName(AtividadeProfessor)

    def add_questao(self, questao_id=None, num=None, enunciado=None, alternativas=None):
        self.questoes[num] = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.questoes[num].setMinimumSize(QtCore.QSize(825, 300))
        self.questoes[num].setMaximumSize(QtCore.QSize(825, 16777215))
        self.questoes[num].setStyleSheet("background-color: rgb(52, 161, 50);")
        self.questoes[num].setTitle("")
        self.questoes[num].setObjectName("questoes[num]")
        self.num_questao = QtWidgets.QLabel(self.questoes[num])
        self.num_questao.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_questao.setFont(font)
        self.num_questao.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(252, 88, 20);")
        self.num_questao.setAlignment(QtCore.Qt.AlignCenter)
        self.num_questao.setObjectName("num_questao")
        self.input_enunciado[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_enunciado[self.num_questoes].setGeometry(QtCore.QRect(50, 20, 761, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_enunciado[self.num_questoes].setFont(font)
        self.input_enunciado[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_enunciado[self.num_questoes].setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input_enunciado[self.num_questoes].setObjectName("input_enunciado[self.num_questoes]")
        self.input_A[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_A[self.num_questoes].setGeometry(QtCore.QRect(50, 140, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_A[self.num_questoes].setFont(font)
        self.input_A[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_A[self.num_questoes].setObjectName("input_A[self.num_questoes]")
        self.input_B[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_B[self.num_questoes].setGeometry(QtCore.QRect(50, 170, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_B[self.num_questoes].setFont(font)
        self.input_B[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_B[self.num_questoes].setObjectName("input_B[self.num_questoes]")
        self.input_C[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_C[self.num_questoes].setGeometry(QtCore.QRect(50, 200, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_C[self.num_questoes].setFont(font)
        self.input_C[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_C[self.num_questoes].setObjectName("input_C[self.num_questoes]")
        self.input_D[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_D[self.num_questoes].setGeometry(QtCore.QRect(50, 230, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_D[self.num_questoes].setFont(font)
        self.input_D[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_D[self.num_questoes].setObjectName("input_D")
        self.input_E[self.num_questoes] = QtWidgets.QLineEdit(self.questoes[num])
        self.input_E[self.num_questoes].setGeometry(QtCore.QRect(50, 260, 113, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_E[self.num_questoes].setFont(font)
        self.input_E[self.num_questoes].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_E[self.num_questoes].setObjectName("input_E")
        self.selecao_A = QtWidgets.QRadioButton(self.questoes[num])
        self.selecao_A.setGeometry(QtCore.QRect(30, 140, 16, 16))
        self.selecao_A.setText("")
        self.selecao_A.setObjectName("selecao_A")
        self.selecao_B = QtWidgets.QRadioButton(self.questoes[num])
        self.selecao_B.setGeometry(QtCore.QRect(30, 170, 16, 16))
        self.selecao_B.setText("")
        self.selecao_B.setObjectName("selecao_B")
        self.selecao_C = QtWidgets.QRadioButton(self.questoes[num])
        self.selecao_C.setGeometry(QtCore.QRect(30, 200, 16, 16))
        self.selecao_C.setText("")
        self.selecao_C.setObjectName("selecao_C")
        self.selecao_D = QtWidgets.QRadioButton(self.questoes[num])
        self.selecao_D.setGeometry(QtCore.QRect(30, 230, 16, 16))
        self.selecao_D.setText("")
        self.selecao_D.setObjectName("selecao_D")
        self.selecao_E = QtWidgets.QRadioButton(self.questoes[num])
        self.selecao_E.setGeometry(QtCore.QRect(30, 260, 16, 16))
        self.selecao_E.setText("")
        self.selecao_E.setObjectName("selecao_E")
        self.input_enunciado[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "Enunciado"))
        self.input_A[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "A"))
        self.input_B[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "B"))
        self.input_C[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "C"))
        self.input_D[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "D"))
        self.input_E[self.num_questoes].setPlaceholderText(self._translate("AtividadeProfessor", "E"))
        self.verticalLayout.addWidget(self.questoes[num])
        if not num:
            self.num_questao.setText(self._translate("AtividadeProfessor", str(self.num_questoes + 1)))
        else:
            self.num_questao.setText(self._translate("AtividadeProfessor", str(num)))
        if enunciado:
            self.input_enunciado[self.num_questoes].setText(enunciado)
        if alternativas:
            self.input_A[self.num_questoes].setText(alternativas[0])
            self.input_B[self.num_questoes].setText(alternativas[1])
            self.input_C[self.num_questoes].setText(alternativas[2])
            self.input_D[self.num_questoes].setText(alternativas[3])
            self.input_E[self.num_questoes].setText(alternativas[4])
        if questao_id:
            self.questoes_bd[self.num_questoes] = Questao(questao_id, self.atividade_id, enunciado, None, alternativas[0], alternativas[1], alternativas[2], alternativas[3], alternativas[4])
        self.num_questoes += 1

    def retranslateUi(self, AtividadeProfessor):
        AtividadeProfessor.setWindowTitle(self._translate("AtividadeProfessor", "Cadastrar Atividade"))
        self.input_titulo.setPlaceholderText(self._translate("AtividadeProfessor", "Título"))
        self.input_descricao.setPlaceholderText(self._translate("AtividadeProfessor", "Descrição"))
        self.botao_add.setText(self._translate("AtividadeProfessor", "+"))
        self.botao_publicar.setText(self._translate("AtividadeProfessor", "Publicar"))
        self.botao_voltar.setText(self._translate("Atividade", "←"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AtividadeProfessor = QtWidgets.QWidget()
    ui = Ui_AtividadeProfessor()
    ui.setupUi(AtividadeProfessor)
    AtividadeProfessor.show()
    sys.exit(app.exec_())
