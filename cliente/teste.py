from PyQt5 import QtCore, QtGui, QtWidgets


class PaginaTurma(QtWidgets.QWidget):
    def __init__(self, nome_turma, materia_id, turma_id, scrollAreaWidgetContents_lateral, verticalLayout_lateral, _translate, atividades_turma=None, funcao_criar_pagina_atividade=None):
        super().__init__()
        self.label_novas_atividades = QtWidgets.QLabel(self)
        self.linha_horizontal = QtWidgets.QFrame(self)
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.botao_atividade = {}
        self.ultimo_botao_atividade = [0, 0]
        self.botao_add_atividade = QtWidgets.QPushButton(self)
        self.botao_fechar = QtWidgets.QPushButton(self)
        self.add_botao_turma_lateral(nome_turma, scrollAreaWidgetContents_lateral, verticalLayout_lateral, _translate)
        self.add_modificacoes(nome_turma, materia_id, turma_id, _translate, atividades_turma, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade)
        self.botao_add_atividade.clicked.connect(self.funcao_botao_add_atividade(nome_turma, materia_id, turma_id, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade))
    
    def add_modificacoes(self, nome_turma, materia_id, turma_id, _translate, atividades_turma=None, funcao_criar_pagina_atividade=None):
        self.setObjectName(nome_turma)
        self.label_novas_atividades.setGeometry(QtCore.QRect(10, 10, 511, 40))
        font_label_novas_atividades = QtGui.QFont()
        font_label_novas_atividades.setPointSize(24)
        self.label_novas_atividades.setFont(font_label_novas_atividades)
        self.label_novas_atividades.setStyleSheet("color: white;")
        self.label_novas_atividades.setObjectName("pagina_label_novas_atividades")
        self.linha_horizontal.setGeometry(QtCore.QRect(10, 50, 560, 7))
        self.linha_horizontal.setFrameShadow(QtWidgets.QFrame.Plain)
        self.linha_horizontal.setLineWidth(5)
        self.linha_horizontal.setFrameShape(QtWidgets.QFrame.HLine)
        self.linha_horizontal.setObjectName("pagina_linha_horizontal")
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 561, 501))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("pagina_scrollArea")
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 544, 221))
        self.scrollAreaWidgetContents.setObjectName("pagina_scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("pagina_gridLayout")
        if atividades_turma:
            self.add_botoes_atividade(atividades_turma, materia_id, turma_id, funcao_criar_pagina_atividade=funcao_criar_pagina_atividade)
        self.botao_add_atividade.setGeometry(QtCore.QRect(170, 10, 40, 40))
        self.botao_add_atividade.setMinimumSize(QtCore.QSize(40, 40))
        self.botao_add_atividade.setMaximumSize(QtCore.QSize(50, 50))
        font_botao_add_atividade = QtGui.QFont()
        font_botao_add_atividade.setPointSize(32)
        self.botao_add_atividade.setFont(font_botao_add_atividade)
        self.botao_add_atividade.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_add_atividade.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_add_atividade.setStyleSheet("border: 3px solid rgb(7, 66, 22);\n"
                                                     "border-radius: 20px;\n"
                                                     "background-color: rgb(255, 255, 255);")
        self.botao_add_atividade.setObjectName("pagina_botao_add_atividade")
        self.botao_fechar.setGeometry(QtCore.QRect(530, 10, 40, 40))
        font_botao_fechar = QtGui.QFont()
        font_botao_fechar.setPointSize(24)
        self.botao_fechar.setFont(font_botao_fechar)
        self.botao_fechar.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_fechar.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.botao_fechar.setObjectName("pagina_botao_fechar")
        self.label_novas_atividades.setText(_translate(
            "TelaPrincipalProfessor", "Atividades"))
        self.botao_add_atividade.setText(
            _translate("TelaPrincipalProfessor", "+"))
        self.botao_fechar.setText(
            _translate("TelaPrincipalProfessor", "X"))

    def funcao_botao_add_atividade(self, atividade, materia_id, turma_id, funcao_criar_pagina_atividade=None):
        def funcao_botao_add_atividade():
            self.botao_atividade[atividade] = QtWidgets.QPushButton(
                self.scrollArea)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.botao_atividade[atividade].sizePolicy().hasHeightForWidth())
            self.botao_atividade[atividade].setSizePolicy(
                sizePolicy)
            self.botao_atividade[atividade].setMinimumSize(
                QtCore.QSize(120, 150))
            self.botao_atividade[atividade].setMaximumSize(
                QtCore.QSize(120, 150))
            self.botao_atividade[atividade].setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_atividade[atividade].setLayoutDirection(
                QtCore.Qt.LeftToRight)
            self.botao_atividade[atividade].setAutoFillBackground(
                False)
            self.botao_atividade[atividade].setStyleSheet("border-radius: 10px;\n"
                                                                                     "background-color: rgb(217, 217, 217);\n"
                                                                                     "background-image: url(img/lista.png);\n"
                                                                                     "background-repeat: no-repeat;\n"
                                                                                     "background-position: center center;")
            self.botao_atividade[atividade].setObjectName(atividade)
            if self.ultimo_botao_atividade[1] == 3:
                self.ultimo_botao_atividade = (self.ultimo_botao_atividade[0] + 1, 0)
            else:
                self.ultimo_botao_atividade = (self.ultimo_botao_atividade[0], self.ultimo_botao_atividade[1] + 1)
            self.gridLayout.addWidget(
                self.botao_atividade[atividade], self.ultimo_botao_atividade[0], self.ultimo_botao_atividade[1], 1, 1)
            if funcao_criar_pagina_atividade:
                self.botao_atividade[atividade].clicked.connect(
                    funcao_criar_pagina_atividade(materia_id, turma_id))
        return funcao_botao_add_atividade

    def add_botoes_atividade(self, atividades_turma, materia_id, turma_id, funcao_criar_pagina_atividade=None):
        for i, atividade in enumerate(atividades_turma):
            self.botao_atividade[atividade.nome] = QtWidgets.QPushButton(
                self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(
                QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(
                self.botao_atividade[atividade.nome].sizePolicy().hasHeightForWidth())
            self.botao_atividade[atividade.nome].setSizePolicy(sizePolicy)
            self.botao_atividade[atividade.nome].setMinimumSize(
                QtCore.QSize(120, 150))
            self.botao_atividade[atividade.nome].setMaximumSize(
                QtCore.QSize(120, 150))
            self.botao_atividade[atividade.nome].setCursor(
                QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.botao_atividade[atividade.nome].setLayoutDirection(
                QtCore.Qt.LeftToRight)
            self.botao_atividade[atividade.nome].setAutoFillBackground(False)
            self.botao_atividade[atividade.nome].setStyleSheet("border-radius: 10px;\n"
                                                         "background-color: rgb(217, 217, 217);\n"
                                                         "background-image: url(img/lista.png);\n"
                                                         "background-repeat: no-repeat;\n"
                                                         "background-position: center center;")
            self.botao_atividade[atividade.nome].setObjectName(
                f"botao_atividade{i}")
            self.gridLayout.addWidget(
                self.botao_atividade[atividade.nome], i // 4, i % 4, 1, 1)
            if funcao_criar_pagina_atividade:
                self.botao_atividade[atividade.nome].clicked.connect(funcao_criar_pagina_atividade(materia_id, turma_id, id_atividade=atividade.id))
            self.ultimo_botao_atividade[0] = i // 4
            self.ultimo_botao_atividade[1] = i % 4
    
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
    
    def rem_botao_turma_lateral(self):
        self.botao_turma_lateral.deleteLater()
        self.botao_turma_lateral = None