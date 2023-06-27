# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipalAluno(object):
    def setupUi(self, TelaPrincipalAluno):
        TelaPrincipalAluno.setObjectName("TelaPrincipalAluno")
        TelaPrincipalAluno.resize(900, 580)
        TelaPrincipalAluno.setMinimumSize(QtCore.QSize(900, 580))
        TelaPrincipalAluno.setMaximumSize(QtCore.QSize(900, 580))
        TelaPrincipalAluno.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.conteudo = QtWidgets.QFrame(TelaPrincipalAluno)
        self.conteudo.setGeometry(QtCore.QRect(290, -10, 600, 581))
        self.conteudo.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.conteudo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.conteudo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.conteudo.setObjectName("conteudo")
        self.stackedWidget = QtWidgets.QStackedWidget(self.conteudo)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 580, 580))
        self.stackedWidget.setMinimumSize(QtCore.QSize(580, 580))
        self.stackedWidget.setMaximumSize(QtCore.QSize(580, 580))
        self.stackedWidget.setStyleSheet("background-color: rgb(33, 33, 33);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.rotulo_novas_atividades = QtWidgets.QLabel(self.page)
        self.rotulo_novas_atividades.setGeometry(QtCore.QRect(10, 10, 511, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.rotulo_novas_atividades.setFont(font)
        self.rotulo_novas_atividades.setStyleSheet("color: white;")
        self.rotulo_novas_atividades.setObjectName("rotulo_novas_atividades")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(10, 50, 560, 7))
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.rotulo_respondidas = QtWidgets.QLabel(self.page)
        self.rotulo_respondidas.setGeometry(QtCore.QRect(10, 289, 560, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.rotulo_respondidas.setFont(font)
        self.rotulo_respondidas.setStyleSheet("color: white;")
        self.rotulo_respondidas.setObjectName("rotulo_respondidas")
        self.line_2 = QtWidgets.QFrame(self.page)
        self.line_2.setGeometry(QtCore.QRect(10, 320, 560, 7))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.conteudo_scrollArea = QtWidgets.QScrollArea(self.page)
        self.conteudo_scrollArea.setGeometry(QtCore.QRect(10, 60, 561, 221))
        self.conteudo_scrollArea.setStyleSheet("border: none;")
        self.conteudo_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.conteudo_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conteudo_scrollArea.setWidgetResizable(True)
        self.conteudo_scrollArea.setObjectName("conteudo_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -265, 544, 486))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setObjectName("gridLayout")
        self.botao_atividade1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade1.sizePolicy().hasHeightForWidth())
        self.botao_atividade1.setSizePolicy(sizePolicy)
        self.botao_atividade1.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade1.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade1.setAutoFillBackground(False)
        self.botao_atividade1.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade1.setText("")
        self.botao_atividade1.setObjectName("botao_atividade1")
        self.gridLayout.addWidget(self.botao_atividade1, 0, 0, 1, 1)
        self.botao_atividade2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade2.sizePolicy().hasHeightForWidth())
        self.botao_atividade2.setSizePolicy(sizePolicy)
        self.botao_atividade2.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade2.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade2.setAutoFillBackground(False)
        self.botao_atividade2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade2.setText("")
        self.botao_atividade2.setObjectName("botao_atividade2")
        self.gridLayout.addWidget(self.botao_atividade2, 0, 1, 1, 1)
        self.botao_atividade5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade5.sizePolicy().hasHeightForWidth())
        self.botao_atividade5.setSizePolicy(sizePolicy)
        self.botao_atividade5.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade5.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade5.setAutoFillBackground(False)
        self.botao_atividade5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade5.setText("")
        self.botao_atividade5.setObjectName("botao_atividade5")
        self.gridLayout.addWidget(self.botao_atividade5, 1, 0, 1, 1)
        self.botao_atividade6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade6.sizePolicy().hasHeightForWidth())
        self.botao_atividade6.setSizePolicy(sizePolicy)
        self.botao_atividade6.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade6.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade6.setAutoFillBackground(False)
        self.botao_atividade6.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade6.setText("")
        self.botao_atividade6.setObjectName("botao_atividade6")
        self.gridLayout.addWidget(self.botao_atividade6, 1, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.botao_atividade7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade7.sizePolicy().hasHeightForWidth())
        self.botao_atividade7.setSizePolicy(sizePolicy)
        self.botao_atividade7.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade7.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade7.setAutoFillBackground(False)
        self.botao_atividade7.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade7.setText("")
        self.botao_atividade7.setObjectName("botao_atividade7")
        self.gridLayout.addWidget(self.botao_atividade7, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 4, 1, 1)
        self.botao_atividade4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade4.sizePolicy().hasHeightForWidth())
        self.botao_atividade4.setSizePolicy(sizePolicy)
        self.botao_atividade4.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade4.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade4.setAutoFillBackground(False)
        self.botao_atividade4.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade4.setText("")
        self.botao_atividade4.setObjectName("botao_atividade4")
        self.gridLayout.addWidget(self.botao_atividade4, 0, 3, 1, 1)
        self.botao_atividade3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade3.sizePolicy().hasHeightForWidth())
        self.botao_atividade3.setSizePolicy(sizePolicy)
        self.botao_atividade3.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade3.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade3.setAutoFillBackground(False)
        self.botao_atividade3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade3.setText("")
        self.botao_atividade3.setObjectName("botao_atividade3")
        self.gridLayout.addWidget(self.botao_atividade3, 0, 2, 1, 1)
        self.botao_atividade8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade8.sizePolicy().hasHeightForWidth())
        self.botao_atividade8.setSizePolicy(sizePolicy)
        self.botao_atividade8.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade8.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade8.setAutoFillBackground(False)
        self.botao_atividade8.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade8.setText("")
        self.botao_atividade8.setObjectName("botao_atividade8")
        self.gridLayout.addWidget(self.botao_atividade8, 1, 3, 1, 1)
        self.botao_atividade9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade9.sizePolicy().hasHeightForWidth())
        self.botao_atividade9.setSizePolicy(sizePolicy)
        self.botao_atividade9.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade9.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade9.setAutoFillBackground(False)
        self.botao_atividade9.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade9.setText("")
        self.botao_atividade9.setObjectName("botao_atividade9")
        self.gridLayout.addWidget(self.botao_atividade9, 2, 0, 1, 1)
        self.botao_atividade10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade10.sizePolicy().hasHeightForWidth())
        self.botao_atividade10.setSizePolicy(sizePolicy)
        self.botao_atividade10.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade10.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade10.setAutoFillBackground(False)
        self.botao_atividade10.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade10.setText("")
        self.botao_atividade10.setObjectName("botao_atividade10")
        self.gridLayout.addWidget(self.botao_atividade10, 2, 1, 1, 1)
        self.botao_atividade11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade11.sizePolicy().hasHeightForWidth())
        self.botao_atividade11.setSizePolicy(sizePolicy)
        self.botao_atividade11.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade11.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade11.setAutoFillBackground(False)
        self.botao_atividade11.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade11.setText("")
        self.botao_atividade11.setObjectName("botao_atividade11")
        self.gridLayout.addWidget(self.botao_atividade11, 2, 2, 1, 1)
        self.conteudo_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.conteudo_scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.conteudo_scrollArea_2.setGeometry(QtCore.QRect(10, 330, 561, 221))
        self.conteudo_scrollArea_2.setStyleSheet("border: none;")
        self.conteudo_scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.conteudo_scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.conteudo_scrollArea_2.setWidgetResizable(True)
        self.conteudo_scrollArea_2.setObjectName("conteudo_scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 544, 221))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 0, 1, 1)
        self.botao_atividade_respondida1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade_respondida1.sizePolicy().hasHeightForWidth())
        self.botao_atividade_respondida1.setSizePolicy(sizePolicy)
        self.botao_atividade_respondida1.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida1.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade_respondida1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade_respondida1.setAutoFillBackground(False)
        self.botao_atividade_respondida1.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade_respondida1.setText("")
        self.botao_atividade_respondida1.setObjectName("botao_atividade_respondida1")
        self.gridLayout_2.addWidget(self.botao_atividade_respondida1, 0, 0, 1, 1)
        self.botao_atividade_respondida2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade_respondida2.sizePolicy().hasHeightForWidth())
        self.botao_atividade_respondida2.setSizePolicy(sizePolicy)
        self.botao_atividade_respondida2.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida2.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade_respondida2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade_respondida2.setAutoFillBackground(False)
        self.botao_atividade_respondida2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade_respondida2.setText("")
        self.botao_atividade_respondida2.setObjectName("botao_atividade_respondida2")
        self.gridLayout_2.addWidget(self.botao_atividade_respondida2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 0, 3, 1, 1)
        self.botao_atividade_respondida3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.botao_atividade_respondida3.sizePolicy().hasHeightForWidth())
        self.botao_atividade_respondida3.setSizePolicy(sizePolicy)
        self.botao_atividade_respondida3.setMinimumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida3.setMaximumSize(QtCore.QSize(120, 150))
        self.botao_atividade_respondida3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_atividade_respondida3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.botao_atividade_respondida3.setAutoFillBackground(False)
        self.botao_atividade_respondida3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(217, 217, 217);\n"
"background-image: url(:/img/lista.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center center;")
        self.botao_atividade_respondida3.setText("")
        self.botao_atividade_respondida3.setObjectName("botao_atividade_respondida3")
        self.gridLayout_2.addWidget(self.botao_atividade_respondida3, 0, 2, 1, 1)
        self.conteudo_scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.botao_fechar = QtWidgets.QPushButton(self.page)
        self.botao_fechar.setGeometry(QtCore.QRect(530, 10, 40, 40))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.botao_fechar.setFont(font)
        self.botao_fechar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_fechar.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.botao_fechar.setObjectName("botao_fechar")
        self.rotulo_novas_atividades.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.rotulo_respondidas.raise_()
        self.conteudo_scrollArea.raise_()
        self.conteudo_scrollArea_2.raise_()
        self.botao_fechar.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_recepcao = QtWidgets.QWidget()
        self.page_recepcao.setObjectName("page_recepcao")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_recepcao)
        self.verticalLayout_2.setContentsMargins(190, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget.addWidget(self.page_recepcao)
        self.botao_logoff = QtWidgets.QPushButton(TelaPrincipalAluno)
        self.botao_logoff.setGeometry(QtCore.QRect(10, 10, 40, 20))
        self.botao_logoff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_logoff.setStyleSheet("border-radius: 10px;\n"
"background-color: blue;")
        self.botao_logoff.setObjectName("botao_logoff")
        self.lateral_scrollArea = QtWidgets.QScrollArea(TelaPrincipalAluno)
        self.lateral_scrollArea.setGeometry(QtCore.QRect(0, 210, 300, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lateral_scrollArea.sizePolicy().hasHeightForWidth())
        self.lateral_scrollArea.setSizePolicy(sizePolicy)
        self.lateral_scrollArea.setMinimumSize(QtCore.QSize(300, 330))
        self.lateral_scrollArea.setStyleSheet("border: none;\n"
"background-color: rgb(30, 30, 30);")
        self.lateral_scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lateral_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.lateral_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lateral_scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.lateral_scrollArea.setWidgetResizable(True)
        self.lateral_scrollArea.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lateral_scrollArea.setObjectName("lateral_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 283, 378))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.matematica = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.matematica.setFont(font)
        self.matematica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.matematica.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.matematica.setCheckable(True)
        self.matematica.setChecked(False)
        self.matematica.setObjectName("matematica")
        self.verticalLayout.addWidget(self.matematica)
        self.quimica = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.quimica.setFont(font)
        self.quimica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.quimica.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.quimica.setObjectName("quimica")
        self.verticalLayout.addWidget(self.quimica)
        self.historia = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.historia.setFont(font)
        self.historia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.historia.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.historia.setObjectName("historia")
        self.verticalLayout.addWidget(self.historia)
        self.ingles = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ingles.setFont(font)
        self.ingles.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ingles.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.ingles.setObjectName("ingles")
        self.verticalLayout.addWidget(self.ingles)
        self.fisica = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.fisica.setFont(font)
        self.fisica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fisica.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.fisica.setObjectName("fisica")
        self.verticalLayout.addWidget(self.fisica)
        self.geografia = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.geografia.setFont(font)
        self.geografia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.geografia.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.geografia.setObjectName("geografia")
        self.verticalLayout.addWidget(self.geografia)
        self.filosofia = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.filosofia.setFont(font)
        self.filosofia.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filosofia.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.filosofia.setObjectName("filosofia")
        self.verticalLayout.addWidget(self.filosofia)
        self.portugues = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.portugues.setFont(font)
        self.portugues.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.portugues.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.portugues.setObjectName("portugues")
        self.verticalLayout.addWidget(self.portugues)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lateral_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.botao_sair = QtWidgets.QPushButton(TelaPrincipalAluno)
        self.botao_sair.setGeometry(QtCore.QRect(240, 10, 40, 20))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("border-radius: 10px;\n"
"background-color: red;")
        self.botao_sair.setObjectName("botao_sair")
        self.logo_escola = QtWidgets.QLabel(TelaPrincipalAluno)
        self.logo_escola.setGeometry(QtCore.QRect(60, 30, 180, 180))
        self.logo_escola.setStyleSheet("background-size: contain;")
        self.logo_escola.setText("")
        self.logo_escola.setPixmap(QtGui.QPixmap(":/img/logo-escola.png"))
        self.logo_escola.setScaledContents(True)
        self.logo_escola.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_escola.setObjectName("logo_escola")

        self.retranslateUi(TelaPrincipalAluno)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipalAluno)

    def retranslateUi(self, TelaPrincipalAluno):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipalAluno.setWindowTitle(_translate("TelaPrincipalAluno", "Tela Principal"))
        self.rotulo_novas_atividades.setText(_translate("TelaPrincipalAluno", "Novas Atividades"))
        self.rotulo_respondidas.setText(_translate("TelaPrincipalAluno", "Respondidas"))
        self.botao_fechar.setText(_translate("TelaPrincipalAluno", "X"))
        self.botao_logoff.setText(_translate("TelaPrincipalAluno", "Logoff"))
        self.matematica.setText(_translate("TelaPrincipalAluno", "Matemática"))
        self.quimica.setText(_translate("TelaPrincipalAluno", "Química"))
        self.historia.setText(_translate("TelaPrincipalAluno", "História"))
        self.ingles.setText(_translate("TelaPrincipalAluno", "Inglês"))
        self.fisica.setText(_translate("TelaPrincipalAluno", "Física"))
        self.geografia.setText(_translate("TelaPrincipalAluno", "Geografia"))
        self.filosofia.setText(_translate("TelaPrincipalAluno", "Filosofia"))
        self.portugues.setText(_translate("TelaPrincipalAluno", "Português"))
        self.botao_sair.setText(_translate("TelaPrincipalAluno", "Sair"))
import img_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipalAluno = QtWidgets.QWidget()
    ui = Ui_TelaPrincipalAluno()
    ui.setupUi(TelaPrincipalAluno)
    TelaPrincipalAluno.show()
    sys.exit(app.exec_())
