# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TelaPrincipal(object):
    def setupUi(self, TelaPrincipal):
        TelaPrincipal.setObjectName("TelaPrincipal")
        TelaPrincipal.setEnabled(True)
        TelaPrincipal.resize(900, 570)
        TelaPrincipal.setMinimumSize(QtCore.QSize(900, 550))
        TelaPrincipal.setMaximumSize(QtCore.QSize(900, 640))
        TelaPrincipal.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.centralwidget = QtWidgets.QWidget(TelaPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 220, 300, 330))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(300, 330))
        self.scrollArea.setStyleSheet("border: none;\n"
"background-color: rgb(33, 33, 33);")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 283, 372))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(255, 229, 0);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_9)
        self.pushButton_7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.pushButton_11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(252, 88, 20);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout.addWidget(self.pushButton_11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.background_foto = QtWidgets.QFrame(self.centralwidget)
        self.background_foto.setGeometry(QtCore.QRect(65, 20, 170, 170))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background_foto.sizePolicy().hasHeightForWidth())
        self.background_foto.setSizePolicy(sizePolicy)
        self.background_foto.setMinimumSize(QtCore.QSize(170, 170))
        self.background_foto.setMaximumSize(QtCore.QSize(170, 170))
        self.background_foto.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.background_foto.setStyleSheet("border-radius: 85px;\n"
"background-color: rgb(217, 217, 217);")
        self.background_foto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_foto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_foto.setObjectName("background_foto")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(300, 0, 600, 530))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.botao_sair = QtWidgets.QPushButton(self.centralwidget)
        self.botao_sair.setGeometry(QtCore.QRect(10, 10, 40, 20))
        self.botao_sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.botao_sair.setStyleSheet("border-radius: 10px;\n"
"background-color: red;")
        self.botao_sair.setObjectName("botao_sair")
        TelaPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TelaPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        TelaPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TelaPrincipal)
        self.statusbar.setObjectName("statusbar")
        TelaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(TelaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(TelaPrincipal)

    def retranslateUi(self, TelaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        TelaPrincipal.setWindowTitle(_translate("TelaPrincipal", "Tela Principal"))
        self.pushButton.setText(_translate("TelaPrincipal", "Matemática"))
        self.pushButton_2.setText(_translate("TelaPrincipal", "Física"))
        self.pushButton_3.setText(_translate("TelaPrincipal", "História"))
        self.pushButton_4.setText(_translate("TelaPrincipal", "Geografia"))
        self.pushButton_5.setText(_translate("TelaPrincipal", "Filosofia"))
        self.pushButton_9.setText(_translate("TelaPrincipal", "Inglês"))
        self.pushButton_7.setText(_translate("TelaPrincipal", "Português"))
        self.pushButton_11.setText(_translate("TelaPrincipal", "Química"))
        self.botao_sair.setText(_translate("TelaPrincipal", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaPrincipal = QtWidgets.QMainWindow()
    ui = Ui_TelaPrincipal()
    ui.setupUi(TelaPrincipal)
    TelaPrincipal.show()
    sys.exit(app.exec_())