import socket
import threading
import mysql.connector as mysql
from modelos import Professor, Aluno, Materia, Turma, Atividade, Questao
import settings


class SistemaEducacional:
    """
    Classe que representa o sistema educacional e implementa todos os atributos e metodos necessarios para o funcionamento do sistema.

    ...

    Attributes
    ----------
    mydb : mysql.connector.connection.MySQLConnection
        Conexao com o banco de dados.
    cursor : mysql.connector.cursor.MySQLCursor
        Cursor para executar comandos SQL.
    usuario : Professor ou Aluno
        Usuario logado no sistema.
    materias : dict
        Dicionario com todas as materias cadastradas no sistema.
    turmas : dict
        Dicionario com todas as turmas cadastradas no sistema.

    Methods
    -------
    get_materias()
        Retorna um dicionario com todas as materias cadastradas no sistema.
    get_turmas()
        Retorna um dicionario com todas as turmas cadastradas no sistema.
    get_alunos_turma(turma_id)
        Retorna um dicionario com todos os alunos de uma turma.
    get_professores_turma(turma_id)
        Retorna um dicionario com todos os professores de uma turma.
    get_atividade(id_atividade)
        Retorna uma atividade.
    get_questoes_atividade(id_atividade)
        Retorna um dicionario com todas as questoes de uma atividade.
    get_atividades_professor(professor_id)
        Retorna um dicionário com todas as atividades de um professor.
    get_atividades_turma_professor(turma_id, professor_id)
        Retorna um dicionario com todas as atividades de uma turma de um professor.
    get_turmas_professor(professor_id)
        Retorna um dicionario com todas as turmas de um professor.
    get_atividades_materia(materia_id)
        Retorna um dicionario com todas as atividades de uma materia.
    get_atividades_turma(turma_id)
        Retorna um dicionario com todas as atividades de uma turma.
    buscar(email)
        Retorna uma tupla com os dados de um usuario.
    submeter_atividade(atividade_id, aluno_id, pontuacao)
        Submete uma atividade de um aluno.
    cadastrar_professor(email, senha, nome, sobrenome, nascimento)
        Cadastra um professor no sistema.
    cadastrar_aluno(email, senha, nome, sobrenome, nascimento, turma)
        Cadastra um aluno no sistema.
    login_professor(usuario)
        Realiza o login de um professor.
    login_aluno(usuario)
        Realiza o login de um aluno.
    autenticar(email, senha)
        Autentica um usuário.
    login(email, senha)
        Realiza o login de um usuário.
    cadastrar_atividade(nome, descricao, materia, turma, id=None)
        Cadastra uma atividade no sistema.
    cadastrar_questao(atividade_id, enunciado, resposta, a, b, c, d, e, id=None)
        Cadastra uma questao no sistema.
    logout()
        Realiza o logout de um usuario.
    fechar_bd()
        Fecha a conexao com o banco de dados.
    """

    def __init__(self):
        """
        Parameters
        ----------
        mydb : mysql.connector.connection.MySQLConnection
            Conexão com o banco de dados.
        cursor : mysql.connector.cursor.MySQLCursor
            Cursor para executar comandos SQL.
        usuario : Professor ou Aluno
            Usuario logado no sistema.
        materias : dict
            Dicionario com todas as materias cadastradas no sistema.
        turmas : dict
            Dicionario com todas as turmas cadastradas no sistema.
        """
        self._mydb = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            auth_plugin='mysql_native_password',
            consume_results=True
        )
        self._cursor = self._mydb.cursor()
        consulta_sql = "CREATE DATABASE IF NOT EXISTS sistema_educacional"
        self._cursor.execute(consulta_sql)
        for tabela in settings.TABELAS_SISTEMA_EDUCACIONAL:
            self._cursor.execute(settings.TABELAS_SISTEMA_EDUCACIONAL[tabela])
        self._mydb.commit()
        self._usuario = None
        self._materias = self.get_materias()
        self._turmas = self.get_turmas()

    @property
    def usuario(self):
        return self._usuario

    @property
    def materias(self):
        return self._materias

    @property
    def turmas(self):
        return self._turmas

    def get_materias(self):
        """
        Retorna um dicionario com todas as materias cadastradas no sistema.

        Returns
        -------
        dict
            Dicionario com todas as materias cadastradas no sistema.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.materias"
        self._cursor.execute(consulta_sql)
        materias = {}
        for materia in self._cursor.fetchall():
            atividades = self.get_atividades_materia(materia[0])
            materias.update({materia[0]: Materia(*materia, atividades)})
        return materias

    def get_turmas(self):
        """
        Retorna um dicionario com todas as turmas cadastradas no sistema.

        Returns
        -------
        dict
            Dicionario com todas as turmas cadastradas no sistema.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.turmas"
        self._cursor.execute(consulta_sql)
        turmas = {}
        for turma in self._cursor.fetchall():
            atividades = self.get_atividades_turma(turma[0])
            alunos = self.get_alunos_turma(turma[0])
            professores = self.get_professores_turma(turma[0])
            turmas.update(
                {turma[0]: Turma(*turma, atividades, alunos, professores)})
        return turmas

    def get_alunos_turma(self, turma_id):
        """
        Retorna um dicionario com todos os alunos de uma turma.

        Parameters
        ----------
        turma_id : int
            ID da turma.

        Returns
        -------
        dict
            Dicionario com todos os alunos de uma turma.
        """
        consulta_sql = "SELECT sistema_educacional.alunos.id, sistema_educacional.usuarios.nome FROM sistema_educacional.alunos INNER JOIN sistema_educacional.usuarios ON sistema_educacional.alunos.usuario_id = sistema_educacional.usuarios.id WHERE sistema_educacional.alunos.turma_id = %s"
        parametros_consulta = (turma_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        alunos = {}
        for aluno in self._cursor.fetchall():
            alunos.update({aluno[0]: aluno})
        return alunos

    def get_professores_turma(self, turma_id):
        """
        Retorna um dicionario com todos os professores de uma turma.

        Parameters
        ----------
        turma_id : int
            ID da turma.

        Returns
        -------
        dict
            Dicionario com todos os professores de uma turma.
        """
        consulta_sql = "SELECT sistema_educacional.professores.id, sistema_educacional.usuarios.nome FROM sistema_educacional.professores INNER JOIN sistema_educacional.usuarios ON sistema_educacional.professores.usuario_id = sistema_educacional.usuarios.id INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.professores.id = sistema_educacional.turmas_professores.professor_id WHERE sistema_educacional.turmas_professores.turma_id = %s"
        parametros_consulta = (turma_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        professores = {}
        for professor in self._cursor.fetchall():
            professores.update({professor[0]: professor})
        return professores

    def get_atividade(self, id_atividade):
        """
        Retorna uma atividade.

        Parameters
        ----------
        id_atividade : int
            ID da atividade.

        Returns
        -------
        Atividade
            Objeto da classe Atividade, caso exista. Caso contrario, retorna None.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.id = %s"
        parametros_consulta = (id_atividade,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        atividade = self._cursor.fetchone()
        if atividade:
            questoes = self.get_questoes_atividade(atividade[0])
            return Atividade(*atividade, questoes)
        else:
            return None

    def get_questoes_atividade(self, id_atividade):
        """
        Retorna um dicionario com todas as questoes de uma atividade.

        Parameters
        ----------
        id_atividade : int
            ID da atividade.

        Returns
        -------
        dict
            Dicionario com todas as questoes de uma atividade.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.questoes WHERE sistema_educacional.questoes.atividade_id = %s"
        parametros_consulta = (id_atividade,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        questoes_atividade = {}
        for questao in self._cursor.fetchall():
            questoes_atividade.update({questao[0]: Questao(*questao)})
        return questoes_atividade

    def get_atividades_professor(self, professor_id):
        """
        Retorna um dicionario com todas as atividades de um professor.

        Parameters
        ----------
        professor_id : int
            ID do professor.

        Returns
        -------
        dict
            Dicionario com todas as atividades de um professor.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.professor_id = %s"
        parametros_consulta = (professor_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def get_atividades_turma_professor(self, turma_id, professor_id):
        """
        Retorna um dicionario com todas as atividades de uma turma de um professor.

        Parameters
        ----------
        turma_id : int
            ID da turma.
        professor_id : int
            ID do professor.

        Returns
        -------
        dict
            Dicionario com todas as atividades de uma turma de um professor.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.turma_id = %s AND sistema_educacional.atividades.professor_id = %s"
        parametros_consulta = (turma_id, professor_id)
        self._cursor.execute(consulta_sql, parametros_consulta)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def get_turmas_professor(self, professor_id):
        """
        Retorna um dicionario com todas as turmas de um professor.

        Parameters
        ----------
        professor_id : int
            ID do professor.

        Returns
        -------
        dict
            Dicionario com todas as turmas de um professor.
        """
        consulta_sql = "SELECT sistema_educacional.turmas.id, sistema_educacional.turmas.nome, sistema_educacional.turmas.num_sala FROM sistema_educacional.turmas INNER JOIN sistema_educacional.turmas_professores WHERE sistema_educacional.turmas_professores.professor_id = %s AND sistema_educacional.turmas_professores.turma_id = sistema_educacional.turmas.id"
        parametros_consulta = (professor_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        turmas = {}
        for turma in self._cursor.fetchall():
            atividades = self.get_atividades_turma_professor(
                turma[0], professor_id)
            alunos = self.get_alunos_turma(turma[0])
            professores = self.get_professores_turma(turma[0])
            turmas.update(
                {turma[0]: Turma(*turma, atividades, alunos, professores)})
        return turmas

    def get_atividades_materia(self, materia_id):
        """
        Retorna um dicionario com todas as atividades de uma materia.

        Parameters
        ----------
        materia_id : int
            ID da materia.

        Returns
        -------
        dict
            Dicionario com todas as atividades de uma materia.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.atividades WHERE materia_id = %s"
        parametros_consulta = (materia_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        atividades_materia = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            atividades_materia.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return atividades_materia

    def get_atividades_turma(self, turma_id):
        """
        Retorna um dicionario com todas as atividades de uma turma.

        Parameters
        ----------
        turma_id : int
            ID da turma.

        Returns
        -------
        dict
            Dicionario com todas as atividades de uma turma.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.turma_id = %s"
        parametros_consulta = (turma_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def buscar(self, email):
        """
        Retorna uma tupla com os dados de um usuario.

        Parameters
        ----------
        email : str
            Email do usuario.

        Returns
        -------
        tuple
            Tupla com os dados de um usuario.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s"
        parametros_consulta = (email,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        return self._cursor.fetchone()

    def submeter_atividade(self, atividade_id, aluno_id, pontuacao):
        """
        Submete uma atividade de um aluno.

        Parameters
        ----------
        atividade_id : int
            ID da atividade.
        aluno_id : int
            ID do aluno.
        pontuacao : int
            Pontuacao do aluno na atividade.

        Returns
        -------
        bool
            True, caso a atividade tenha sido submetida com sucesso. Caso contrario, retorna False.
        """
        consulta_sql = "SELECT COUNT(*) FROM sistema_educacional.questoes WHERE sistema_educacional.questoes.atividade_id = %s"
        parametros_consulta = (atividade_id,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        total_questoes = self._cursor.fetchone()[0]
        if total_questoes == 0:
            return False
        else:
            taxa_acerto = int(pontuacao) / total_questoes * 100
            consulta_sql = "INSERT INTO sistema_educacional.atividades_alunos (atividade_id, aluno_id, pontuacao, taxa_acerto) VALUES (%s, %s, %s, %s)"
            parametros_consulta = (
                atividade_id, aluno_id, pontuacao, taxa_acerto)
            self._cursor.execute(consulta_sql, parametros_consulta)
            self._mydb.commit()
            return True

    def cadastrar_professor(self, email, senha, nome, sobrenome, nascimento):
        """
        Cadastra um professor no sistema.

        Parameters
        ----------
        email : str
            Email do professor.
        senha : str
            Senha do professor.
        nome : str
            Nome do professor.
        sobrenome : str
            Sobrenome do professor.
        nascimento : str
            Data de nascimento do professor.

        Returns
        -------
        bool
            True, caso o professor tenha sido cadastrado com sucesso. Caso contrario, retorna False.
        """
        if self.buscar(email):
            return False
        consulta_sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        parametros_consulta = (email, senha, nome, sobrenome, nascimento)
        self._cursor.execute(consulta_sql, parametros_consulta)
        self._mydb.commit()
        consulta_sql = 'SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login FROM sistema_educacional.usuarios WHERE email = %s'
        parametros_consulta = (email,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        id, data_cadastro, ultimo_login = self._cursor.fetchone()
        professor = Professor(id, email, senha, nome, sobrenome,
                              nascimento, data_cadastro, ultimo_login)
        self._usuario = professor

        consulta_sql = "INSERT INTO sistema_educacional.professores (usuario_id, salario) VALUES (%s, %s)"
        parametros_consulta = (professor.id, 1320)
        self._cursor.execute(consulta_sql, parametros_consulta)
        self._mydb.commit()
        return True

    def cadastrar_aluno(self, email, senha, nome, sobrenome, nascimento, turma):
        """
        Cadastra um aluno no sistema.

        Parameters
        ----------
        email : str
            Email do aluno.
        senha : str
            Senha do aluno.
        nome : str
            Nome do aluno.
        sobrenome : str
            Sobrenome do aluno.
        nascimento : str
            Data de nascimento do aluno.
        turma : str
            Nome da turma do aluno.

        Returns
        -------
        bool
            True, caso o aluno tenha sido cadastrado com sucesso. Caso contrario, retorna False.
        """
        if self.buscar(email):
            return False
        consulta_sql = "SELECT sistema_educacional.turmas.id FROM sistema_educacional.turmas WHERE sistema_educacional.turmas.nome = %s"
        parametros_consulta = (turma,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        try:
            turma_id = self._cursor.fetchone()[0]
        except:
            return False
        consulta_sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        parametros_consulta = (email, senha, nome,
                               sobrenome, nascimento)
        self._cursor.execute(consulta_sql, parametros_consulta)
        self._mydb.commit()
        consulta_sql = 'SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login FROM sistema_educacional.usuarios WHERE email = %s'
        parametros_consulta = (email,)
        self._cursor.execute(consulta_sql, parametros_consulta)
        id, data_cadastro, ultimo_login = self._cursor.fetchone()
        aluno = Aluno(id, email, senha, nome, sobrenome,
                      nascimento, data_cadastro, ultimo_login, turma)
        self._usuario = aluno

        consulta_sql = "INSERT INTO sistema_educacional.alunos (usuario_id, pontuacao_geral, turma_id) VALUES (%s, %s, %s)"
        parametros_consulta = (aluno.id, 0, turma_id)
        self._cursor.execute(consulta_sql, parametros_consulta)
        self._mydb.commit()
        return True

    def login_professor(self, usuario):
        """
        Realiza o login de um professor.

        Parameters
        ----------
        usuario : tuple
            Tupla com os dados do usuario.

        Returns
        -------
        bool
            True, caso o professor tenha sido logado com sucesso. Caso contrario, retorna False.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.professores WHERE sistema_educacional.professores.usuario_id = %s"
        parametros_consulta = (usuario[0],)
        self._cursor.execute(consulta_sql, parametros_consulta)
        consulta = self._cursor.fetchone()
        if consulta:
            consulta_sql = "SELECT sistema_educacional.materias.id, sistema_educacional.materias.nome FROM sistema_educacional.materias INNER JOIN sistema_educacional.materias_professores ON sistema_educacional.materias_professores.materia_id = sistema_educacional.materias.id WHERE sistema_educacional.materias_professores.professor_id = %s"
            parametros_consulta = (consulta[0],)
            self._cursor.execute(consulta_sql, parametros_consulta)
            materias = self._cursor.fetchall()
            turmas = self.get_turmas_professor(consulta[0])
            atividades = self.get_atividades_professor(consulta[0])
            professor = Professor(
                consulta[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5],
                usuario[6], usuario[7], materias_professor=materias, turmas_professor=turmas, atividades_professor=atividades, salario=consulta[2]
            )
            self._usuario = professor
            consulta_sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
            parametros_consulta = (usuario[0],)
            self._cursor.execute(consulta_sql, parametros_consulta)
            self._mydb.commit()
            return True
        else:
            return False

    def login_aluno(self, usuario):
        """
        Realiza o login de um aluno.

        Parameters
        ----------
        usuario : tuple
            Tupla com os dados do usuario.

        Returns
        -------
        bool
            True, caso o aluno tenha sido logado com sucesso. Caso contrario, retorna False.
        """
        consulta_sql = "SELECT * FROM sistema_educacional.alunos WHERE sistema_educacional.alunos.usuario_id = %s"
        parametros_consulta = (usuario[0],)
        self._cursor.execute(consulta_sql, parametros_consulta)
        consulta = self._cursor.fetchone()
        if consulta:
            aluno = Aluno(
                consulta[0], usuario[1], usuario[2], usuario[3], usuario[4],
                usuario[5], usuario[6], usuario[7], consulta[2], pontuacao=consulta[3]
            )
            self._usuario = aluno
            consulta_sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
            parametros_consulta = (usuario[0],)
            self._cursor.execute(consulta_sql, parametros_consulta)
            self._mydb.commit()
            return True
        else:
            return False

    def autenticar(self, email, senha):
        consulta_sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s AND senha = %s"
        parametros_consulta = (email, senha)
        self._cursor.execute(consulta_sql, parametros_consulta)
        return self._cursor.fetchone()

    def login(self, email, senha):
        usuario = self.autenticar(email, senha)
        if usuario:
            if not self.login_professor(usuario):
                self.login_aluno(usuario)
            return True
        else:
            return False

    def cadastrar_atividade(self, nome, descricao, materia, turma, id=None):
        """
        Cadastra uma atividade no sistema.

        Parameters
        ----------
        nome : str
            Nome da atividade.
        descricao : str
            Descricao da atividade.
        materia : int
            ID da materia.
        turma : int
            ID da turma.
        id : int, optional
            ID da atividade. O valor padrao e None.

        Returns
        -------
        Atividade
            Objeto da classe Atividade, caso a atividade tenha sido cadastrada com sucesso. Caso contrario, retorna None.
        """
        retorno = None
        try:
            if id:
                consulta_sql = "UPDATE sistema_educacional.atividades SET nome = %s, descricao = %s, materia_id = %s, turma_id = %s WHERE id = %s"
                parametros_consulta = (nome, descricao, materia, turma, id)
                self._cursor.execute(consulta_sql, parametros_consulta)
                self._mydb.commit()
                retorno = Atividade(id, nome, descricao,
                                    self.usuario.id, turma, materia)
            else:
                consulta_sql = "INSERT INTO sistema_educacional.atividades (nome, descricao, professor_id, turma_id, materia_id) VALUES (%s, %s, %s, %s, %s)"
                parametros_consulta = (
                    nome, descricao, self.usuario.id, turma, materia)
                self._cursor.execute(consulta_sql, parametros_consulta)
                self._mydb.commit()
                retorno = Atividade(
                    self._cursor.lastrowid, nome, descricao, self.usuario.id, turma, materia)
        except Exception as e:
            print('Erro ao cadastrar atividade:', str(e))
        return retorno

    def cadastrar_questao(self, atividade_id, enunciado, resposta, a, b, c, d, e, id=None):
        """
        Cadastra uma questao no sistema.

        Parameters
        ----------
        atividade_id : int
            ID da atividade.
        enunciado : str
            Enunciado da questao.
        resposta : str
            Resposta da questao.
        a : str
            Alternativa A.
        b : str
            Alternativa B.
        c : str
            Alternativa C.
        d : str
            Alternativa D.
        e : str
            Alternativa E.
        id : int, optional
            ID da questao. O valor padrao e None.

        Returns
        -------
        Questao
            Objeto da classe Questao, caso a questao tenha sido cadastrada com sucesso. Caso contrario, retorna None.
        """
        retorno = None
        try:
            if id:
                consulta_sql = "UPDATE sistema_educacional.questoes SET enunciado = %s, resposta = %s, letra_a = %s, letra_b = %s, letra_c = %s, letra_d = %s, letra_e = %s WHERE id = %s"
                parametros_consulta = (enunciado, resposta, a, b, c, d, e, id)
                self._cursor.execute(consulta_sql, parametros_consulta)
                self._mydb.commit()
                retorno = Questao(id, atividade_id, enunciado,
                                  resposta, a, b, c, d, e)
            else:
                consulta_sql = "INSERT INTO sistema_educacional.questoes (atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                parametros_consulta = (
                    atividade_id, enunciado, resposta, a, b, c, d, e)
                self._cursor.execute(consulta_sql, parametros_consulta)
                self._mydb.commit()
                retorno = Questao(self._cursor.lastrowid,
                                  atividade_id, enunciado, resposta, a, b, c, d, e)
        except Exception as e:
            print('Erro ao cadastrar questão:', str(e))
        return retorno

    def logout(self):
        """
        Realiza o logout de um usuario.
        """
        self._usuario = None

    def fechar_bd(self):
        """
        Fecha a conexao com o banco de dados.
        """
        self._mydb.close()


class MyThread(threading.Thread):
    """
    Classe para criar uma thread para cada cliente conectado ao servidor.

    ...

    Attributes
    ----------
    name : str
        Nome da thread.
    sistema : SistemaEducacional
        Sistema educacional.
    client_address : tuple
        Endereço do cliente.
    client_socket : socket.socket
        Socket do cliente.
    serv_socket : socket.socket
        Socket do servidor.

    Methods
    -------
    run()
        Executa a thread.
    """
    def __init__(self, serv_socket, client_address, client_socket):
        """
        Parameters
        ----------
        client_address : tuple
            Endereço do cliente.
        serv_socket : socket.socket
            Socket do servidor.
        client_socket : socket.socket
            Socket do cliente.
        """
        threading.Thread.__init__(self)
        self.name = None
        self.sistema = SistemaEducacional()
        self.serv_socket = serv_socket
        self.client_address = client_address
        self.client_socket = client_socket
        print(f'Nova conexão, endereço: {self.client_address}')

    def run(self):
        """
        Executa a thread.
        """
        enviar = '1|'
        for materia in self.sistema.materias.values():
            enviar += f'{materia.id}-{materia.nome},'
        enviar += '0'
        self.client_socket.send(enviar.encode())
        while True:
            try:
                mensagem = self.client_socket.recv(32784)
                mensagem_str = mensagem.decode().split('|')

                if mensagem_str[0] == '1':
                    login = mensagem_str[1].split(',')
                    email = login[0]
                    senha = login[1]
                    if self.sistema.login(email, senha):
                        if isinstance(self.sistema.usuario, Professor):
                            enviar = f'1|{self.sistema.usuario}|{self.sistema.usuario.get_materias_id()}0'
                            self.client_socket.send(enviar.encode())
                            enviar = '1|'
                            for materia in self.sistema.usuario.materias:
                                enviar += f"{materia[0]},"
                            enviar += '0|'
                            for turma in self.sistema.usuario.turmas.values():
                                enviar += f'{turma.id}-{turma.nome},'
                            print(
                                f'Professor {self.sistema.usuario.email} logou em {self.client_address}')
                        elif isinstance(self.sistema.usuario, Aluno):
                            enviar = f'2|{self.sistema.usuario}'
                            self.client_socket.send(enviar.encode())
                            enviar = '2'
                            print(
                                f'Aluno {self.sistema.usuario.email} logou em {self.client_address}')
                    else:
                        enviar = '0'
                        print(f'Erro no login em {self.client_address}')
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '2':
                    cadastro = mensagem_str[1].split(',')
                    email = cadastro[0]
                    senha = cadastro[1]
                    nome = cadastro[2]
                    sobrenome = cadastro[3]
                    nascimento = cadastro[4]
                    if cadastro[-1] == 'a':
                        turma = cadastro[5]
                        if self.sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento, turma):
                            enviar = '2'
                            print(
                                f'Aluno {self.sistema.usuario.email} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastro aluno no sistema em {self.client_address}')
                    elif cadastro[-1] == 'p':
                        if self.sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                            enviar = '2'
                            print(
                                f'Professor {self.sistema.usuario.email} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastrar professor no sistema em {self.client_address}')
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '3':
                    materia_id = mensagem_str[1]
                    enviar = f'3'
                    for atividade in self.sistema.get_atividades_materia(materia_id).values():
                        enviar += f'|{atividade}'
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '4':
                    for questao in self.sistema.get_questoes_atividade(mensagem_str[1]).values():
                        enviar = f'4|{questao}'
                        self.client_socket.send(enviar.encode())
                        self.client_socket.recv(1024)
                    atividade = self.sistema.get_atividade(mensagem_str[1])
                    self.client_socket.send(f'0|{atividade}'.encode())
                elif mensagem_str[0] == '5':
                    turmas_professor = mensagem_str[1].split(',')
                    turma_id = turmas_professor[0]
                    professor_id = turmas_professor[1]
                    enviar = f'5'
                    for atividade in self.sistema.get_atividades_turma_professor(turma_id, professor_id).values():
                        enviar += f'|{atividade}'
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '6':
                    atividade_id = mensagem_str[1] if mensagem_str[1] != 'None' else None
                    titulo = mensagem_str[2] if mensagem_str[2] != 'None' else None
                    descricao = mensagem_str[3] if mensagem_str[3] != 'None' else None
                    materia = int(
                        mensagem_str[4]) if mensagem_str[4] != 'None' else None
                    turma = int(
                        mensagem_str[5]) if mensagem_str[5] != 'None' else None
                    nova = self.sistema.cadastrar_atividade(
                        titulo, descricao, materia, turma, atividade_id)
                    if not nova:
                        self.client_socket.send('-6'.encode())
                        print(
                            f'Erro ao cadastrar atividade em {self.client_address}')
                    else:
                        try:
                            for questao in mensagem_str[6:]:
                                q = questao.split('//')
                                if q[0] == 'None':
                                    q[0] = None
                                if not self.sistema.cadastrar_questao(
                                        nova.id, q[1], q[2], q[3], q[4], q[5], q[6], q[7], id=q[0]):
                                    raise Exception(
                                        f'Erro ao cadastrar questao em {self.client_address}')
                            print(
                                f'Atividade {titulo} cadastrada em {self.client_address}')
                            self.client_socket.send('6'.encode())
                        except:
                            self.client_socket.send('-6'.encode())
                            print(
                                f'Erro ao cadastrar atividade em {self.client_address}')
                elif mensagem_str[0] == '7':
                    atividade_id = mensagem_str[1]
                    aluno_id = mensagem_str[2]
                    pontuacao = mensagem_str[3]
                    if self.sistema.submeter_atividade(
                            atividade_id, aluno_id, pontuacao):
                        enviar = '7'
                        print(
                            f'Atividade {atividade_id} submetida por {aluno_id} em {self.client_address}')
                    else:
                        enviar = '-7'
                        print(
                            f'Erro ao submeter atividade {atividade_id} por {aluno_id} em {self.client_address}')
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '0':
                    print(
                        f'Usuário {self.sistema.usuario.email} deslogou em {self.client_address}')
                    self.sistema.logout()
                elif mensagem_str[0] == '-1':
                    print(f'Conexão com {self.client_address} finalizada')
                    self.client_socket.close()
                    self.sistema.fechar_bd()
                    break
                else:
                    raise Exception(
                        f'Conexão com {self.client_address} finalizada inesperadamente')
            except Exception as e:
                print(str(e))
                self.client_socket.close()
                self.sistema.fechar_bd()
                break


class Servidor:
    """
    Classe que representa o servidor do sistema.

    ...

    Attributes
    ----------
    host : str
        Endereço do servidor.
    port : int
        Porta do servidor.
    addr : tuple
        Tupla com o endereço e a porta do servidor.
    serv_socket : socket
        Socket do servidor.

    Methods
    -------
    iniciar()
        Inicia o servidor.
    """

    def __init__(self):
        """
        Parameters
        ----------
        host : str
            Endereço do servidor.
        port : int
            Porta do servidor.
        addr : tuple
            Tupla com o endereço e a porta do servidor.
        serv_socket : socket
            Socket do servidor.
        """
        self.host = settings.IP_SERVIDOR
        self.port = settings.PORTA_SERVIDOR
        self.addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)
        print('Aguardando conexão...')

    def iniciar(self):
        """
        Inicia o servidor.
        """
        while True:
            try:
                client_socket, client_address = self.serv_socket.accept()
                my_thread = MyThread(self.serv_socket, client_address, client_socket)
                my_thread.start()
            except KeyboardInterrupt:
                print('Servidor encerrado')
                self.serv_socket.close()
                break
            except Exception as e:
                print(str(e))
                self.serv_socket.close()
                break


class Teste:
    """
    Classe para testar o sistema.

    ...

    Attributes
    ----------
    sistema : SistemaEducacional
        Sistema educacional.
    """
    def __init__(self):
        """
        Parameters
        ----------
        sistema : SistemaEducacional
            Sistema educacional.
        """
        self.sistema = SistemaEducacional()

    def iniciar(self):
        """
        Inicia o teste.
        """
        opc = 1
        while opc:
            try:
                if opc == 1:
                    print('Login')
                    email = input('E-mail: ')
                    senha = input('Senha: ')
                    if self.sistema.login(email, senha):
                        if isinstance(self.sistema.usuario, Professor):
                            print(
                                f'Professor {self.sistema.usuario.email} logado no sistema')
                        elif isinstance(self.sistema.usuario, Aluno):
                            print(
                                f'Aluno {self.sistema.usuario.email} logado no sistema')
                    else:
                        print('Erro no login')
                elif opc == 2:
                    print(
                        'Cadastro\n'
                        '1 - Professor\n'
                        '2 - Aluno\n'
                        '0 - Voltar'
                    )
                    opc = int(input())
                    email = input('E-mail: ')
                    senha1 = input('Senha: ')
                    senha2 = input('Confirme a senha: ')
                    nome = input('Nome: ')
                    sobrenome = input('Sobrenome: ')
                    nascimento = input('Data de nascimento: ')
                    if senha1 == senha2:
                        if opc == 1:
                            if self.sistema.cadastrar_professor(
                                email, senha1, nome, sobrenome, nascimento
                            ):
                                print(
                                    f'Professor {self.sistema.usuario} cadastrado no sistema')
                            else:
                                print('Erro ao cadastrar professor')
                        elif opc == 2:
                            turma = input('Turma: ')
                            if self.sistema.cadastrar_aluno(
                                email, senha1, nome, sobrenome, nascimento, turma
                            ):
                                print(
                                    f'Aluno {self.sistema.usuario} cadastrado no sistema')
                            else:
                                print('Erro ao cadastrar aluno')
                if self.sistema.usuario:
                    if isinstance(self.sistema.usuario, Professor):
                        for num, turma in self.sistema.usuario.turmas.items():
                            print(f'{turma.id} - {turma.nome}')
                        print('0 - Sair')
                        opc = int(input())
                        while opc:
                            try:
                                if self.sistema.turmas[opc].atividades:
                                    self.sistema.turmas[opc].abrir(
                                        self.sistema)
                                    for num, turma in self.sistema.usuario.turmas.items():
                                        print(f'{turma.id} - {turma.nome}')
                                    print('0 - Sair')
                                else:
                                    print('Turma sem atividades')
                                opc = int(input())
                            except KeyError:
                                print('Opção inválida')
                                opc = int(input())
                    elif isinstance(self.sistema.usuario, Aluno):
                        for num, materia in self.sistema.materias.items():
                            print(f'{num} - {materia.nome}')
                        print('0 - Sair')
                        opc = int(input())
                        while opc:
                            try:
                                if self.sistema.materias[opc].atividades:
                                    self.sistema.materias[opc].abrir(
                                        self.sistema.usuario)
                                    for num, materia in self.sistema.materias.items():
                                        print(f'{num} - {materia.nome}')
                                    print('0 - Sair')
                                else:
                                    print('Matéria sem atividades')
                                opc = int(input())
                            except KeyError:
                                print('Opção inválida')
                                opc = int(input())
                print(
                    'Tela inicial\n'
                    '1 - Entrar\n'
                    '2 - Cadastrar\n'
                    '0 - Fechar'
                )
                opc = int(input())
            except KeyboardInterrupt:
                self.sistema.logout()
                self.sistema.fechar_bd()
                print('\nEncerrado')
                break


if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
    # teste = Teste()
    # teste.iniciar()
    # sistema = SistemaEducacional()
    # sistema.login('jorge@example.com', '1111')
    # sistema.submeter_atividade(32, 1, 2)

    # enviar = f'3'
    # for atividade in sistema.get_atividades_materia(2).values():
    #     enviar += f'|{atividade}'
    # atividades = enviar.split('|')
    # lista_atividades = []
    # for atividade in atividades[1:]:
    #     atividade_campos = atividade.split('//')[:6]
    #     lista_questoes = {}
    #     for questao in atividade.split('//')[6:]:
    #         questao_campos = questao.split(';;')
    #         lista_questoes.update(
    #             {questao_campos[0]: Questao(*questao_campos)})
    #     lista_atividades.append(Atividade(*atividade_campos, lista_questoes))
    # for atividade in lista_atividades:
    #     print(atividade.questoes)

    # enviar = f'5'
    # for atividade in sistema.get_atividades_turma(1).values():
    #     enviar += f'|{atividade}'
    # resposta = enviar.split('|')
    # lista_atividades = []
    # for atividade in resposta[1:]:
    #     atividade_campos = atividade.split('//')[:6]
    #     lista_questoes = {}
    #     for questao in atividade.split('//')[6:]:
    #         questao_campos = questao.split(';;')
    #         lista_questoes.update(
    #             {questao_campos[0]: Questao(*questao_campos)})
    #     lista_atividades.append(Atividade(*atividade_campos, lista_questoes))
    # for atividade in lista_atividades:
    #     print(atividade.questoes)

    # atividade_campos = enviar.split('//')[:6]
    # questoes_campos = enviar.split('//')[6:]
    # print(atividade_campos)
    # print(questoes_campos)

    # print(sistema.usuario.get_materias_id())

    # mensagem_str = '6|None|titulo|descricao|1|2|None//enuciado//1//2//3//4//5'.split(
    #     '|')
    # print(mensagem_str)
    # atividade_id = mensagem_str[1] if mensagem_str[1] != 'None' else None
    # titulo = mensagem_str[2] if mensagem_str[2] != 'None' else None
    # descricao = mensagem_str[3] if mensagem_str[3] != 'None' else None
    # materia = int(mensagem_str[4]) if mensagem_str[4] != 'None' else None
    # turma = int(mensagem_str[5]) if mensagem_str[5] != 'None' else None
    # nova = sistema.cadastrar_atividade(
    #     titulo, descricao, materia, turma, atividade_id)
    # if not nova:
    #     pass
    # else:
    #     try:
    #         for questao in mensagem_str[6:]:
    #             q = questao.split('//')
    #             if q[0] == 'None':
    #                 q[0] = None
    #             novaq = sistema.cadastrar_questao(
    #                 nova.id, q[1], 'a', q[2], q[3], q[4], q[5], q[6], id=q[0])
    #             print(novaq)
    #     except:
    #         pass

    # enviar = '2|'
    # for materia in sistema.materias.values():
    #     enviar += f'{materia.id}-{materia.nome},'
    # enviar += '0|'
    # print(enviar)

    # enviar = '1|'
    # for materia in sistema.usuario.materias:
    #     enviar += f"{materia[0]},"
    # enviar += '0|'
    # for turma in sistema.usuario.turmas.values():
    #     enviar += f'{turma.id}-{turma.nome},'
    # enviar += '0|'
    # print(enviar)

    # for materia in sistema.usuario.materias:
    #     print(materia)

    # for turma in sistema.get_turmas_professor().values():
    #     print(turma.nome)

    # for turma in sistema.turmas.values():
    #     print(turma.professores)

    # for num, materia in sistema.materias.items():
    #     print(f'{num} - {materia.nome}')
    #     for atividade in materia.atividades:
    #         print('\t', atividade)
    #     for questao in atividade.questoes:
    #         print('\t\t',questao)

    # for num, materia in sistema.materias.items():
    #     print(f'{num} - {materia.nome}')
    # print('0 - Sair')
    # opc = int(input())
    # while opc:
    #     try:
    #         if sistema.materias[opc].atividades:
    #             sistema.materias[opc].abrir()
    #             for num, materia in sistema.materias.items():
    #                 print(f'{num} - {materia.nome}')
    #             print('0 - Sair')
    #         else:
    #             print('Matéria sem atividades')
    #         opc = int(input())
    #     except KeyError:
    #         print('Opção inválida')
    #         opc = int(input())
