# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modelos import Atividade


class Ui_TelaPrincipalAluno(object):
    def setupUi(self, TelaPrincipalAluno):
        TelaPrincipalAluno.setObjectName("TelaPrincipalAluno")
        TelaPrincipalAluno.resize(900, 580)
        TelaPrincipalAluno.setMinimumSize(QtCore.QSize(900, 580))
        TelaPrincipalAluno.setMaximumSize(QtCore.QSize(900, 580))
        TelaPrincipalAluno.setStyleSheet("background-color: rgb(30, 30, 30);")
        qtRectangle = TelaPrincipalAluno.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        TelaPrincipalAluno.move(qtRectangle.topLeft())
        self.materias = {}
        self.botao_logoff = QtWidgets.QPushButton(TelaPrincipalAluno)
        self.botao_logoff.setGeometry(QtCore.QRect(10, 10, 40, 20))
        self.botao_logoff.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_logoff.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: blue;")
        self.botao_logoff.setObjectName("botao_logoff")
        self.botao_sair = QtWidgets.QPushButton(TelaPrincipalAluno)
        self.botao_sair.setGeometry(QtCore.QRect(240, 10, 40, 20))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: red;")
        self.botao_sair.setObjectName("botao_sair")
        self.logo_escola = QtWidgets.QLabel(TelaPrincipalAluno)
        self.logo_escola.setGeometry(QtCore.QRect(60, 30, 180, 180))
        self.logo_escola.setPixmap(QtGui.QPixmap("img/logo-escola.png"))
        self.logo_escola.setScaledContents(True)
        self.logo_escola.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_escola.setObjectName("logo_escola")
        self.lateral_scrollArea = QtWidgets.QScrollArea(TelaPrincipalAluno)
        self.lateral_scrollArea.setGeometry(QtCore.QRect(0, 210, 290, 361))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lateral_scrollArea.sizePolicy().hasHeightForWidth())
        self.lateral_scrollArea.setSizePolicy(sizePolicy)
        self.lateral_scrollArea.setMinimumSize(QtCore.QSize(290, 330))
        self.lateral_scrollArea.setStyleSheet("border: none;\n"
                                              "background-color: rgb(30, 30, 30);")
        self.lateral_scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lateral_scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAsNeeded)
        self.lateral_scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.lateral_scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lateral_scrollArea.setWidgetResizable(True)
        self.lateral_scrollArea.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.lateral_scrollArea.setObjectName("lateral_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, -17, 283, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lateral_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.conteudo = QtWidgets.QFrame(TelaPrincipalAluno)
        self.conteudo.setGeometry(QtCore.QRect(290, -10, 600, 581))
        self.conteudo.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.stackedWidget = QtWidgets.QStackedWidget(self.conteudo)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 580, 580))
        self.stackedWidget.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pagina_recepcao = QtWidgets.QWidget()
        self.pagina_recepcao.setObjectName("pagina_recepcao")
        self.ultimo_botao = None
        self.stackedWidget.addWidget(self.pagina_recepcao)

        self._translate = QtCore.QCoreApplication.translate
        self.retranslateUi(TelaPrincipalAluno)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalAluno)

    def add_materia(self, nome, atividades, funcao_criar_pagina_atividade=None):
        self.materias[nome] = TelaPrincipalAlunoMateria(
            nome,
            atividades,
            self.scrollAreaWidgetContents,
            self.stackedWidget,
            funcao_criar_pagina_atividade
        )
        self.verticalLayout.addWidget(self.materias[nome].botao)
        self.stackedWidget.addWidget(self.materias[nome].pagina)
        self.stackedWidget.setCurrentWidget(self.pagina_recepcao)

    def inserir_espacamento(self):
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

    def remover_espaçamento(self):
        if isinstance(self.verticalLayout.itemAt(self.verticalLayout.count() - 1), QtWidgets.QSpacerItem):
            self.verticalLayout.removeItem(
                self.verticalLayout.itemAt(self.verticalLayout.count() - 1))

    def limpar_materias(self):
        for materia in self.materias.values():
            self.verticalLayout.removeWidget(materia.botao)
            self.stackedWidget.removeWidget(materia.pagina)
        self.remover_espaçamento()
        self.materias = {}

    def retranslateUi(self, TelaPrincipalAluno):
        TelaPrincipalAluno.setWindowTitle(
            self._translate("TelaPrincipalAluno", "Tela Principal"))
        self.botao_logoff.setText(
            self._translate("TelaPrincipalAluno", "Logoff"))
        self.botao_sair.setText(self._translate("TelaPrincipalAluno", "Sair"))


class TelaPrincipalAlunoMateria:
    def __init__(self, materia_nome: str, atividades: Atividade, scrollAreaWidgetContents: QtWidgets.QWidget, stackedWidget: QtWidgets.QStackedWidget, funcao_criar_pagina_atividade=None):
        self.stackedWidget = stackedWidget
        self.botao = QtWidgets.QPushButton(
            scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao.setFont(font)
        self.botao.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao.setStyleSheet(
            'QPushButton {\n'
            'border-radius: 10px;\n'
            'background-color: rgb(252, 88, 20);\n'
            '}'
        )
        self.botao.setObjectName(materia_nome)
        self.botao.setText(materia_nome)
        self.botao.clicked.connect(self.abrir_pagina)
        self.pagina = TelaPrincipalAlunoMateriaPagina(
            materia_nome,
            atividades,
            funcao_criar_pagina_atividade
        )
        self.pagina.botao_fechar.clicked.connect(self.fechar_pagina)

    def abrir_pagina(self):
        self.stackedWidget.setCurrentWidget(self.pagina)

    def fechar_pagina(self):
        self.stackedWidget.setCurrentIndex(0)


class TelaPrincipalAlunoMateriaPagina(QtWidgets.QWidget):
    def __init__(self, materia_nome: str, atividades: Atividade, funcao_criar_pagina_atividade=None):
        super().__init__()
        self.materia_nome = materia_nome
        self.setObjectName(materia_nome)
        self.rotulo_novas_atividades = QtWidgets.QLabel(self)
        self.rotulo_novas_atividades.setGeometry(QtCore.QRect(10, 10, 560, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.rotulo_novas_atividades.setFont(font)
        self.rotulo_novas_atividades.setStyleSheet("color: white;")
        self.rotulo_novas_atividades.setObjectName("rotulo_novas_atividades")
        self.line = QtWidgets.QFrame(self)
        self.line.setGeometry(QtCore.QRect(10, 50, 560, 7))
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.conteudo_scrollArea = QtWidgets.QScrollArea(self)
        self.conteudo_scrollArea.setGeometry(QtCore.QRect(10, 60, 561, 501))
        self.conteudo_scrollArea.setStyleSheet("border: none;")
        self.conteudo_scrollArea.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOn)
        self.conteudo_scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.conteudo_scrollArea.setWidgetResizable(True)
        self.conteudo_scrollArea.setObjectName("conteudo_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 544, 221))
        self.scrollAreaWidgetContents.setObjectName(
            "scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(
            self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.itens_atividade = {}
        for i, atividade in enumerate(atividades.values()):
            self.itens_atividade.update(
                {atividade.titulo: TelaPrincipalAlunoAtividade(self.scrollAreaWidgetContents)})
            self.gridLayout.addWidget(
                self.itens_atividade[atividade.titulo], i // 4, i % 4, 1, 1)
            if funcao_criar_pagina_atividade:
                self.itens_atividade[atividade.titulo].botao_atividade.clicked.connect(funcao_criar_pagina_atividade(
                    atividade))
            self.itens_atividade[atividade.titulo].label_titulo_atividade.setText(
                atividade.titulo)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.conteudo_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_fechar = QtWidgets.QPushButton(self)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setGeometry(QtCore.QRect(530, 10, 40, 40))
        self.botao_fechar.setFont(font)
        self.botao_fechar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_fechar.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.rotulo_novas_atividades.raise_()
        self.line.raise_()
        self.conteudo_scrollArea.raise_()
        self.botao_fechar.raise_()
        self.rotulo_novas_atividades.setText(materia_nome)
        self.botao_fechar.setText(QtCore.QCoreApplication.translate(
            "TelaPrincipalAluno", u"X", None))


class TelaPrincipalAlunoAtividade(QtWidgets.QGroupBox):
    def __init__(self, scrollAreaWidgetContents):
        super().__init__(scrollAreaWidgetContents)
        self.setMinimumSize(QtCore.QSize(120, 190))
        self.setMaximumSize(QtCore.QSize(120, 190))
        self.setTitle("")
        self.setObjectName("atividade")
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.botao_atividade = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.botao_atividade.sizePolicy().hasHeightForWidth())
        self.botao_atividade.setSizePolicy(sizePolicy)
        self.botao_atividade.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade.setAutoFillBackground(False)
        self.botao_atividade.setStyleSheet("border-radius: 10px;\n"
                                           "background-color: rgb(217, 217, 217);\n"
                                           "background-image: url(img/lista.png);\n"
                                           "background-repeat: no-repeat;\n"
                                           "background-position: center center;")
        self.botao_atividade.setText("")
        self.botao_atividade.setObjectName("botao_atividade")
        self.verticalLayout.addWidget(self.botao_atividade)
        self.label_titulo_atividade = QtWidgets.QLabel(self)
        self.label_titulo_atividade.setMinimumSize(QtCore.QSize(120, 15))
        self.label_titulo_atividade.setMaximumSize(QtCore.QSize(120, 15))
        self.label_titulo_atividade.setStyleSheet(
            "background-color: rgb(253, 255, 102);")
        self.label_titulo_atividade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_titulo_atividade.setObjectName("label_titulo_atividade")
        self.verticalLayout.addWidget(self.label_titulo_atividade)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalAluno = QtWidgets.QWidget()
    ui = Ui_TelaPrincipalAluno()
    ui.setupUi(TelaPrincipalAluno)
    ui.add_materia("Matemática", {
        "MMC e MDC": Atividade(1, "MMC e MDC", "Matemática", 1, 1, 1, {}),
        "Função Afim": Atividade(2, "Função Afim", "Matemática", 1, 1, 1, {}),
        "Radiciação": Atividade(3, "Radiciação", "Matemática", 1, 1, 1, {}),
        "Potência": Atividade(4, "Potência", "Matemática", 1, 1, 1, {}),
        "Equações": Atividade(5, "Equações", "Matemática", 1, 1, 1, {}),
    })
    ui.inserir_espacamento()
    ui.limpar_materias()
    ui.add_materia("Português", {
        "Análise Sintática": Atividade(1, "Análise Sintática", "Português", 1, 1, 1, {}),
        "Análise Morfológica": Atividade(2, "Análise Morfológica", "Português", 1, 1, 1, {}),
        "Análise Semântica": Atividade(3, "Análise Semântica", "Português", 1, 1, 1, {}),
    })
    ui.inserir_espacamento()
    TelaPrincipalAluno.show()
    sys.exit(app.exec_())
