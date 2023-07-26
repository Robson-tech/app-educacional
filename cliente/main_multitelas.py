import sys
import socket
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from cod_tela_principal_aluno import Ui_TelaPrincipalAluno
from cod_tela_principal_professor import Ui_TelaPrincipalProfessor
from cod_tela_atividade_aluno import Ui_TelaAtividade
from cod_tela_atividade_professor import Ui_AtividadeProfessor
from cod_tela_login import Ui_Login
from cod_tela_cadastro import Ui_Cadastro
from modelos import Professor, Aluno, Materia, Turma, Atividade, Questao
import settings
# pyuic5 -x tela_cadastro.ui -o tela_cadastro.py


class Ui_Main(QtWidgets.QWidget):
    """
    Classe que controla as telas do programa

    ...

    Attributes
    ----------
    stack : list
        lista de widgets
    atividades : dict
        dicionário de atividades
    atividades_turma : dict
        dicionário de atividades da turma
    usuario : Professor or Aluno
        usuário logado
    materias : dict
        dicionário de matérias

    Methods
    -------
    get_materias_id(materia_nome)
        retorna o id da matéria
    get_atividade(id_atividade)
        retorna a atividade
    criar_pagina_atividade(atividade)
        cria a página da atividade
    criar_pagina_atividade_turma(turma_id, materia=None, atividade=None)
        cria a página da atividade da turma
    get_atividades_materia(materia_id)
        retorna as atividades da matéria
    get_atividades_turma_professor(turma_id, professor_id)
        retorna as atividades da turma do professor
    enviar_cadastro_atividade(mensagem)
        envia o cadastro da atividade
    cadastrar_tarefa()
        cadastra a tarefa
    submeter_atividade(atividade_id)
        submete a atividade
    enviar_cadastro(mensagem)
        envia o cadastro
    botao_logoff()
        realiza o logoff
    botao_sair()
        realiza o logout
    enviar_login(mensagem)
        envia o login
    botao_login()
        realiza o login
    botao_cadastrar_professor()
        realiza o cadastro do professor
    botao_cadastrar_aluno()
        realiza o cadastro do aluno
    botao_cadastrar()
        realiza o cadastro
    botao_voltar_cadastro()
        volta para a tela de login
    limpar_campos()
        limpa os campos
    """

    def setupUi(self, Main):
        """
        Configura a interface da tela principal

        Parameters
        ----------
        Main : QMainWindow
            janela principal
        """
        Main.setObjectName("Main")
        Main.resize(500, 450)

        self.QtStack = QtWidgets.QStackedLayout()
        self.stack = []
        self.atividades = {}
        self.atividades_turma = {}

        self.tela_login = Ui_Login()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_login.setupUi(self.stack[0])
        self.tela_cadastro = Ui_Cadastro()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_cadastro.setupUi(self.stack[1])
        self.tela_principal_aluno = Ui_TelaPrincipalAluno()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_principal_aluno.setupUi(self.stack[2])
        self.tela_principal_professor = Ui_TelaPrincipalProfessor()
        self.stack.append(QtWidgets.QMainWindow())
        self.tela_principal_professor.setupUi(self.stack[3])

        self.QtStack.addWidget(self.stack[0])
        self.QtStack.addWidget(self.stack[1])
        self.QtStack.addWidget(self.stack[2])
        self.QtStack.addWidget(self.stack[3])


class Main(QMainWindow, Ui_Main):
    """
    Classe que controla as telas do programa

    ...

    Attributes
    ----------
    stack : list
        lista de widgets
    atividades : dict
        dicionário de atividades
    atividades_turma : dict
        dicionário de atividades da turma
    usuario : Professor or Aluno
        usuário logado
    materias : dict
        dicionário de matérias

    Methods
    -------
    get_materias_id(materia_nome)
        retorna o id da matéria
    get_atividade(id_atividade)
        retorna a atividade
    criar_pagina_atividade(atividade)
        cria a página da atividade
    criar_pagina_atividade_turma(turma_id, materia=None, atividade=None)
        cria a página da atividade da turma
    get_atividades_materia(materia_id)
        retorna as atividades da matéria
    get_atividades_turma_professor(turma_id, professor_id)
        retorna as atividades da turma do professor
    enviar_cadastro_atividade(mensagem)
        envia o cadastro da atividade
    cadastrar_tarefa()
        cadastra a tarefa
    submeter_atividade(atividade_id)
        submete a atividade
    enviar_cadastro(mensagem)
        envia o cadastro
    botao_logoff()
        realiza o logoff
    botao_sair()
        realiza o logout
    enviar_login(mensagem)
        envia o login
    botao_login()
        realiza o login
    botao_cadastrar_professor()
        realiza o cadastro do professor
    botao_cadastrar_aluno()
        realiza o cadastro do aluno
    botao_cadastrar()
        realiza o cadastro
    botao_voltar_cadastro()
        volta para a tela de login
    limpar_campos()
        limpa os campos
    """

    def __init__(self, parent=None):
        """
        Construtor da classe

        Parameters
        ----------
        parent : None
            janela principal

        Attributes
        ----------
        stack : list
            lista de widgets
        atividades : dict
            dicionário de atividades
        atividades_turma : dict
            dicionário de atividades da turma
        usuario : Professor or Aluno
            usuário logado
        materias : dict
            dicionário de matérias
        """
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)
        self._usuario = None
        self._materias = {}
        self._turmas = {}
        ip = settings.IP_SERVIDOR
        port = settings.PORTA_SERVIDOR
        addr = ((ip, port))
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(addr)
        self.tela_login.botao_login.clicked.connect(self.botao_login)
        self.tela_login.botao_cadastro.clicked.connect(self.botao_cadastrar)
        self.tela_cadastro.alunos_botao_voltar.clicked.connect(
            self.botao_voltar_cadastro)
        self.tela_cadastro.professor_botao_voltar.clicked.connect(
            self.botao_voltar_cadastro)
        self.tela_cadastro.alunos_botao_cadastrar.clicked.connect(
            self.botao_cadastrar_aluno)
        self.tela_cadastro.professor_botao_cadastrar.clicked.connect(
            self.botao_cadastrar_professor)
        self.tela_principal_aluno.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_aluno.botao_sair.clicked.connect(self.botao_sair)
        self.tela_principal_professor.botao_logoff.clicked.connect(
            self.botao_logoff)
        self.tela_principal_professor.botao_sair.clicked.connect(
            self.botao_sair)

    @property
    def usuario(self):
        return self._usuario

    @usuario.setter
    def usuario(self, usuario_id):
        self._usuario = usuario_id

    @property
    def materias(self):
        return self._materias

    @property
    def turmas(self):
        return self._turmas

    def request_materias(self):
        self._materias = {}
        self.client_socket.send('8'.encode())
        resposta = self.client_socket.recv(1024).decode().split('|')
        for materia in resposta[1].split(',')[:-1]:
            materia_id = materia.split('-')[0]
            materia_nome = materia.split('-')[1]
            self._materias.update(
                {materia_id: Materia(materia_id, materia_nome)})
            if self._usuario:
                atividades = self.get_atividades_materia(materia_id)
                self.tela_principal_aluno.add_materia(
                    materia_nome.capitalize(), atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade)
        self.tela_principal_aluno.inserir_espacamento()

    def request_turmas(self):
        self._turmas = {}
        self.client_socket.send('9'.encode())
        resposta = self.client_socket.recv(1024).decode().split('|')
        for turma in resposta[1].split(',')[:-1]:
            turma_id = turma.split('-')[0]
            turma_nome = turma.split('-')[1]
            turma_numero = turma.split('-')[2]
            self._turmas.update({turma_id: Turma(turma_id, turma_nome, turma_numero)})
            if self._usuario:
                atividades = self.get_atividades_turma_professor(
                    turma_id, self._usuario.id)
                self.tela_principal_professor.add_pagina(
                    f'Turma-{turma_nome}', turma_id, atividades=atividades, funcao_criar_pagina_atividade=self.criar_pagina_atividade_turma)
        self.tela_principal_professor.inserir_espacamento()

    def get_materias_id(self, materia_nome):
        """
        Retorna o id da matéria

        Parameters
        ----------
        materia_nome : str
            nome da matéria

        Returns
        -------
        int or None
            id da matéria ou None se não encontrada
        """
        for materia in self._materias.values():
            if materia.nome == materia_nome:
                return materia.id
        return None

    def get_atividade(self, id_atividade):
        """
        Retorna a atividade

        Parameters
        ----------
        id_atividade : int
            id da atividade

        Returns
        -------
        Atividade or None
            atividade ou None se não encontrada
        """
        self.client_socket.send(f'4|{id_atividade}'.encode())
        questoes = self.client_socket.recv(1024).decode().split('|')
        lista_questoes = []
        while questoes[0] == '4':
            lista_questoes.append(Questao(*questoes[1].split(';;')))
            self.client_socket.send('4'.encode())
            questoes = self.client_socket.recv(1024).decode().split('|')
        atividade_campos = questoes[1].split('//')
        if atividade_campos[0] == 'None':
            return None
        return Atividade(*atividade_campos, lista_questoes)

    def criar_pagina_atividade(self, atividade):
        """
        Cria a página da atividade

        Parameters
        ----------
        atividade : Atividade
            atividade

        Returns
        -------
        function
            função que cria a página da atividade
        """
        self.atividades.update({atividade.id: Ui_TelaAtividade()})
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        self.atividades[atividade.id].setupUi(self.stack[-1], atividade)
        self.QtStack.addWidget(self.stack[-1])
        for i, questao in enumerate(atividade.questoes.values()) if atividade.questoes else []:
            self.atividades[atividade.id].add_questao(i + 1, questao.enunciado, questao.resposta, [
                questao.letra_a, questao.letra_b, questao.letra_c, questao.letra_d, questao.letra_e])
        self.atividades[atividade.id].add_rodape()

        def voltar_atividade():
            self.QtStack.setCurrentIndex(2)
        self.atividades[atividade.id].botao_voltar.clicked.connect(
            voltar_atividade)

        def ir_para_pagina_atividade():
            self.QtStack.setCurrentWidget(novo)

        def submeter_atividade():
            self.submeter_atividade(atividade.id)

        self.atividades[atividade.id].botao_publicar.clicked.connect(
            submeter_atividade)
        return ir_para_pagina_atividade

    def criar_pagina_atividade_turma(self, turma_id, materia=None, atividade=None):
        """
        Cria a página da atividade da turma

        Parameters
        ----------
        turma_id : int
            id da turma
        materia : str, optional
            nome da matéria
        atividade : Atividade, optional
            atividade

        Returns
        -------
        function
            função que cria a página da atividade da turma
        """
        titulo = len(self.stack) + 1
        self.atividades_turma[titulo] = Ui_AtividadeProfessor()
        novo = QtWidgets.QWidget()
        self.stack.append(novo)
        if atividade:
            self.atividades_turma[titulo].setupUi(self.stack[-1], atividade)
            self.atividades_turma[titulo].input_titulo.setText(
                atividade.titulo)
            self.atividades_turma[titulo].input_descricao.setPlainText(
                atividade.descricao)
            self.atividades_turma[titulo].input_materia.setText(
                self._materias[materia].nome)
        else:
            self.atividades_turma[titulo].setupUi(
                self.stack[-1], Atividade(None, None, None, None, turma_id, materia, None))
        self.QtStack.addWidget(self.stack[-1])
        self.atividades_turma[titulo].botao_publicar.clicked.connect(
            self.cadastrar_tarefa)

        def voltar_atividade():
            self.QtStack.setCurrentIndex(3)
        self.atividades_turma[titulo].botao_voltar.clicked.connect(
            voltar_atividade)

        def ir_para_pagina_atividade():
            self.QtStack.setCurrentWidget(novo)
        return ir_para_pagina_atividade

    def get_atividades_materia(self, materia_id):
        """
        Retorna as atividades da matéria

        Parameters
        ----------
        materia_id : int
            id da matéria

        Returns
        -------
        dict
            dicionário de atividades
        """
        self.client_socket.send(f'3|{materia_id}'.encode())
        atividades = self.client_socket.recv(32784).decode().split('|')
        lista_atividades = {}
        for atividade in atividades[1:]:
            atividade_campos = atividade.split('//')[:6]
            lista_questoes = {}
            for questao in atividade.split('//')[6:]:
                questao_campos = questao.split(';;')
                lista_questoes.update(
                    {questao_campos[0]: Questao(*questao_campos)})
            lista_atividades.update(
                {atividade_campos[0]: Atividade(*atividade_campos, lista_questoes)})
        return lista_atividades

    def get_atividades_turma_professor(self, turma_id, professor_id):
        """
        Retorna as atividades da turma do professor

        Parameters
        ----------
        turma_id : int
            id da turma
        professor_id : int
            id do professor

        Returns
        -------
        dict
            dicionário de atividades
        """
        self.client_socket.send(f'5|{turma_id},{professor_id}'.encode())
        atividades = self.client_socket.recv(32784).decode().split('|')
        if len(atividades) == 1:
            return None
        lista_atividades = []
        for atividade in atividades[1:]:
            atividade_campos = atividade.split('//')[:6]
            lista_questoes = {}
            for questao in atividade.split('//')[6:]:
                questao_campos = questao.split(';;')
                lista_questoes.update(
                    {questao_campos[0]: Questao(*questao_campos)})
            lista_atividades.append(
                Atividade(*atividade_campos, lista_questoes))
        return lista_atividades

    def enviar_cadastro_atividade(self, mensagem):
        """
        Envia o cadastro da atividade

        Parameters
        ----------
        mensagem : str
            mensagem de cadastro da atividade para o servidor

        Returns
        -------
        bool
            True se a atividade foi cadastrada com sucesso, False caso contrário
        """
        if mensagem.split('|')[0] == '6':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()
            if resposta and resposta == '6':
                return True
        return False

    def cadastrar_tarefa(self):
        """
        Cadastra a tarefa
        """
        atividade_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.id
        titulo = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_titulo.text()
        descricao = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_descricao.toPlainText()
        materia = self.atividades_turma[
            self.QtStack.currentIndex() + 1].input_materia.text().capitalize()
        turma_id = self.atividades_turma[
            self.QtStack.currentIndex() + 1].atividade.turma_id
        materia_id = self.get_materias_id(materia)
        if materia_id:
            mensagem = f'6|{atividade_id}|{titulo}|{descricao}|{materia_id}|{turma_id}'
            for num in enumerate(self.atividades_turma[self.QtStack.currentIndex() + 1].questoes):
                enunciado = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_enunciado.toPlainText()
                a = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['a'].text()
                b = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['b'].text()
                c = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['c'].text()
                d = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['d'].text()
                e = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].input_letra['e'].text()
                alternativa = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].alternativa_correta()
                id_questao = self.atividades_turma[self.QtStack.currentIndex(
                ) + 1].questoes[num[0]].questao_id
                mensagem += f'|{id_questao}//{enunciado}//{alternativa}//{a}//{b}//{c}//{d}//{e}'
            if self.enviar_cadastro_atividade(mensagem):
                self.criar_pagina_atividade_turma(turma_id, materia)
                QMessageBox.about(
                    self, "Sucesso", "Tarefa cadastrada com sucesso")
                self.QtStack.setCurrentIndex(3)
            else:
                QMessageBox.about(self, "Erro", "Erro ao cadastrar tarefa")
        else:
            QMessageBox.about(self, "Erro", "Matéria não encontrada")

    def submeter_atividade(self, atividade_id):
        """
        Submete a atividade

        Parameters
        ----------
        atividade_id : int
            id da atividade a ser submetida ao servidor
        """
        aluno_id = self.usuario.id
        mensagem = f'7|{atividade_id}|{aluno_id}'
        acertos = 0
        for q in self.atividades[atividade_id].questoes:
            if self.atividades[atividade_id].questoes[q].alternativa_selecionada() == self.atividades[atividade_id].questoes[q].resposta:
                acertos += 1
        mensagem += f'|{acertos}'
        self.client_socket.send(mensagem.encode())
        resposta = self.client_socket.recv(1024).decode()
        if resposta and resposta == '7':
            QMessageBox.about(
                self, "Sucesso", "Atividade submetida com sucesso")
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.about(self, "Erro", "Erro ao submeter atividade")

    def enviar_cadastro(self, mensagem):
        """
        Envia o cadastro

        Parameters
        ----------
        mensagem : str
            mensagem de cadastro para o servidor

        Returns
        -------
        bool
            True se o cadastro foi realizado com sucesso, False caso contrário
        """
        if mensagem.split('|')[0] == '2':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode()

            if resposta and resposta == '2':
                return True
        return False

    def botao_logoff(self):
        """
        Realiza o logoff
        """
        if isinstance(self.usuario, Professor):
            self.tela_principal_professor.limpar_paginas()
        elif isinstance(self.usuario, Aluno):
            self.tela_principal_aluno.limpar_paginas()
            self.tela_principal_aluno.limpar_materias()
        self.client_socket.send('0'.encode())
        self.usuario = None
        self.QtStack.setCurrentIndex(0)

    def botao_sair(self):
        """
        Encerra o programa
        """
        mensagem = '-1'
        self.client_socket.send(mensagem.encode())
        self.client_socket.close()
        exit()

    def enviar_login(self, mensagem):
        """
        Envia o login

        Parameters
        ----------
        mensagem : str
            mensagem a ser enviada para o servidor

        Returns
        -------
        bool or list
            False se o login falhou, lista com os dados do usuário se o login foi realizado com sucesso
        """
        logou = False
        if mensagem.split('|')[0] == '1':
            self.client_socket.send(mensagem.encode())
            resposta = self.client_socket.recv(1024).decode().split('|')

            if resposta and resposta[0] == '1':
                self.usuario = Professor(
                    *resposta[1].split(','), materias_professor=resposta[2].split(',')[:-1])
            elif resposta and resposta[0] == '2':
                self.usuario = Aluno(*resposta[1].split(','))

            resposta = self.client_socket.recv(1024).decode().split('|')

            if resposta and resposta != '0':
                logou = resposta
        return logou

    def botao_login(self):
        """
        Realiza o login
        """
        email = self.tela_login.caixa_email.text()
        senha = self.tela_login.caixa_senha.text()
        mensagem = f'1|{email},{senha}'

        if email and senha:
            resposta = self.enviar_login(mensagem)
            if resposta:
                self.request_materias()
                if resposta[0] == '1':
                    self.request_turmas()
                    self.QtStack.setCurrentIndex(3)
                elif resposta[0] == '2':
                    self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.about(self, "Erro", "E-mail ou senha incorretos")
        else:
            QMessageBox.about(self, "Erro", "E-mail ou senha não preenchidos")

    def botao_cadastrar_professor(self):
        """
        Realiza o cadastro do professor
        """
        email = self.tela_cadastro.professor_caixa_email.text()
        senha1 = self.tela_cadastro.professor_caixa_senha1.text()
        senha2 = self.tela_cadastro.professor_caixa_senha2.text()
        nome = self.tela_cadastro.professor_caixa_nome.text()
        sobrenome = self.tela_cadastro.professor_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.professor_caixa_nascimento.text()
        materias = self.tela_cadastro.get_materias()
        turmas = self.tela_cadastro.get_turmas()
        mensagem = f'2|{email},{senha1},{nome},{sobrenome},{nascimento},{materias},{turmas},p'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(
                        self, "Sucesso", "Professor cadastrado com sucesso")
                    self.request_turmas()
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(3)
                else:
                    QMessageBox.about(
                        self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def botao_cadastrar_aluno(self):
        """
        Realiza o cadastro do aluno
        """
        email = self.tela_cadastro.alunos_caixa_email.text()
        senha1 = self.tela_cadastro.alunos_caixa_senha1.text()
        senha2 = self.tela_cadastro.alunos_caixa_senha2.text()
        nome = self.tela_cadastro.alunos_caixa_nome.text()
        sobrenome = self.tela_cadastro.alunos_caixa_sobrenome.text()
        nascimento = self.tela_cadastro.alunos_caixa_nascimento.text()
        turma = self.tela_cadastro.alunos_comboBox_turmas.currentText()
        mensagem = f'2|{email},{senha1},{nome},{sobrenome},{nascimento},{turma},a'
        if email and senha1 and senha2 and nome and sobrenome and nascimento:
            if senha1 == senha2:
                if self.enviar_cadastro(mensagem):
                    QMessageBox.about(
                        self, "Sucesso", "Aluno cadastrado com sucesso")
                    self.request_materias()
                    self.limpar_campos()
                    self.QtStack.setCurrentIndex(2)
                else:
                    QMessageBox.about(
                        self, "Erro", "E-mail de usuário já cadastrado")
            else:
                QMessageBox.about(self, "Erro", "Senhas não coincidem")
        else:
            QMessageBox.about(self, "Erro", "Preencha todos os campos")

    def botao_cadastrar(self):
        """
        Realiza o cadastro
        """
        self.request_materias()
        self.request_turmas()
        self.tela_cadastro.set_turmas(self._turmas)
        self.tela_cadastro.set_materias(self._materias)
        self.QtStack.setCurrentIndex(1)

    def botao_voltar_cadastro(self):
        """
        Volta para a tela de login
        """
        self.QtStack.setCurrentIndex(0)

    def limpar_campos(self):
        """
        Limpa os campos de cadastro de professor e aluno
        """
        self.tela_cadastro.alunos_caixa_email.clear()
        self.tela_cadastro.alunos_caixa_senha1.clear()
        self.tela_cadastro.alunos_caixa_senha2.clear()
        self.tela_cadastro.alunos_caixa_nome.clear()
        self.tela_cadastro.alunos_caixa_sobrenome.clear()
        self.tela_cadastro.alunos_caixa_nascimento.setDate(
            QtCore.QDate(2000, 1, 1))
        self.tela_cadastro.alunos_comboBox_turmas.setCurrentIndex(0)
        self.tela_cadastro.professor_caixa_email.clear()
        self.tela_cadastro.professor_caixa_senha1.clear()
        self.tela_cadastro.professor_caixa_senha2.clear()
        self.tela_cadastro.professor_caixa_nome.clear()
        self.tela_cadastro.professor_caixa_sobrenome.clear()
        self.tela_cadastro.professor_caixa_nascimento.setDate(
            QtCore.QDate(2000, 1, 1))
        self.tela_cadastro.professor_comboBox_materias.setCurrentIndex(0)
        self.tela_cadastro.professor_comboBox_turmas.setCurrentIndex(0)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Main()
    sys.exit(app.exec_())
