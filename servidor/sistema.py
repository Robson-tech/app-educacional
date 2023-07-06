import socket
import threading
import mysql.connector as mysql
from modelos import Professor, Aluno, Atividade, Questao


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
    'nome VARCHAR(255) NOT NULL,'
    'professores_id INT NOT NULL,'
    'FOREIGN KEY (professores_id) REFERENCES professores(id)'
    ')'
)
tabelas['atividades'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.atividades ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'descricao VARCHAR(255) NOT NULL,'
    'materia_id INT NOT NULL,'
    'turma_id INT NOT NULL,'
    'FOREIGN KEY (materia_id) REFERENCES materias(id)'
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
        self._usuario = None
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

    @property
    def usuario(self):
        return self._usuario

    @property
    def materias(self):
        self._sql = "SELECT sistema_educacional.materias.nome FROM sistema_educacional.materias"
        self._val = ()
        self._cursor.execute(self._sql, self._val)
        return [x[0] for x in self._cursor.fetchall()]

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

    def buscar(self, email):
        self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s"
        self._val = (email,)
        self._cursor.execute(self._sql, self._val)
        try:
            return self._cursor.fetchone()
        except:
            return False

    def autenticar(self, email, senha):
        self._sql = "SELECT * FROM sistema_educacional.usuarios WHERE email = %s AND senha = %s"
        self._val = (email, senha)
        self._cursor.execute(self._sql, self._val)
        try:
            return self._cursor.fetchone()
        except:
            return False

    def login_professor(self, usuario):
        self._sql = "SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.email, sistema_educacional.usuarios.senha, sistema_educacional.usuarios.nome, sistema_educacional.usuarios.sobrenome, sistema_educacional.usuarios.nascimento, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login, sistema_educacional.materias.nome, sistema_educacional.materias.id, sistema_educacional.professores.salario FROM sistema_educacional.usuarios INNER JOIN sistema_educacional.professores ON sistema_educacional.usuarios.id = sistema_educacional.professores.usuario_id INNER JOIN sistema_educacional.materias ON sistema_educacional.professores.id = sistema_educacional.materias.professores_id WHERE usuario_id = %s"
        self._val = (usuario[0],)
        self._cursor.execute(self._sql, self._val)
        consulta = self._cursor.fetchone()
        if consulta:
            professor = Professor(
                consulta[0], consulta[1], consulta[2], consulta[3], consulta[4],
                consulta[5], consulta[6], consulta[7], consulta[8], consulta[9], salario=consulta[10]
            )
            self._usuario = professor
            for turma in self.get_turmas_professor():
                professor.add_turma(turma)
            self._sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
            self._val = (usuario[0],)
            self._cursor.execute(self._sql, self._val)
            self._mydb.commit()
            return True
        return False

    def login_aluno(self, usuario):
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

    def login(self, email, senha):
        usuario = self.autenticar(email, senha)
        if usuario:
            if not self.login_professor(usuario):
                self.login_aluno(usuario)
            return True
        else:
            return False

    def get_turmas_professor(self):
        if isinstance(self.usuario, Professor):
            self._sql = "SELECT sistema_educacional.turmas.nome, sistema_educacional.turmas.id FROM sistema_educacional.turmas INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.turmas.id = sistema_educacional.turmas_professores.turma_id INNER JOIN sistema_educacional.professores ON sistema_educacional.turmas_professores.professor_id = sistema_educacional.professores.id WHERE sistema_educacional.professores.usuario_id = %s"
            self._val = (self.usuario.id,)
            self._cursor.execute(self._sql, self._val)
            return [[turma[0], turma[1]] for turma in self._cursor.fetchall()]

    def get_atividades_materia(self, materia):
        self._sql = "SELECT sistema_educacional.atividades.id, sistema_educacional.atividades.nome, sistema_educacional.atividades.turma_id FROM sistema_educacional.atividades INNER JOIN sistema_educacional.materias ON sistema_educacional.atividades.materia_id = sistema_educacional.materias.id WHERE sistema_educacional.materias.nome = %s"
        self._val = (materia,)
        self._cursor.execute(self._sql, self._val)
        return self._cursor.fetchall()

    def get_atividades_turma(self, turma):
        if isinstance(self.usuario, Professor):
            self._sql = "SELECT sistema_educacional.atividades.id, sistema_educacional.atividades.nome, sistema_educacional.atividades.descricao, sistema_educacional.atividades.materia_id, sistema_educacional.atividades.turma_id, sistema_educacional.turmas_professores.professor_id FROM sistema_educacional.atividades INNER JOIN sistema_educacional.turmas INNER JOIN sistema_educacional.materias INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.atividades.turma_id = sistema_educacional.turmas.id AND sistema_educacional.atividades.materia_id = sistema_educacional.materias.id AND sistema_educacional.turmas.id = sistema_educacional.turmas_professores.turma_id WHERE sistema_educacional.turmas.nome = %s AND sistema_educacional.turmas_professores.professor_id = %s"
            self._val = (turma, self.usuario.id)
            self._cursor.execute(self._sql, self._val)
            lista_atividades = []
            for atividade in self._cursor.fetchall():
                lista_atividades.append(Atividade(*atividade))
            return lista_atividades

    def cadastrar_atividade(self, nome, descricao, materia, turma, id):
        retorno = False
        if id:
            self._sql = "UPDATE sistema_educacional.atividades SET nome = %s, descricao = %s, materia_id = %s, turma_id = %s WHERE id = %s"
            self._val = (nome, descricao, materia, turma, id)
            try:
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = id
            except Exception as e:
                print(str(e))
                retorno = False
        else:
            self._sql = "INSERT INTO sistema_educacional.atividades (nome, descricao, materia_id, turma_id) VALUES (%s, %s, %s, %s)"
            self._val = (nome, descricao, materia, turma)
            try:
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                retorno = self._cursor.lastrowid
            except Exception as e:
                print(str(e))
                retorno = False
        return retorno
    
    def get_atividade(self, id_atividade):
        self._sql = "SELECT sistema_educacional.atividades.id, sistema_educacional.atividades.nome, sistema_educacional.atividades.descricao, sistema_educacional.atividades.materia_id, sistema_educacional.atividades.turma_id, sistema_educacional.turmas_professores.professor_id FROM sistema_educacional.atividades INNER JOIN sistema_educacional.turmas INNER JOIN sistema_educacional.materias INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.atividades.turma_id = sistema_educacional.turmas.id AND sistema_educacional.atividades.materia_id = sistema_educacional.materias.id AND sistema_educacional.turmas.id = sistema_educacional.turmas_professores.turma_id WHERE sistema_educacional.atividades.id = %s"
        self._val = (id_atividade,)
        self._cursor.execute(self._sql, self._val)
        atividade = self._cursor.fetchone()
        return Atividade(*atividade)

    def cadastrar_questao(self, id, atividade, enunciado, resposta, a, b, c, d, e):
        if id:
            self._sql = "UPDATE sistema_educacional.questoes SET atividade_id = %s, enunciado = %s, resposta = %s, letra_a = %s, letra_b = %s, letra_c = %s, letra_d = %s, letra_e = %s WHERE id = %s"
            self._val = (atividade, enunciado, resposta, a, b, c, d, e, id)
            try:
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                return
            except Exception as e:
                print(str(e))
        self._sql = "INSERT INTO sistema_educacional.questoes (atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        self._val = (atividade, enunciado, resposta, a, b, c, d, e)
        try:
            self._cursor.execute(self._sql, self._val)
            self._mydb.commit()
        except Exception as e:
            print(str(e))

    def get_questoes(self, id_atividade):
        self._sql = "SELECT sistema_educacional.questoes.id, sistema_educacional.questoes.atividade_id, sistema_educacional.questoes.enunciado, sistema_educacional.questoes.resposta, sistema_educacional.questoes.letra_a, sistema_educacional.questoes.letra_b, sistema_educacional.questoes.letra_c, sistema_educacional.questoes.letra_d, sistema_educacional.questoes.letra_e FROM sistema_educacional.questoes WHERE sistema_educacional.questoes.atividade_id = %s"
        self._val = (id_atividade,)
        self._cursor.execute(self._sql, self._val)
        questoes = []
        for questao in self._cursor.fetchall():
            questoes.append(Questao(*questao))
        return questoes

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
        enviar = '1'
        for materia in self.sistema.materias:
            enviar += f'|{materia}'
        self.client_socket.send(enviar.encode())
        while True:
            try:
                mensagem = self.client_socket.recv(4096)
                mensagem_str = mensagem.decode().split('|')
                enviar = ''

                if mensagem_str[0] == '1':
                    email = mensagem_str[1]
                    senha = mensagem_str[2]
                    if self.sistema.login(email, senha):
                        if isinstance(self.sistema.usuario, Professor):
                            enviar = f"1|{self.sistema.usuario.materia['id']}"
                            for turma in self.sistema.usuario.turmas:
                                enviar += f'|{turma[0]}-{turma[1]}'
                            print(
                                f'Professor {self.sistema.usuario} logou em {self.client_address}')
                        else:
                            enviar = '2'
                            print(
                                f'Aluno {self.sistema.usuario} logou em {self.client_address}')
                    else:
                        enviar = '0'
                        print(f'Erro no login em {self.client_address}')
                elif mensagem_str[0] == '2':
                    email = mensagem_str[1]
                    senha = mensagem_str[2]
                    nome = mensagem_str[3]
                    sobrenome = mensagem_str[4]
                    nascimento = mensagem_str[5]
                    if mensagem_str[-1] == 'a':
                        turma = mensagem_str[6]
                        if self.sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento, turma):
                            enviar = '2'
                            print(
                                f'Aluno {self.sistema.usuario} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastrar aluno no sistema em {self.client_address}')
                    else:
                        if self.sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                            enviar = '2'
                            print(
                                f'Professor {self.sistema.usuario} cadastrado no sistema em {self.client_address}')
                        else:
                            enviar = '0'
                            print(
                                f'Erro ao cadastrar professor no sistema em {self.client_address}')
                elif mensagem_str[0] == '3':
                    materia = mensagem_str[1]
                    enviar = f'3'
                    for atividade in self.sistema.get_atividades_materia(materia):
                        enviar += f'|{atividade[0]}-{atividade[1]}-{atividade[2]}'
                elif mensagem_str[0] == '4':
                    for questao in self.sistema.get_questoes(mensagem_str[1]):
                        enviar = f'4|{questao}'
                        self.client_socket.send(enviar.encode())
                        self.client_socket.recv(1024)
                    atividade = self.sistema.get_atividade(mensagem_str[1])
                    self.client_socket.send(f'0|{atividade}'.encode())
                    continue
                elif mensagem_str[0] == '5':
                    turma = mensagem_str[1]
                    enviar = f'5'
                    for atividade in self.sistema.get_atividades_turma(turma):
                        enviar += f'|{atividade}'
                elif mensagem_str[0] == '6':
                    atividade_id = mensagem_str[1] if mensagem_str[1] != '-1' else None
                    titulo = mensagem_str[2]
                    descricao = mensagem_str[3]
                    materia = mensagem_str[4]
                    turma = mensagem_str[5]
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
                        except:
                            self.client_socket.send('-6'.encode())
                            print(
                                f'Erro ao cadastrar atividade em {self.client_address}')
                            continue
                        for questao in lista_questoes:
                            self.sistema.cadastrar_questao(questao[0],
                                id, questao[1], 'a', questao[2], questao[3], questao[4], questao[5], questao[6])
                        enviar = '6'
                        print(
                            f'Atividade {titulo} cadastrada em {self.client_address}')
                elif mensagem_str[0] == '0':
                    print(
                        f'Usuário {self.sistema.usuario} deslogou em {self.client_address}')
                    self.sistema.logout()
                elif mensagem_str[0] == '-1':
                    print(f'Conexão com {self.client_address} finalizada')
                    self.client_socket.close()
                    return False
                else:
                    raise Exception(
                        f'Conexão com {self.client_address} finalizada inesperadamente')

                self.client_socket.send(enviar.encode())
            except Exception as e:
                print(str(e))
                self.client_socket.close()
                self.sistema.fechar_bd()
                break


def main():
    host = '10.180.41.189'
    port = 5000
    addr = (host, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    print('Aguardando conexão...')
    while True:
        try:
            client_socket, client_address = serv_socket.accept()
            my_thread = MyThread(client_address, serv_socket, client_socket)
            my_thread.start()
        except KeyboardInterrupt:
            print('Servidor encerrado')
            serv_socket.close()
            break
        except Exception as e:
            print(str(e))
            serv_socket.close()
            break


if __name__ == "__main__":
    main()
    # sistema = SistemaEducacional()
    # sistema.login('julio@example.com', '1234')
    # for atividade in sistema.get_atividades_turma('3A'):
    #     print(atividade)
