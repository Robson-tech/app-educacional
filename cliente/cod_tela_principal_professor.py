import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from modelos import Atividade


class Ui_TelaPrincipalProfessor(object):
    def setupUi(self, TelaPrincipalProfessor):
        TelaPrincipalProfessor.setObjectName("TelaPrincipalProfessor")
        TelaPrincipalProfessor.resize(900, 580)
        TelaPrincipalProfessor.setMinimumSize(QtCore.QSize(900, 580))
        TelaPrincipalProfessor.setMaximumSize(QtCore.QSize(900, 580))
        TelaPrincipalProfessor.setStyleSheet(
            "background-color: rgb(30, 30, 30);")
        qtRectangle = TelaPrincipalProfessor.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        TelaPrincipalProfessor.move(qtRectangle.topLeft())
        self.paginas = {}
        self.conteudo = QtWidgets.QFrame(TelaPrincipalProfessor)
        self.conteudo.setGeometry(QtCore.QRect(290, -10, 600, 581))
        self.conteudo.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.stackedWidget = QtWidgets.QStackedWidget(self.conteudo)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 580, 580))
        self.stackedWidget.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_recepcao = QtWidgets.QWidget()
        self.page_recepcao.setObjectName("page_recepcao")
        self.stackedWidget.addWidget(self.page_recepcao)
        self.botao_logoff = QtWidgets.QPushButton(TelaPrincipalProfessor)
        self.botao_logoff.setGeometry(QtCore.QRect(10, 10, 40, 20))
        self.botao_logoff.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_logoff.setStyleSheet("border-radius: 10px;\n"
                                        "background-color: blue;")
        self.botao_logoff.setObjectName("botao_logoff")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 290, 361))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(
            self.scrollAreaWidgetContents)
        self.spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollArea = QtWidgets.QScrollArea(TelaPrincipalProfessor)
        self.scrollArea.setGeometry(QtCore.QRect(0, 210, 300, 361))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 330))
        self.scrollArea.setStyleSheet("border: none;\n"
                                      "background-color: rgb(30, 30, 30);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_sair = QtWidgets.QPushButton(TelaPrincipalProfessor)
        self.botao_sair.setGeometry(QtCore.QRect(240, 10, 40, 20))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("border-radius: 10px;\n"
                                      "background-color: red;")
        self.botao_sair.setObjectName("botao_sair")
        self.logo_escola = QtWidgets.QLabel(TelaPrincipalProfessor)
        self.logo_escola.setGeometry(QtCore.QRect(60, 30, 180, 180))
        self.logo_escola.setPixmap(QtGui.QPixmap("img/logo-escola.png"))
        self.logo_escola.setScaledContents(True)
        self.logo_escola.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_escola.setObjectName("logo_escola")

        self._translate = QtCore.QCoreApplication.translate
        self.retranslateUi(TelaPrincipalProfessor)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalProfessor)

    def add_pagina(self, nome_turma, turma_id, atividades=None, funcao_criar_pagina_atividade=None):
        self.paginas[nome_turma] = PaginaTurma(nome_turma, turma_id, self.scrollAreaWidgetContents,
                                               self.verticalLayout, self._translate, atividades_turma=atividades, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade)

        def alterar_pagina():
            if self.stackedWidget.currentWidget().objectName() == nome_turma:
                return
            elif self.stackedWidget.currentWidget().objectName() != "page_recepcao":
                self.paginas[self.stackedWidget.currentWidget().objectName()].botao_turma_lateral.setStyleSheet("""
                        QPushButton {
                            border-radius: 10px;
                            background-color: rgb(252, 88, 20);
                        }
                    """
                                                                                                                )
            self.stackedWidget.setCurrentWidget(self.paginas[nome_turma])
            self.paginas[nome_turma].botao_turma_lateral.setStyleSheet("""
                    QPushButton {
                        border-radius: 10px;
                        background-color: rgb(255, 229, 0);
                    }
                """
                                                                       )

        def fechar_pagina():
            self.stackedWidget.setCurrentWidget(self.page_recepcao)
            self.paginas[nome_turma].botao_turma_lateral.setStyleSheet("""
                    QPushButton {
                        border-radius: 10px;
                        background-color: rgb(252, 88, 20);
                    }
                """
                                                                       )
        self.paginas[nome_turma].botao_turma_lateral.clicked.connect(
            alterar_pagina)
        self.paginas[nome_turma].botao_fechar.clicked.connect(fechar_pagina)
        self.stackedWidget.addWidget(self.paginas[nome_turma])
        self.stackedWidget.setCurrentWidget(self.page_recepcao)

    def inserir_espacamento(self):
        self.verticalLayout.addItem(self.spacerItem)

    def limpar_paginas(self):
        for pagina in self.paginas:
            self.stackedWidget.removeWidget(self.paginas[pagina])
            self.paginas[pagina].botao_turma_lateral.deleteLater()
            self.paginas[pagina].deleteLater()
        self.paginas = {}
        self.verticalLayout.removeItem(self.spacerItem)

    def retranslateUi(self, TelaPrincipalProfessor):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalProfessor.setWindowTitle(
            _translate("TelaPrincipalProfessor", "Tela Principal"))
        self.botao_logoff.setText(_translate(
            "TelaPrincipalProfessor", "Logoff"))
        self.botao_sair.setText(_translate("TelaPrincipalProfessor", "Sair"))


class PaginaTurma(QtWidgets.QWidget):
    def __init__(self, nome_turma, turma_id, scrollAreaWidgetContents_lateral, verticalLayout_lateral, _translate, atividades_turma=None, funcao_criar_pagina_atividade=None):
        super().__init__()
        self.setObjectName(nome_turma)
        self.label_novas_atividades = QtWidgets.QLabel(self)
        self.label_novas_atividades.setGeometry(QtCore.QRect(10, 10, 511, 40))
        font_label_novas_atividades = QtGui.QFont()
        font_label_novas_atividades.setPointSize(24)
        self.label_novas_atividades.setFont(font_label_novas_atividades)
        self.label_novas_atividades.setStyleSheet("color: white;")
        self.label_novas_atividades.setObjectName(
            "pagina_label_novas_atividades")
        self.linha_horizontal = QtWidgets.QFrame(self)
        self.linha_horizontal.setGeometry(QtCore.QRect(10, 50, 560, 7))
        self.linha_horizontal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.linha_horizontal.setLineWidth(5)
        self.linha_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.linha_horizontal.setObjectName("pagina_linha_horizontal")
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 561, 501))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("pagina_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 221))
        self.scrollAreaWidgetContents.setObjectName(
            "pagina_scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("pagina_gridLayout")
        self.itens_atividade = {}
        self.ultimo_botao_atividade = [0, 0]
        for i, atividade in enumerate(atividades_turma) if atividades_turma else enumerate([]):
            self.itens_atividade.update(
                {atividade.titulo: ItemAtividade(self.scrollAreaWidgetContents)})
            self.gridLayout.addWidget(
                self.itens_atividade[atividade.titulo], i // 4, i % 4, 1, 1)
            if funcao_criar_pagina_atividade:
                self.itens_atividade[atividade.titulo].botao_atividade.clicked.connect(
                    funcao_criar_pagina_atividade(turma_id, atividade.materia_id, atividade=atividade))
            self.ultimo_botao_atividade[0] = i // 4
            self.ultimo_botao_atividade[1] = i % 4
            if self.ultimo_botao_atividade[1] == 3:
                self.ultimo_botao_atividade = [
                    self.ultimo_botao_atividade[0] + 1, 0]
            else:
                self.ultimo_botao_atividade = [
                    self.ultimo_botao_atividade[0], self.ultimo_botao_atividade[1] + 1]
            self.itens_atividade[atividade.titulo].label_titulo_atividade.setText(atividade.titulo)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.botao_add_atividade = QtWidgets.QPushButton(self)
        self.botao_add_atividade.setGeometry(QtCore.QRect(170, 10, 40, 40))
        self.botao_add_atividade.setMinimumSize(QtCore.QSize(40, 40))
        self.botao_add_atividade.setMaximumSize(QtCore.QSize(50, 50))
        font_botao_add_atividade = QtGui.QFont()
        font_botao_add_atividade.setPointSize(32)
        self.botao_add_atividade.setFont(font_botao_add_atividade)
        self.botao_add_atividade.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_add_atividade.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_add_atividade.setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
                                               "border-radius: 20px;\n"
                                               "background-color: rgb(255, 255, 255);")
        self.botao_add_atividade.setObjectName("pagina_botao_add_atividade")
        self.botao_fechar = QtWidgets.QPushButton(self)
        self.botao_fechar.setGeometry(QtCore.QRect(530, 10, 40, 40))
        font_botao_fechar = QtGui.QFont()
        font_botao_fechar.setPointSize(24)
        self.botao_fechar.setFont(font_botao_fechar)
        self.botao_fechar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_fechar.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.botao_fechar.setObjectName("pagina_botao_fechar")
        self.add_botao_turma_lateral(
            nome_turma, scrollAreaWidgetContents_lateral, verticalLayout_lateral, _translate)
        self.botao_add_atividade.clicked.connect(self.botao_add_nova_atividade_funcao(
            turma_id, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade))

        self.label_novas_atividades.setText(_translate(
            "TelaPrincipalProfessor", "Atividades"))
        self.botao_add_atividade.setText(
            _translate("TelaPrincipalProfessor", "+"))
        self.botao_fechar.setText(
            _translate("TelaPrincipalProfessor", "X"))

    def botao_add_nova_atividade_funcao(self, turma_id, funcao_criar_pagina_atividade=None):
        def botao_add_nova_atividade_funcao():
            num = len(self.itens_atividade)
            self.itens_atividade.update(
                {num: ItemAtividade(self.scrollAreaWidgetContents)})
            self.gridLayout.addWidget(
                self.itens_atividade[num], self.ultimo_botao_atividade[0], self.ultimo_botao_atividade[1], 1, 1)
            self.itens_atividade[num].setObjectName(f'botao_atividade{num}')
            if self.ultimo_botao_atividade[1] == 3:
                self.ultimo_botao_atividade = [
                    self.ultimo_botao_atividade[0] + 1, 0]
            else:
                self.ultimo_botao_atividade = [
                    self.ultimo_botao_atividade[0], self.ultimo_botao_atividade[1] + 1]
            if funcao_criar_pagina_atividade:
                self.itens_atividade[num].botao_atividade.clicked.connect(
                    funcao_criar_pagina_atividade(turma_id))
            self.itens_atividade[num].label_titulo_atividade.setText(
                f'Nova Atividade {num}')
        return botao_add_nova_atividade_funcao

    def add_botao_turma_lateral(self, nome_turma, scrollAreaWidgetContents_lateral, verticalLayout_lateral, _translate):
        self.botao_turma_lateral = QtWidgets.QPushButton(
            scrollAreaWidgetContents_lateral)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_turma_lateral.setFont(font)
        self.botao_turma_lateral.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_turma_lateral.setStyleSheet("border-radius: 10px;\n"
                                               "background-color: rgb(252, 88, 20);")
        self.botao_turma_lateral.setObjectName(nome_turma)
        verticalLayout_lateral.addWidget(self.botao_turma_lateral)
        self.botao_turma_lateral.setText(
            _translate("TelaPrincipalProfessor", nome_turma))


class ItemAtividade(QtWidgets.QGroupBox):
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
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalProfessor = QtWidgets.QWidget()
    ui = Ui_TelaPrincipalProfessor()
    ui.setupUi(TelaPrincipalProfessor)
    ui.add_pagina("Turma 1", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
        Atividade(2, "Atividade 2", "Atividade 2", 1, 1, 1),
        Atividade(3, "Atividade 3", "Atividade 3", 1, 1, 1),
    ])
    ui.add_pagina("Turma 2", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
        Atividade(2, "Atividade 2", "Atividade 2", 1, 1, 1),
    ])
    ui.add_pagina("Turma 3", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
        Atividade(2, "Atividade 2", "Atividade 2", 1, 1, 1),
        Atividade(3, "Atividade 3", "Atividade 3", 1, 1, 1),
        Atividade(4, "Atividade 4", "Atividade 4", 1, 1, 1),
        Atividade(5, "Atividade 5", "Atividade 5", 1, 1, 1),
    ])
    ui.add_pagina("Turma 4", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
    ])
    ui.inserir_espacamento()
    ui.limpar_paginas()
    ui.add_pagina("Turma 4", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
    ])
    ui.add_pagina("Turma 3", 1, [
        Atividade(1, "Atividade 1", "Atividade 1", 1, 1, 1),
        Atividade(2, "Atividade 2", "Atividade 2", 1, 1, 1),
        Atividade(3, "Atividade 3", "Atividade 3", 1, 1, 1),
        Atividade(4, "Atividade 4", "Atividade 4", 1, 1, 1),
        Atividade(5, "Atividade 5", "Atividade 5", 1, 1, 1),
    ])
    ui.inserir_espacamento()
    TelaPrincipalProfessor.show()
    sys.exit(app.exec_())
