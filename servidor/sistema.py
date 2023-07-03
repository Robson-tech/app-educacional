import mysql.connector as mysql
from modelos import Professor, Aluno, Questao


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
            auth_plugin='mysql_native_password'
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
        self._sql = "SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.email, sistema_educacional.usuarios.senha, sistema_educacional.usuarios.nome, sistema_educacional.usuarios.sobrenome, sistema_educacional.usuarios.nascimento, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login, sistema_educacional.professores.salario FROM sistema_educacional.usuarios INNER JOIN sistema_educacional.professores ON sistema_educacional.usuarios.id = sistema_educacional.professores.usuario_id WHERE usuario_id = %s"
        self._val = (usuario[0],)
        self._cursor.execute(self._sql, self._val)
        consulta = self._cursor.fetchone()
        if consulta:
            professor = Professor(
                consulta[0], usuario[1], usuario[2], usuario[3], usuario[4],
                usuario[5], usuario[6], usuario[7], consulta[8]
            )
            self._usuario = professor
            for turma in sistema.get_turmas_professor():
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
            self._sql = "SELECT sistema_educacional.turmas.nome FROM sistema_educacional.turmas INNER JOIN sistema_educacional.turmas_professores INNER JOIN sistema_educacional.professores ON sistema_educacional.turmas.id = sistema_educacional.turmas_professores.turma_id AND sistema_educacional.turmas_professores.professor_id = sistema_educacional.professores.id WHERE sistema_educacional.professores.usuario_id = %s"
            self._val = (self.usuario.id,)
            self._cursor.execute(self._sql, self._val)
            return [x[0] for x in self._cursor.fetchall()]

    def get_atividades_materia(self, materia):
        self._sql = "SELECT sistema_educacional.atividades.id, sistema_educacional.atividades.nome, sistema_educacional.atividades.turma_id FROM sistema_educacional.atividades INNER JOIN sistema_educacional.materias ON sistema_educacional.atividades.materia_id = sistema_educacional.materias.id WHERE sistema_educacional.materias.nome = %s"
        self._val = (materia,)
        self._cursor.execute(self._sql, self._val)
        return self._cursor.fetchall()

    def get_atividades_turma(self, turma):
        self._sql = "SELECT sistema_educacional.atividades.id, sistema_educacional.atividades.nome, sistema_educacional.atividades.turma_id, sistema_educacional.atividades.materia_id FROM sistema_educacional.atividades INNER JOIN sistema_educacional.turmas INNER JOIN sistema_educacional.materias ON sistema_educacional.atividades.turma_id = sistema_educacional.turmas.id AND sistema_educacional.atividades.materia_id = sistema_educacional.materias.id WHERE sistema_educacional.turmas.nome = %s"
        self._val = (turma,)
        self._cursor.execute(self._sql, self._val)
        return self._cursor.fetchall()

    def get_questoes(self, id_atividade):
        self._sql = "SELECT sistema_educacional.questoes.id, sistema_educacional.questoes.atividade_id, sistema_educacional.questoes.resposta, sistema_educacional.questoes.letra_a, sistema_educacional.questoes.letra_b, sistema_educacional.questoes.letra_c, sistema_educacional.questoes.letra_d, sistema_educacional.questoes.letra_e, sistema_educacional.questoes.enunciado FROM sistema_educacional.questoes WHERE sistema_educacional.questoes.atividade_id = %s"
        self._val = (id_atividade,)
        self._cursor.execute(self._sql, self._val)
        questoes = []
        for questao in self._cursor.fetchall():
            questoes.append(Questao(*questao))
        return questoes

    def cadastrar_atividade(self, nome, descricao, materia, turma):
        self._sql = "INSERT INTO sistema_educacional.atividades (nome, descricao, materia_id, turma_id) VALUES (%s, %s, %s, %s)"
        self._val = (nome, descricao, materia, turma)
        try:
            self._cursor.execute(self._sql, self._val)
        except:
            return False
        self._mydb.commit()
        return self._cursor.lastrowid

    def cadastrar_questao(self, atividade, enunciado, resposta, a, b, c, d, e):
        pass

    def logout(self):
        self._usuario = None

    def fechar_bd(self):
        self._mydb.close()


def main():
    host = 'localhost'
    port = 5000
    addr = (host, port)
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen(10)
    print('Aguardando conexão...')
    con, cliente = serv_socket.accept()
    enviar = '1'
    for materia in sistema.materias:
        enviar += f'|{materia}'
    con.send(enviar.encode())
    print('Conectado')
    print('Aguardando interação...')

    while True:
        try:
            mensagem = con.recv(4096)
            mensagem_str = mensagem.decode().split('|')
            enviar = ''
            # print(mensagem_str)

            if mensagem_str[0] == '1':
                email = mensagem_str[1]
                senha = mensagem_str[2]
                if sistema.login(email, senha):
                    if isinstance(sistema.usuario, Professor):
                        enviar = '1'
                        for turma in sistema.usuario.turmas:

                            enviar += f'|{turma}'
                        print(f'Professor {sistema.usuario} logou')
                    else:
                        enviar = '2'
                        print(f'Aluno {sistema.usuario} logou')
                else:
                    enviar = '0'
                    print('Erro no login')
            elif mensagem_str[0] == '2':
                email = mensagem_str[1]
                senha = mensagem_str[2]
                nome = mensagem_str[3]
                sobrenome = mensagem_str[4]
                nascimento = mensagem_str[5]
                if mensagem_str[-1] == 'a':
                    turma = mensagem_str[6]
                    if sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento, turma):
                        enviar = '2'
                        print(f'Aluno {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar aluno no sistema')
                else:
                    if sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                        enviar = '2'
                        print(
                            f'Professor {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar professor no sistema')
            elif mensagem_str[0] == '3':
                materia = mensagem_str[1]
                enviar = f'3'
                for atividade in sistema.get_atividades_materia(materia):
                    enviar += f'|{atividade[0]}-{atividade[1]}-{atividade[2]}'
            elif mensagem_str[0] == '4':
                for questao in sistema.get_questoes(mensagem_str[1]):
                    enviar = f'4|{questao}'
                    con.send(enviar.encode())
                    con.recv(1024)
                con.send('0'.encode())
                continue
            elif mensagem_str[0] == '5':
                turma = mensagem_str[1]
                enviar = f'5'
                for atividade in sistema.get_atividades_turma(turma):
                    enviar += f'|{atividade[0]}-{atividade[1]}-{atividade[2]}-{atividade[3]}'
                print(f'Atividades da turma {turma} enviadas')
            elif mensagem_str[0] == '6':
                titulo = mensagem_str[1]
                descricao = mensagem_str[2]
                materia = mensagem_str[3]
                turma = mensagem_str[4]
                id = sistema.cadastrar_atividade(
                    titulo, descricao, materia, turma)
                lista_questoes = [num.split('/') for num in mensagem_str[5:]]
                for questao in lista_questoes:
                    sistema.cadastrar_questao(
                        id, questao[1], 'a', questao[2], questao[3], questao[4], questao[5], questao[6])
                enviar = '6'
                print(f'Atividade {titulo} cadastrada')
            elif mensagem_str[0] == '0':
                print(f'Usuário {sistema.usuario} deslogou')
                sistema.logout()
            elif mensagem_str[0] == '-1':
                print('Conexão finalizada pelo cliente')
                con.close()
                serv_socket.close()
                return False
            else:
                raise Exception(
                    'Conexão finalizada inesperadamente pelo cliente')

            con.send(enviar.encode())
        except Exception as e:
            print(str(e))
            con.close()
            serv_socket.close()
            break

    return True


if __name__ == "__main__":
    import socket

    sistema = SistemaEducacional()
    while main():
        pass
    # sistema.login('julio@example.com', '1234')
    # print(sistema.get_atividades_turma('1A'))
    # print(sistema.cadastrar_atividade('Atividade 2', 'Atividade 2', 1, 1))
    # print(sistema.get_atividades_turma('1A'))
    sistema.fechar_bd()
