# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_AtividadeProfessor_professor.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modelos import Atividade, Questao


class Ui_AtividadeProfessor(object):
    def setupUi(self, AtividadeProfessor, atividade=None):
        self.atividade = atividade
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
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_principal = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_principal.setGeometry(
            QtCore.QRect(0, -38, 843, 577))
        self.scrollAreaWidgetContents_principal.setObjectName(
            "scrollAreaWidgetContents_principal")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents_principal)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.input_titulo = QtWidgets.QLineEdit(
            self.scrollAreaWidgetContents_principal)
        self.input_titulo.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.input_titulo.setFont(font)
        self.input_titulo.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_titulo.setText("")
        self.input_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.input_titulo.setObjectName("input_titulo")
        self.horizontalLayout_3.addWidget(self.input_titulo)
        self.input_comboBox_materia = QtWidgets.QComboBox(
            self.scrollAreaWidgetContents_principal)
        self.input_comboBox_materia.setMinimumSize(QtCore.QSize(300, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.input_comboBox_materia.setFont(font)
        self.input_comboBox_materia.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_comboBox_materia.setEditable(False)
        self.input_comboBox_materia.setObjectName("input_comboBox_materia")
        self.horizontalLayout_3.addWidget(
            self.input_comboBox_materia)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.input_descricao = QtWidgets.QPlainTextEdit(
            self.scrollAreaWidgetContents_principal)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_descricao.setFont(font)
        self.input_descricao.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_descricao.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_descricao.setTabChangesFocus(True)
        self.input_descricao.setObjectName("input_descricao")
        self.verticalLayout.addWidget(self.input_descricao)
        self.questoes = {}
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_principal)
        self.botao_voltar = QtWidgets.QPushButton(AtividadeProfessor)
        self.botao_voltar.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_voltar.setFont(font)
        self.botao_voltar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_voltar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_voltar.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.botao_voltar.setObjectName("botao_voltar")
        self.layoutWidget = QtWidgets.QWidget(AtividadeProfessor)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 530, 861, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.botao_add_questao = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_add_questao.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_add_questao.setFont(font)
        self.botao_add_questao.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_add_questao.setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
                                             "background-color: rgb(255, 255, 255);")
        self.botao_add_questao.setObjectName("botao_add_questao")
        self.horizontalLayout_2.addWidget(self.botao_add_questao)
        self.botao_publicar = QtWidgets.QPushButton(self.layoutWidget)
        self.botao_publicar.setMinimumSize(QtCore.QSize(0, 30))
        self.botao_publicar.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.botao_publicar.setFont(font)
        self.botao_publicar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_publicar.setStyleSheet("border: none;\n"
                                          "border-radius: 15px;\n"
                                          "background-color: rgb(0, 166, 202);")
        self.botao_publicar.setObjectName("botao_publicar")
        self.horizontalLayout_2.addWidget(self.botao_publicar)
        for q in atividade.questoes.values() if atividade and atividade.questoes else []:
            num = len(self.questoes)
            self.questoes[num] = AtividadeQuestao(
                self.scrollAreaWidgetContents_principal, q.enunciado, q.resposta, [q.letra_a, q.letra_b, q.letra_c, q.letra_d, q.letra_e], q.id)
            self.questoes[num].num_questao.setText(str(num + 1))
            self.verticalLayout.addWidget(self.questoes[num])

        self._translate = QtCore.QCoreApplication.translate
        self.botao_add_questao.clicked.connect(
            self.botao_add_nova_questao_funcao)
        self.retranslateUi(AtividadeProfessor)
        self.input_comboBox_materia.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AtividadeProfessor)

    def botao_add_nova_questao_funcao(self):
        num = len(self.questoes)
        self.questoes[num] = AtividadeQuestao(
            self.scrollAreaWidgetContents_principal)
        self.questoes[num].num_questao.setText(str(num + 1))
        self.questoes[num].input_enunciado.setPlaceholderText(
            self._translate("AtividadeProfessor", "Enunciado"))
        self.questoes[num].input_letra['a'].setPlaceholderText(
            self._translate("AtividadeProfessor", "A"))
        self.questoes[num].input_letra['b'].setPlaceholderText(
            self._translate("AtividadeProfessor", "B"))
        self.questoes[num].input_letra['c'].setPlaceholderText(
            self._translate("AtividadeProfessor", "C"))
        self.questoes[num].input_letra['d'].setPlaceholderText(
            self._translate("AtividadeProfessor", "D"))
        self.questoes[num].input_letra['e'].setPlaceholderText(
            self._translate("AtividadeProfessor", "E"))
        self.verticalLayout.addWidget(self.questoes[num])

    def retranslateUi(self, AtividadeProfessor):
        AtividadeProfessor.setWindowTitle(self._translate(
            "AtividadeProfessor", "Cadastrar Atividade"))
        self.input_titulo.setPlaceholderText(
            self._translate("AtividadeProfessor", "Título"))
        self.input_comboBox_materia.setCurrentText(
            self._translate("Atividade", "Matéria"))
        self.input_descricao.setPlaceholderText(
            self._translate("AtividadeProfessor", "Descrição"))
        self.botao_add_questao.setText(
            self._translate("AtividadeProfessor", "+"))
        self.botao_publicar.setText(
            self._translate("AtividadeProfessor", "Publicar"))
        self.botao_voltar.setText(self._translate("Atividade", "←"))


class AtividadeQuestao(QtWidgets.QGroupBox):
    def __init__(self, scrollAreaWidgetContents_principal, enunciado=None, resposta=None, alternativas=None, questao_id=None):
        super().__init__(scrollAreaWidgetContents_principal)
        self.questao_id = questao_id
        self.setMinimumSize(QtCore.QSize(835, 300))
        self.setMaximumSize(QtCore.QSize(835, 16777215))
        self.setStyleSheet("background-color: rgb(52, 161, 50);")
        self.setTitle("")
        self.setObjectName("questao")
        self.gridLayout_principal = QtWidgets.QGridLayout(self)
        self.gridLayout_principal.setObjectName("gridLayout_principal")
        self.num_questao = QtWidgets.QLabel(self)
        self.num_questao.setMinimumSize(QtCore.QSize(30, 30))
        self.num_questao.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_questao.setFont(font)
        self.num_questao.setStyleSheet("border-radius: 15px;\n"
                                       "background-color: rgb(252, 88, 20);")
        self.num_questao.setAlignment(QtCore.Qt.AlignCenter)
        self.num_questao.setObjectName("num_questao")
        self.gridLayout_principal.addWidget(self.num_questao, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout_principal.addWidget(self.label, 0, 1, 1, 1)
        self.num_questao = QtWidgets.QLabel(self)
        self.num_questao.setMinimumSize(QtCore.QSize(30, 30))
        self.num_questao.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num_questao.setFont(font)
        self.num_questao.setStyleSheet("border-radius: 15px;\n"
                                       "background-color: rgb(252, 88, 20);")
        self.num_questao.setAlignment(QtCore.Qt.AlignCenter)
        self.num_questao.setObjectName("num_questao")
        self.gridLayout_principal.addWidget(self.num_questao, 0, 0, 1, 1)
        self.input_enunciado = QtWidgets.QPlainTextEdit(self)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_enunciado.setFont(font)
        self.input_enunciado.setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_enunciado.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_enunciado.setTabChangesFocus(True)
        self.input_enunciado.setObjectName("input_enunciado")
        self.gridLayout_principal.addWidget(self.input_enunciado, 1, 1, 1, 1)
        # inicio
        self.input_letra = {}
        self.selecao = {}
        font_input_letra = QtGui.QFont()
        font_input_letra.setPointSize(12)
        self.gridLayout_alternativas = QtWidgets.QGridLayout()
        self.gridLayout_alternativas.setObjectName("gridLayout_alternativas")
        self.input_letra['a'] = QtWidgets.QLineEdit(self)
        self.input_letra['a'].setFont(font_input_letra)
        self.input_letra['a'].setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_letra['a'].setText("")
        self.input_letra['a'].setObjectName("input_A")
        self.input_letra['b'] = QtWidgets.QLineEdit(self)
        self.input_letra['b'].setFont(font_input_letra)
        self.input_letra['b'].setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_letra['b'].setText("")
        self.input_letra['b'].setObjectName("input_B")
        self.input_letra['c'] = QtWidgets.QLineEdit(self)
        self.input_letra['c'].setFont(font_input_letra)
        self.input_letra['c'].setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_letra['c'].setText("")
        self.input_letra['c'].setObjectName("input_C")
        self.input_letra['d'] = QtWidgets.QLineEdit(self)
        self.input_letra['d'].setFont(font_input_letra)
        self.input_letra['d'].setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_letra['d'].setText("")
        self.input_letra['d'].setObjectName("input_D")
        self.input_letra['e'] = QtWidgets.QLineEdit(self)
        self.input_letra['e'].setFont(font_input_letra)
        self.input_letra['e'].setStyleSheet(
            "background-color: rgb(255, 255, 255);")
        self.input_letra['e'].setText("")
        self.input_letra['e'].setObjectName("input_E")
        self.selecao['a'] = QtWidgets.QRadioButton(self)
        self.selecao['a'].setText("")
        self.selecao['a'].setObjectName("selecao_A")
        self.selecao['b'] = QtWidgets.QRadioButton(self)
        self.selecao['b'].setText("")
        self.selecao['b'].setObjectName("selecao_B")
        self.selecao['c'] = QtWidgets.QRadioButton(self)
        self.selecao['c'].setText("")
        self.selecao['c'].setObjectName("selecao_C")
        self.selecao['d'] = QtWidgets.QRadioButton(self)
        self.selecao['d'].setText("")
        self.selecao['d'].setObjectName("selecao_D")
        self.selecao['e'] = QtWidgets.QRadioButton(self)
        self.selecao['e'].setText("")
        self.selecao['e'].setObjectName("selecao_E")
        self.gridLayout_alternativas.addWidget(
            self.input_letra['a'], 0, 1, 1, 1)
        self.gridLayout_alternativas.addWidget(
            self.input_letra['b'], 1, 1, 1, 1)
        self.gridLayout_alternativas.addWidget(
            self.input_letra['c'], 2, 1, 1, 1)
        self.gridLayout_alternativas.addWidget(
            self.input_letra['d'], 3, 1, 1, 1)
        self.gridLayout_alternativas.addWidget(
            self.input_letra['e'], 4, 1, 1, 1)
        self.gridLayout_alternativas.addWidget(self.selecao['a'], 0, 0, 1, 1)
        self.gridLayout_alternativas.addWidget(self.selecao['b'], 1, 0, 1, 1)
        self.gridLayout_alternativas.addWidget(self.selecao['c'], 2, 0, 1, 1)
        self.gridLayout_alternativas.addWidget(self.selecao['d'], 3, 0, 1, 1)
        self.gridLayout_alternativas.addWidget(self.selecao['e'], 4, 0, 1, 1)
        self.gridLayout_principal.addLayout(
            self.gridLayout_alternativas, 2, 1, 1, 1)
        # fim
        if enunciado:
            self.input_enunciado.setPlainText(enunciado)
        if alternativas:
            for i, letra in enumerate(self.input_letra):
                self.input_letra[letra].setText(alternativas[i])
        if resposta and resposta in self.selecao:
            self.selecao[resposta].setChecked(True)

    def alternativa_correta(self):
        for letra, alternativa in self.selecao.items():
            if alternativa.isChecked():
                return letra


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AtividadeProfessor = QtWidgets.QWidget()
    ui = Ui_AtividadeProfessor()
    ui.setupUi(AtividadeProfessor, Atividade(1, 'função afim', 'atividade de função',
               1, 1, 1, {1: Questao(1, 1, 'enunciado', 'a', 'a', 'b', 'c', 'd', 'e')}))
    AtividadeProfessor.show()
    sys.exit(app.exec_())
