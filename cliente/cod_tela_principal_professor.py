from PyQt5 import QtCore, QtGui, QtWidgets
from teste import PaginaTurma
import time


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

    def add_pagina(self, nome_turma, materia_id, turma_id, atividades=None, funcao_criar_pagina_atividade=None):
        self.paginas[nome_turma] = PaginaTurma(nome_turma, materia_id, turma_id, self.scrollAreaWidgetContents, self.verticalLayout, self._translate, atividades, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade)

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

    # def add_pagina(self, nome, atividades, pilha_paginas=None, funcao_criar_pagina_atividade=None):
    #     self.pages[nome] = QtWidgets.QWidget()
    #     self.pages[nome].setObjectName(nome)
    #     self.novas_atividades = QtWidgets.QLabel(self.pages[nome])
    #     self.novas_atividades.setGeometry(QtCore.QRect(10, 10, 511, 40))
    #     font = QtGui.QFont()
    #     font.setPointSize(24)
    #     self.novas_atividades.setFont(font)
    #     self.novas_atividades.setStyleSheet("color: white;")
    #     self.novas_atividades.setObjectName("novas_atividades")
        # self.line = QtWidgets.QFrame(self.pages[nome])
    #     self.line.setGeometry(QtCore.QRect(10, 50, 560, 7))
    #     self.line.setFrameShadow(QtWidgets.QFrame.Plain)
    #     self.line.setLineWidth(5)
    #     self.line.setFrameShape(QtWidgets.QFrame.HLine)
    #     self.line.setObjectName("line")
    #     self.scrollArea_pages[nome] = QtWidgets.QScrollArea(
    #         self.pages[nome])
    #     self.scrollArea_pages[nome].setGeometry(
    #         QtCore.QRect(10, 60, 561, 501))
    #     self.scrollArea_pages[nome].setStyleSheet(
    #         "border: none;")
    #     self.scrollArea_pages[nome].setVerticalScrollBarPolicy(
    #         QtCore.Qt.ScrollBarAlwaysOn)
    #     self.scrollArea_pages[nome].setHorizontalScrollBarPolicy(
    #         QtCore.Qt.ScrollBarAlwaysOff)
    #     self.scrollArea_pages[nome].setWidgetResizable(
    #         True)
    #     self.scrollArea_pages[nome].setObjectName(
    #         f"scrollArea_{nome}")
    #     self.scrollAreaWidgetContents_pages[nome] = QtWidgets.QWidget(
    #     )
    #     self.scrollAreaWidgetContents_pages[nome].setGeometry(
    #         QtCore.QRect(0, 0, 544, 221))
    #     self.scrollAreaWidgetContents_pages[nome].setObjectName(
    #         f"scrollAreaWidgetContents{nome}")
    #     self.scrollArea_pages[nome].setWidget(
    #         self.scrollAreaWidgetContents_pages[nome])
    #     self.gridLayout[nome] = QtWidgets.QGridLayout(
    #         self.scrollAreaWidgetContents_pages[nome])
    #     self.gridLayout[nome].setObjectName("gridLayout")
    #     self.botoes_atividades = {}
    #     self.add_botoes(nome,
    #                     atividades, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade, pilha_paginas=pilha_paginas)
    #     self.botao_add_atividade = {}
    #     self.botao_add_atividade[nome] = QtWidgets.QPushButton(
    #         self.pages[nome])
    #     self.botao_add_atividade[nome].setGeometry(
    #         QtCore.QRect(170, 10, 40, 40))
    #     self.botao_add_atividade[nome].setMinimumSize(QtCore.QSize(40, 40))
    #     self.botao_add_atividade[nome].setMaximumSize(QtCore.QSize(50, 50))
    #     font = QtGui.QFont()
    #     font.setPointSize(32)
    #     self.botao_add_atividade[nome].setFont(font)
    #     self.botao_add_atividade[nome].setCursor(
    #         QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    #     self.botao_add_atividade[nome].setLayoutDirection(
    #         QtCore.Qt.LeftToRight)
    #     self.botao_add_atividade[nome].setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
    #                                                  "border-radius: 20px;\n"
    #                                                  "background-color: rgb(255, 255, 255);")
    #     self.botao_add_atividade[nome].setObjectName(
    #         f"botao_add_atividade{nome}")
    #     self.botao_add_atividade[nome].clicked.connect(self.add_botao(nome, atividades,
    #                                                                   funcao_criar_pagina_atividade=funcao_criar_pagina_atividade, pilha_paginas=pilha_paginas))
    #     self.botao_fechar = QtWidgets.QPushButton(self.pages[nome])
    #     self.botao_fechar.setGeometry(QtCore.QRect(530, 10, 40, 40))
    #     font = QtGui.QFont()
    #     font.setPointSize(24)
    #     self.botao_fechar.setFont(font)
    #     self.botao_fechar.setCursor(
    #         QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    #     self.botao_fechar.setStyleSheet("background-color: rgb(255, 0, 0);")
    #     self.botao_fechar.setObjectName("botao_fechar")
    #     self.stackedWidget.addWidget(self.pages[nome])
    #     self.verticalLayout.setSpacing(6)
    #     self.verticalLayout.setObjectName("verticalLayout")
    #     self.stackedWidget.addWidget(self.pages[nome])

    #     def alterar_pagina():
    #         if self.stackedWidget.currentWidget().objectName() == nome:
    #             return
    #         elif self.stackedWidget.currentWidget().objectName() != "page_recepcao":
    #             self.turmas[self.stackedWidget.currentWidget().objectName()].setStyleSheet("""
    #                     QPushButton {
    #                         border-radius: 10px;
    #                         background-color: rgb(252, 88, 20);
    #                     }
    #                 """
    #                                                                                        )
    #         self.stackedWidget.setCurrentWidget(self.pages[nome])
    #         self.turmas[nome].setStyleSheet("""
    #                 QPushButton {
    #                     border-radius: 10px;
    #                     background-color: rgb(255, 229, 0);
    #                 }
    #             """
    #                                         )

    #     def fechar_pagina():
    #         self.stackedWidget.setCurrentWidget(self.page_recepcao)
    #         self.turmas[nome].setStyleSheet("""
    #                 QPushButton {
    #                     border-radius: 10px;
    #                     background-color: rgb(252, 88, 20);
    #                 }
    #             """
    #                                         )
    #     self.turmas[nome].clicked.connect(alterar_pagina)
    #     self.botao_fechar.clicked.connect(fechar_pagina)
    #     self.stackedWidget.setCurrentWidget(self.page_recepcao)
    #     self.novas_atividades.setText(self._translate(
    #         "TelaPrincipalProfessor", "Atividades"))
    #     self.botao_add_atividade[nome].setText(
    #         self._translate("TelaPrincipalProfessor", "+"))
    #     self.botao_fechar.setText(
    #         self._translate("TelaPrincipalProfessor", "X"))

    # def add_botao(self, nome, atividades, funcao_criar_pagina_atividade=None, pilha_paginas=None):
    #     def add_botao_funcao():
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'] = QtWidgets.QPushButton(
    #             self.scrollArea_pages[nome])
    #         sizePolicy = QtWidgets.QSizePolicy(
    #             QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    #         sizePolicy.setHorizontalStretch(0)
    #         sizePolicy.setVerticalStretch(0)
    #         sizePolicy.setHeightForWidth(
    #             self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].sizePolicy().hasHeightForWidth())
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setSizePolicy(
    #             sizePolicy)
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setMinimumSize(
    #             QtCore.QSize(120, 150))
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setMaximumSize(
    #             QtCore.QSize(120, 150))
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setCursor(
    #             QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setLayoutDirection(
    #             QtCore.Qt.LeftToRight)
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setAutoFillBackground(
    #             False)
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setStyleSheet("border-radius: 10px;\n"
    #                                                                                  "background-color: rgb(217, 217, 217);\n"
    #                                                                                  "background-image: url(img/lista.png);\n"
    #                                                                                  "background-repeat: no-repeat;\n"
    #                                                                                  "background-position: center center;")
    #         self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].setObjectName(
    #             f"botao_atividade{self.indice_scroll[nome]}")
    #         self.gridLayout[nome].addWidget(
    #             self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'], self.indice_scroll[nome] // 4, self.indice_scroll[nome] % 4, 1, 1)
    #         if funcao_criar_pagina_atividade and pilha_paginas:
    #             self.botoes_atividades[f'novo_{self.indice_scroll[nome]}'].clicked.connect(
    #                 funcao_criar_pagina_atividade(atividades[2].split('-')[3], atividades[3].split('-')[2]))
    #         self.indice_scroll[nome] += 1
    #     return add_botao_funcao

    # def add_botoes(self, nome, atividades, funcao_criar_pagina_atividade=None, pilha_paginas=None):
    #     for i, titulo in enumerate(atividades):
    #         self.botoes_atividades[titulo] = QtWidgets.QPushButton(
    #             self.scrollAreaWidgetContents_pages[nome])
    #         sizePolicy = QtWidgets.QSizePolicy(
    #             QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    #         sizePolicy.setHorizontalStretch(0)
    #         sizePolicy.setVerticalStretch(0)
    #         sizePolicy.setHeightForWidth(
    #             self.botoes_atividades[titulo].sizePolicy().hasHeightForWidth())
    #         self.botoes_atividades[titulo].setSizePolicy(sizePolicy)
    #         self.botoes_atividades[titulo].setMinimumSize(
    #             QtCore.QSize(120, 150))
    #         self.botoes_atividades[titulo].setMaximumSize(
    #             QtCore.QSize(120, 150))
    #         self.botoes_atividades[titulo].setCursor(
    #             QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    #         self.botoes_atividades[titulo].setLayoutDirection(
    #             QtCore.Qt.LeftToRight)
    #         self.botoes_atividades[titulo].setAutoFillBackground(False)
    #         self.botoes_atividades[titulo].setStyleSheet("border-radius: 10px;\n"
    #                                                      "background-color: rgb(217, 217, 217);\n"
    #                                                      "background-image: url(img/lista.png);\n"
    #                                                      "background-repeat: no-repeat;\n"
    #                                                      "background-position: center center;")
    #         self.botoes_atividades[titulo].setObjectName(
    #             f"botao_atividade{i}")
    #         self.gridLayout[nome].addWidget(
    #             self.botoes_atividades[titulo], i // 4, i % 4, 1, 1)
    #         if funcao_criar_pagina_atividade and pilha_paginas:
    #             self.botoes_atividades[titulo].clicked.connect(funcao_criar_pagina_atividade(atividades[i].split(
    #                 '-')[2], atividades[i].split('-')[3], id_atividade=atividades[i].split('-')[0]))
    #         self.indice_scroll[nome] = i + 1

    # def add_turma(self, nome_turma, atividades, pilha_paginas=None, funcao_criar_pagina_atividade=None):
    #     self.turmas[nome_turma] = QtWidgets.QPushButton(
    #         self.scrollAreaWidgetContents)
    #     font = QtGui.QFont()
    #     font.setPointSize(24)
    #     self.turmas[nome_turma].setFont(font)
    #     self.turmas[nome_turma].setCursor(
    #         QtGui.QCursor(QtCore.Qt.PointingHandCursor))
    #     self.turmas[nome_turma].setStyleSheet("border-radius: 10px;\n"
    #                                           "background-color: rgb(252, 88, 20);")
    #     self.turmas[nome_turma].setObjectName(nome_turma)
    #     self.verticalLayout.addWidget(self.turmas[nome_turma])
    #     self.turmas[nome_turma].setText(
    #         self._translate("TelaPrincipalProfessor", nome_turma))
    #     self.add_pagina(nome_turma, atividades, pilha_paginas=pilha_paginas,
    #                     funcao_criar_pagina_atividade=funcao_criar_pagina_atividade)

    def inserir_espacamento(self):
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

    def limpar_paginas(self):
        for pagina in self.paginas:
            self.paginas[pagina].rem_botao_turma_lateral()
            self.stackedWidget.removeWidget(self.paginas[pagina])
            self.paginas[pagina].deleteLater()
        self.paginas = {}

    def retranslateUi(self, TelaPrincipalProfessor):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalProfessor.setWindowTitle(
            _translate("TelaPrincipalProfessor", "Tela Principal"))
        self.botao_logoff.setText(_translate(
            "TelaPrincipalProfessor", "Logoff"))
        self.botao_sair.setText(_translate("TelaPrincipalProfessor", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalProfessor = QtWidgets.QWidget()
    ui = Ui_TelaPrincipalProfessor()
    ui.setupUi(TelaPrincipalProfessor)
    ui.add_pagina("Turma 1", ["Atividade 1", "Atividade 2"])
    ui.add_pagina("Turma 2", ["Atividade 1", "Atividade 2", "Atividade 3"])
    ui.add_pagina("Turma 3", ["Atividade 1"])
    ui.add_pagina("Turma 4", ["Atividade 1",
                  "Atividade 2", "Atividade 3", "Atividade 4"])
    ui.add_pagina("Turma 5", ["Atividade 1", "Atividade 2",
                  "Atividade 3", "Atividade 4", "Atividade 5"])
    ui.add_pagina("Turma 6", ["Atividade 1", "Atividade 2",
                  "Atividade 3", "Atividade 4", "Atividade 5", "Atividade 6"])
    ui.inserir_espacamento()
    TelaPrincipalProfessor.show()
    sys.exit(app.exec_())
