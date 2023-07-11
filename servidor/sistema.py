import socket
import threading
import mysql.connector as mysql
from modelos import Professor, Aluno, Materia, Turma, Atividade, Questao


tabelas = {}
tabelas['usuarios'] = (
    "CREATE TABLE IF NOT EXISTS sistema_educacional.usuarios ("
    "id INT AUTO_INCREMENT PRIMARY KEY,"
    "email VARCHAR(255) NOT NULL,"
    "senha VARCHAR(255) NOT NULL,"
    "nome VARCHAR(255) NOT NULL,"
    "sobrenome VARCHAR(255) NOT NULL,"
    "nascimento DATE NOT NULL,"
    "data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
    "ultimo_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,"
    "UNIQUE (email)"
    ")"
)
tabelas['turmas'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.turmas ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'num_sala INT NOT NULL,'
    'UNIQUE (nome),'
    'UNIQUE (num_sala)'
    ')'
)
tabelas['alunos'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.alunos ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'turma_id INT NOT NULL,'
    'pontuacao_geral INT NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id),'
    'FOREIGN KEY (turma_id) REFERENCES turmas(id)'
    ')'
)
tabelas['professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'salario DECIMAL(10,2) NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
tabelas['turmas_professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.turmas_professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'turma_id INT NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (turma_id) REFERENCES turmas(id),'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
tabelas['materias'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL'
    ')'
)
tabelas['materias_professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias_professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'materia_id INT NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (materia_id) REFERENCES materias(id),'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
tabelas['atividades'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.atividades ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao TEXT NULL,'
    'professor_id INT NOT NULL,'
    'turma_id INT NOT NULL,'
    'materia_id INT NOT NULL,'
    'FOREIGN KEY (professor_id) REFERENCES professores(id),'
    'FOREIGN KEY (turma_id) REFERENCES turmas(id)'
    ')'
)
tabelas['questoes'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.questoes ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'atividade_id INT NOT NULL,'
    'enunciado TEXT NOT NULL,'
    'resposta VARCHAR(255) NOT NULL,'
    'letra_a VARCHAR(255) NOT NULL,'
    'letra_b VARCHAR(255) NOT NULL,'
    'letra_c VARCHAR(255) NOT NULL,'
    'letra_d VARCHAR(255) NOT NULL,'
    'letra_e VARCHAR(255) NOT NULL,'
    'FOREIGN KEY (atividade_id) REFERENCES atividades(id)'
    ')'
)
tabelas['atividades_alunos'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.atividades_alunos ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'atividade_id INT NOT NULL,'
    'aluno_id INT NOT NULL,'
    'data_submissao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,'
    'pontuacao INT NOT NULL,'
    'taxa_acerto DECIMAL(10,2) NOT NULL,'
    'FOREIGN KEY (atividade_id) REFERENCES atividades(id),'
    'FOREIGN KEY (aluno_id) REFERENCES alunos(id)'
    ')'
)


class SistemaEducacional:
    def __init__(self):
        self._mydb = mysql.connect(
            host="localhost",
            user="root",
            password="1234",
            auth_plugin='mysql_native_password',
            consume_results=True
        )
        self._cursor = self._mydb.cursor()
        self._sql = "CREATE DATABASE IF NOT EXISTS sistema_educacional"
        self._val = ()
        self._cursor.execute(self._sql)
        for tabela in tabelas:
            self._cursor.execute(tabelas[tabela])
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
        self._sql = "SELECT * FROM sistema_educacional.materias"
        self._val = ()
        self._cursor.execute(self._sql, self._val)
        materias = {}
        for materia in self._cursor.fetchall():
            atividades = self.get_atividades_materia(materia[0])
            materias.update({materia[0]: Materia(*materia, atividades)})
        return materias

    def get_turmas(self):
        self._sql = "SELECT * FROM sistema_educacional.turmas"
        self._val = ()
        self._cursor.execute(self._sql, self._val)
        turmas = {}
        for turma in self._cursor.fetchall():
            atividades = self.get_atividades_turma(turma[0])
            alunos = self.get_alunos_turma(turma[0])
            professores = self.get_professores_turma(turma[0])
            turmas.update(
                {turma[0]: Turma(*turma, atividades, alunos, professores)})
        return turmas

    def get_alunos_turma(self, turma_id):
        self._sql = "SELECT sistema_educacional.alunos.id, sistema_educacional.usuarios.nome FROM sistema_educacional.alunos INNER JOIN sistema_educacional.usuarios ON sistema_educacional.alunos.usuario_id = sistema_educacional.usuarios.id WHERE sistema_educacional.alunos.turma_id = %s"
        self._val = (turma_id,)
        self._cursor.execute(self._sql, self._val)
        alunos = {}
        for aluno in self._cursor.fetchall():
            alunos.update({aluno[0]: aluno})
        return alunos

    def get_professores_turma(self, turma_id):
        self._sql = "SELECT sistema_educacional.professores.id, sistema_educacional.usuarios.nome FROM sistema_educacional.professores INNER JOIN sistema_educacional.usuarios ON sistema_educacional.professores.usuario_id = sistema_educacional.usuarios.id INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.professores.id = sistema_educacional.turmas_professores.professor_id WHERE sistema_educacional.turmas_professores.turma_id = %s"
        self._val = (turma_id,)
        self._cursor.execute(self._sql, self._val)
        professores = {}
        for professor in self._cursor.fetchall():
            professores.update({professor[0]: professor})
        return professores

    def get_atividade(self, id_atividade):
        self._sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.id = %s"
        self._val = (id_atividade,)
        self._cursor.execute(self._sql, self._val)
        atividade = self._cursor.fetchone()
        if atividade:
            questoes = self.get_questoes_atividade(atividade[0])
            return Atividade(*atividade, questoes)
        else:
            return None

    def get_questoes_atividade(self, id_atividade):
        self._sql = "SELECT * FROM sistema_educacional.questoes WHERE sistema_educacional.questoes.atividade_id = %s"
        self._val = (id_atividade,)
        self._cursor.execute(self._sql, self._val)
        questoes_atividade = {}
        for questao in self._cursor.fetchall():
            questoes_atividade.update({questao[0]: Questao(*questao)})
        return questoes_atividade

    def get_atividades_professor(self, professor_id):
        self._sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.professor_id = %s"
        self._val = (professor_id,)
        self._cursor.execute(self._sql, self._val)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def get_atividades_turma_professor(self, turma_id, professor_id):
        self._sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.turma_id = %s AND sistema_educacional.atividades.professor_id = %s"
        self._val = (turma_id, professor_id)
        self._cursor.execute(self._sql, self._val)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def get_turmas_professor(self, professor_id):
        self._sql = "SELECT sistema_educacional.turmas.id, sistema_educacional.turmas.nome, sistema_educacional.turmas.num_sala FROM sistema_educacional.turmas INNER JOIN sistema_educacional.turmas_professores WHERE sistema_educacional.turmas_professores.professor_id = %s AND sistema_educacional.turmas_professores.turma_id = sistema_educacional.turmas.id"
        self._val = (professor_id,)
        self._cursor.execute(self._sql, self._val)
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
        self._sql = "SELECT * FROM sistema_educacional.atividades WHERE materia_id = %s"
        self._val = (materia_id,)
        self._cursor.execute(self._sql, self._val)
        atividades_materia = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            atividades_materia.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return atividades_materia

    def get_atividades_turma(self, turma_id):
        self._sql = "SELECT * FROM sistema_educacional.atividades WHERE sistema_educacional.atividades.turma_id = %s"
        self._val = (turma_id,)
        self._cursor.execute(self._sql, self._val)
        lista_atividades = {}
        for atividade in self._cursor.fetchall():
            questoes = self.get_questoes_atividade(atividade[0])
            lista_atividades.update(
                {atividade[0]: Atividade(*atividade, questoes)})
        return lista_atividades

    def buscar(self, email):
        try:
            self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s"
            self._val = (email,)
            self._cursor.execute(self._sql, self._val)
            return self._cursor.fetchone()
        except:
            return False

    def cadastrar_professor(self, email, senha, nome, sobrenome, nascimento):
        if self.buscar(email):
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        self._val = (email, senha, nome, sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        self._sql = 'SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login FROM sistema_educacional.usuarios WHERE email = %s'
        self._val = (email,)
        self._cursor.execute(self._sql, self._val)
        id, data_cadastro, ultimo_login = self._cursor.fetchone()
        professor = Professor(id, email, senha, nome, sobrenome,
                              nascimento, data_cadastro, ultimo_login)
        self._usuario = professor

        self._sql = "INSERT INTO sistema_educacional.professores (usuario_id, salario) VALUES (%s, %s)"
        self._val = (professor.id, 1320)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        return True

    def cadastrar_aluno(self, email, senha, nome, sobrenome, nascimento, turma):
        if self.buscar(email):
            return False
        self._sql = "SELECT sistema_educacional.turmas.id FROM sistema_educacional.turmas WHERE sistema_educacional.turmas.nome = %s"
        self._val = (turma,)
        self._cursor.execute(self._sql, self._val)
        try:
            turma_id = self._cursor.fetchone()[0]
        except:
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        self._val = (email, senha, nome,
                     sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        self._sql = 'SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login FROM sistema_educacional.usuarios WHERE email = %s'
        self._val = (email,)
        self._cursor.execute(self._sql, self._val)
        id, data_cadastro, ultimo_login = self._cursor.fetchone()
        aluno = Aluno(id, email, senha, nome, sobrenome,
                      nascimento, data_cadastro, ultimo_login, turma)
        self._usuario = aluno

        self._sql = "INSERT INTO sistema_educacional.alunos (usuario_id, pontuacao_geral, turma_id) VALUES (%s, %s, %s)"
        self._val = (aluno.id, 0, turma_id)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        return True

    def login_professor(self, usuario):
        try:
            self._sql = "SELECT * FROM sistema_educacional.professores WHERE sistema_educacional.professores.usuario_id = %s"
            self._val = (usuario[0],)
            self._cursor.execute(self._sql, self._val)
            consulta = self._cursor.fetchone()
            if consulta:
                self._sql = "SELECT sistema_educacional.materias.id, sistema_educacional.materias.nome FROM sistema_educacional.materias INNER JOIN sistema_educacional.materias_professores ON sistema_educacional.materias_professores.materia_id = sistema_educacional.materias.id WHERE sistema_educacional.materias_professores.professor_id = %s"
                self._val = (consulta[0],)
                self._cursor.execute(self._sql, self._val)
                materias = self._cursor.fetchall()
                turmas = self.get_turmas_professor(consulta[0])
                atividades = self.get_atividades_professor(consulta[0])
                professor = Professor(
                    consulta[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5],
                    usuario[6], usuario[7], materias, turmas, atividades, consulta[2]
                )
                self._usuario = professor
                self._sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
                self._val = (usuario[0],)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                return True
            return False
        except Exception as e:
            print('Erro ao logar professor:', str(e))
            return False

    def login_aluno(self, usuario):
        try:
            self._sql = "SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.email, sistema_educacional.usuarios.senha, sistema_educacional.usuarios.nome, sistema_educacional.usuarios.sobrenome, sistema_educacional.usuarios.nascimento, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login, sistema_educacional.alunos.pontuacao_geral FROM sistema_educacional.usuarios INNER JOIN sistema_educacional.alunos ON sistema_educacional.usuarios.id = sistema_educacional.alunos.usuario_id WHERE usuario_id = %s"
            self._val = (usuario[0],)
            self._cursor.execute(self._sql, self._val)
            consulta = self._cursor.fetchone()
            if consulta:
                aluno = Aluno(
                    usuario[0], usuario[1], usuario[2], usuario[3], usuario[4],
                    usuario[5], usuario[6], usuario[7], consulta[8]
                )
                self._usuario = aluno
                self._sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
                self._val = (usuario[0],)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                return True
            return False
        except Exception as e:
            print('Erro ao logar aluno:', str(e))
            return False

    def autenticar(self, email, senha):
        try:
            self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s AND senha = %s"
            self._val = (email, senha)
            self._cursor.execute(self._sql, self._val)
            return self._cursor.fetchone()
        except:
            return False

    def login(self, email, senha):
        usuario = self.autenticar(email, senha)
        if usuario:
            if not self.login_professor(usuario):
                self.login_aluno(usuario)
            return True
        else:
            return False

    def cadastrar_atividade(self, nome, descricao, materia, turma, id=None):
        retorno = None
        try:
            if id:
                self._sql = "UPDATE sistema_educacional.atividades SET nome = %s, descricao = %s, materia_id = %s, turma_id = %s WHERE id = %s"
                self._val = (nome, descricao, materia, turma, id)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = Atividade(id, nome, descricao,
                                    self.usuario.id, turma, materia)
            else:
                self._sql = "INSERT INTO sistema_educacional.atividades (nome, descricao, professor_id, turma_id, materia_id) VALUES (%s, %s, %s, %s, %s)"
                self._val = (nome, descricao, self.usuario.id, turma, materia)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = Atividade(
                    self._cursor.lastrowid, nome, descricao, self.usuario.id, turma, materia)
        except Exception as e:
            print('Erro ao cadastrar atividade:', str(e))
        return retorno

    def cadastrar_questao(self, atividade, enunciado, resposta, a, b, c, d, e, id=None):
        retorno = None
        try:
            if id:
                self._sql = "UPDATE sistema_educacional.questoes SET enunciado = %s, resposta = %s, letra_a = %s, letra_b = %s, letra_c = %s, letra_d = %s, letra_e = %s WHERE id = %s"
                self._val = (enunciado, resposta, a, b, c, d, e, id)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = Questao(id, atividade, enunciado,
                                  resposta, a, b, c, d, e)
            else:
                self._sql = "INSERT INTO sistema_educacional.questoes (atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                self._val = (atividade, enunciado, resposta, a, b, c, d, e)
                print(atividade, enunciado, resposta, a, b, c, d, e)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = Questao(self._cursor.lastrowid,
                                  atividade, enunciado, resposta, a, b, c, d, e)
        except Exception as e:
            print('Erro ao cadastrar questão:', str(e))
        return retorno

    def logout(self):
        self._usuario = None

    def fechar_bd(self):
        self._mydb.close()


class MyThread(threading.Thread):
    def __init__(self, client_address, serv_socket, client_socket):
        threading.Thread.__init__(self)
        self.name = None
        self.sistema = SistemaEducacional()
        self.client_address = client_address
        self.client_socket = client_socket
        self.serv_socket = serv_socket
        print(f'Nova conexão, endereço: {self.client_address}')

    def run(self):
        while True:
            try:
                mensagem = self.client_socket.recv(4096)
                mensagem_str = mensagem.decode().split('|')
                enviar = ''

                if mensagem_str[0] == '1':
                    login = mensagem_str[1].split(',')
                    email = login[0]
                    senha = login[1]
                    if self.sistema.login(email, senha):
                        if isinstance(self.sistema.usuario, Professor):
                            enviar = '1|'
                            for materia in self.sistema.usuario.materias:
                                enviar += f"{materia[0]},"
                            enviar += '0'
                            for turma in self.sistema.usuario.turmas.values():
                                enviar += f'{turma.id}-{turma.nome},'
                            print(
                                f'Professor {self.sistema.usuario} logou em {self.client_address}')
                        elif isinstance(self.sistema.usuario, Aluno):
                            enviar = '2|'
                            for materia in self.sistema.materias.values():
                                enviar += f'{materia.id}-{materia.nome},'
                            print(
                                f'Aluno {self.sistema.usuario} logou em {self.client_address}')
                        enviar += f'0|{self.sistema.usuario.id}'
                    else:
                        enviar = '0'
                        print(f'Erro no login em {self.client_address}')
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '2':
                    cadastrar = mensagem_str[1:].split(',')
                    email = cadastrar[0]
                    senha = cadastrar[1]
                    nome = cadastrar[2]
                    sobrenome = cadastrar[3]
                    nascimento = cadastrar[4]
                    if cadastrar[-1] == 'a':
                        turma = cadastrar[5]
                        if self.sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento, turma):
                            enviar = '2'
                            print(
                                f'Aluno {self.sistema.usuario} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastrar aluno no sistema em {self.client_address}')
                    elif cadastrar[-1] == 'p':
                        if self.sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                            enviar = '2'
                            print(
                                f'Professor {self.sistema.usuario} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastrar professor no sistema em {self.client_address}')
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '3':
                    materia_id = mensagem_str[1]
                    enviar = f'3'
                    for atividade in self.sistema.get_atividades_materia(materia_id).values():
                        enviar += f'|{atividade.id}-{atividade.titulo}-{atividade.turma_id}'
                    self.client_socket.send(enviar.encode())
                elif mensagem_str[0] == '4':
                    for questao in self.sistema.get_questoes_atividade(mensagem_str[1]).values():
                        enviar = f'4|{questao}'
                        self.client_socket.send(enviar.encode())
                        self.client_socket.recv(1024)
                    atividade = self.sistema.get_atividade(mensagem_str[1])
                    self.client_socket.send(f'0|{atividade}'.encode())
                elif mensagem_str[0] == '5':
                    turma = mensagem_str[1]
                    enviar = f'5'
                    for atividade in self.sistema.get_atividades_turma(turma):
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
                    id = self.sistema.cadastrar_atividade(
                        titulo, descricao, materia, turma, atividade_id)
                    if not id:
                        self.client_socket.send('-6'.encode())
                        print(
                            f'Erro ao cadastrar atividade em {self.client_address}')
                        continue
                    else:
                        try:
                            lista_questoes = [num.split('/')
                                              for num in mensagem_str[6:]]
                            for questao in lista_questoes:
                                questao[0] = int(
                                    questao[0]) if questao[0] != 'None' else None
                                self.sistema.cadastrar_questao(questao[0],
                                                               id, questao[1], 'a', questao[2], questao[3], questao[4], questao[5], questao[6])
                            print(
                                f'Atividade {titulo} cadastrada em {self.client_address}')
                            self.client_socket.send('6'.encode())
                        except:
                            self.client_socket.send('-6'.encode())
                            print(
                                f'Erro ao cadastrar atividade em {self.client_address}')
                            continue
                elif mensagem_str[0] == '0':
                    print(
                        f'Usuário {self.sistema.usuario} deslogou em {self.client_address}')
                    self.sistema.logout()
                elif mensagem_str[0] == '-1':
                    print(f'Conexão com {self.client_address} finalizada')
                    self.client_socket.close()
                    self.sistema.fechar_bd()
                else:
                    raise Exception(
                        f'Conexão com {self.client_address} finalizada inesperadamente')
            except Exception as e:
                print(str(e))
                self.client_socket.close()
                self.sistema.fechar_bd()
                break


class Servidor:
    def __init__(self):
        self.host = 'LOCALHOST'
        self.port = 5000
        self.addr = (self.host, self.port)
        self.serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serv_socket.bind(self.addr)
        self.serv_socket.listen(10)
        print('Aguardando conexão...')

    def iniciar(self):
        while True:
            try:
                client_socket, client_address = self.serv_socket.accept()
                my_thread = MyThread(
                    client_address, self.serv_socket, client_socket)
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
    def __init__(self):
        self.sistema = SistemaEducacional()

    def iniciar(self):
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
                                f'Professor {self.sistema.usuario.nome} logado no sistema')
                        elif isinstance(self.sistema.usuario, Aluno):
                            print(
                                f'Aluno {self.sistema.usuario} logado no sistema')
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
    # sistema.login('jose@example.com', '1111')
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
