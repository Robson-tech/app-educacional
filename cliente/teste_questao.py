from PyQt5 import QtCore, QtGui, QtWidgets


class AtividadeQuestao(QtWidgets.QGroupBox):
    def __init__(self, scrollAreaWidgetContents, num, enunciado=None, alternativas=None, questao_id=None):
        super().__init__(scrollAreaWidgetContents)
        self.questao_id = questao_id
        self.setMinimumSize(QtCore.QSize(825, 300))
        self.setMaximumSize(QtCore.QSize(825, 16777215))
        self.setStyleSheet("background-color: rgb(52, 161, 50);")
        self.setTitle("")
        self.setObjectName("questao")
        self.num_questao = QtWidgets.QLabel(self)
        self.num_questao.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font_num_questao = QtGui.QFont()
        font_num_questao.setPointSize(12)
        self.num_questao.setFont(font_num_questao)
        self.num_questao.setStyleSheet("border-radius: 15px;\n"
"background-color: rgb(252, 88, 20);")
        self.num_questao.setAlignment(QtCore.Qt.AlignCenter)
        self.num_questao.setText(str(num))
        self.num_questao.setObjectName("num_questao")
        self.input_enunciado = QtWidgets.QLineEdit(self)
        self.input_enunciado.setGeometry(QtCore.QRect(50, 20, 761, 81))
        font_input_enunciado = QtGui.QFont()
        font_input_enunciado.setPointSize(12)
        self.input_enunciado.setFont(font_input_enunciado)
        self.input_enunciado.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_enunciado.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.input_enunciado.setObjectName("input_enunciado")
        self.input_letra = {}
        font_input_letra = QtGui.QFont()
        font_input_letra.setPointSize(12)
        self.input_letra['A'] = QtWidgets.QLineEdit(self)
        self.input_letra['A'].setGeometry(QtCore.QRect(50, 140, 113, 20))
        self.input_letra['A'].setFont(font_input_letra)
        self.input_letra['A'].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_letra['A'].setObjectName("input_letra_A")
        self.input_letra['B'] = QtWidgets.QLineEdit(self)
        self.input_letra['B'].setGeometry(QtCore.QRect(50, 170, 113, 20))
        self.input_letra['B'].setFont(font_input_letra)
        self.input_letra['B'].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_letra['B'].setObjectName("input_letra_B")
        self.input_letra['C'] = QtWidgets.QLineEdit(self)
        self.input_letra['C'].setGeometry(QtCore.QRect(50, 200, 113, 20))
        self.input_letra['C'].setFont(font_input_letra)
        self.input_letra['C'].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_letra['C'].setObjectName("input_letra_C")
        self.input_letra['D'] = QtWidgets.QLineEdit(self)
        self.input_letra['D'].setGeometry(QtCore.QRect(50, 230, 113, 20))
        self.input_letra['D'].setFont(font_input_letra)
        self.input_letra['D'].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_letra['D'].setObjectName("input_letra_D")
        self.input_letra['E'] = QtWidgets.QLineEdit(self)
        self.input_letra['E'].setGeometry(QtCore.QRect(50, 260, 113, 20))
        self.input_letra['E'].setFont(font_input_letra)
        self.input_letra['E'].setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_letra['E'].setObjectName("input_letra_E")
        self.selecao = {}
        self.selecao['A'] = QtWidgets.QRadioButton(self)
        self.selecao['A'].setGeometry(QtCore.QRect(30, 140, 16, 16))
        self.selecao['A'].setObjectName("selecao_A")
        self.selecao['B'] = QtWidgets.QRadioButton(self)
        self.selecao['B'].setGeometry(QtCore.QRect(30, 170, 16, 16))
        self.selecao['B'].setObjectName("selecao_B")
        self.selecao['C'] = QtWidgets.QRadioButton(self)
        self.selecao['C'].setGeometry(QtCore.QRect(30, 200, 16, 16))
        self.selecao['C'].setObjectName("selecao_C")
        self.selecao['D'] = QtWidgets.QRadioButton(self)
        self.selecao['D'].setGeometry(QtCore.QRect(30, 230, 16, 16))
        self.selecao['D'].setObjectName("selecao_D")
        self.selecao['E'] = QtWidgets.QRadioButton(self)
        self.selecao['E'].setGeometry(QtCore.QRect(30, 260, 16, 16))
        self.selecao['E'].setObjectName("selecao_E")
        if enunciado:
            self.input_enunciado.setText(enunciado)
        if alternativas:
            for i, letra in enumerate(self.input_letra):
                self.input_letra[letra].setText(alternativas[i])