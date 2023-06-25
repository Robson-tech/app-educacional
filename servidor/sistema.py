import mysql.connector as mysql
from modelos import Professor, Aluno


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
    'FOREIGN KEY (materia_id) REFERENCES materias(id)'
    ')'
)
tabelas['questoes'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.questoes ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'enunciado VARCHAR(255) NOT NULL,'
    'resposta VARCHAR(255) NOT NULL,'
    'atividade_id INT NOT NULL,'
    'FOREIGN KEY (atividade_id) REFERENCES atividades(id)'
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
        return [x for x in self._cursor.fetchall()]

    @property
    def turmas(self):
        if isinstance(self._usuario, Professor):
            turmas = {}
            self._sql = "SELECT sistema_educacional.usuarios.nome, sistema_educacional.alunos.turma FROM sistema_educacional.usuarios INNER JOIN sistema_educacional.alunos ON sistema_educacional.usuarios.id = sistema_educacional.alunos.usuario_id"
            self._val = ()
            self._cursor.execute(self._sql, self._val)
            for turma in self._cursor.fetchall():
                if turma[1] not in turmas.keys():
                    turmas[turma[1]] = []
                turmas[turma[1]].append(turma[0])
            return turmas
        else:
            return None

    def cadastrar_professor(self, email, senha, nome, sobrenome, nascimento):
        if self.buscar(email):
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        self._val = (email, senha, nome, sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        professor = Professor(email, senha, nome, sobrenome, nascimento)
        professor.id = self._cursor.lastrowid
        self._usuario = professor

        self._sql = "INSERT INTO sistema_educacional.professores (usuario_id, salario) VALUES (%s, %s)"
        self._val = (professor.id, 1320)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        return True

    def cadastrar_aluno(self, email, senha, nome, sobrenome, nascimento, turma):
        if self.buscar(email):
            return False
        self._sql = "INSERT INTO sistema_educacional.usuarios (email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login) VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        self._val = (email, senha, nome,
                     sobrenome, nascimento)
        self._cursor.execute(self._sql, self._val)
        self._mydb.commit()
        aluno = Aluno(email, senha, nome, sobrenome, nascimento)
        aluno.id = self._cursor.lastrowid
        self._usuario = aluno

        self._sql = "INSERT INTO sistema_educacional.alunos (usuario_id, pontuacao_geral, turma_id) VALUES (%s, %s, %s)"
        self._val = (aluno.id, 0)
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

    def login(self, email, senha):
        usuario = self.autenticar(email, senha)
        if usuario:
            self._sql = "SELECT sistema_educacional.usuarios.id, sistema_educacional.usuarios.email, sistema_educacional.usuarios.senha, sistema_educacional.usuarios.nome, sistema_educacional.usuarios.sobrenome, sistema_educacional.usuarios.nascimento, sistema_educacional.usuarios.data_cadastro, sistema_educacional.usuarios.ultimo_login, sistema_educacional.professores.salario FROM sistema_educacional.usuarios INNER JOIN sistema_educacional.professores ON sistema_educacional.usuarios.id = sistema_educacional.professores.usuario_id WHERE usuario_id = %s"
            self._val = (usuario[0],)
            self._cursor.execute(self._sql, self._val)
            consulta = self._cursor.fetchone()
            if consulta:
                professor = Professor(
                    consulta[0], usuario[1], usuario[2], usuario[3], usuario[4],
                    usuario[5], usuario[6], usuario[7], consulta[8]
                )
                self._sql = "SELECT sistema_educacional.turmas.nome, sistema_educacional.turmas.num_sala FROM sistema_educacional.turmas INNER JOIN sistema_educacional.turmas_professores ON sistema_educacional.turmas.id = sistema_educacional.turmas_professores.turma_id WHERE professor_id = %s"
                self._val = (professor.id,)
                self._cursor.execute(self._sql, self._val)
                for turma in self._cursor.fetchall():
                    professor.add_turma(turma)
                self._usuario = professor
                self._sql = 'UPDATE sistema_educacional.usuarios SET ultimo_login = CURRENT_TIMESTAMP WHERE id = %s'
                self._val = (usuario[0],)
                self._cursor.execute(self._sql, self._val)
                self._mydb.commit()
                return True
            else:
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
                else:
                    return False
        else:
            return False

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
        enviar += f',{materia}'
    con.send(enviar.encode())
    print('Conectado')
    print('Aguardando interação...')

    while True:
        enviar = ''
        try:
            mensagem = con.recv(1024)
            mensagem_str = mensagem.decode().split(',')

            if mensagem_str[0] == '1':
                email = mensagem_str[1]
                senha = mensagem_str[2]
                if sistema.login(email, senha):
                    if isinstance(sistema.usuario, Professor):
                        enviar = '1'
                        print(f'Professor {sistema.usuario} logou')
                    else:
                        enviar = '2'
                        print(f'Aluno {sistema.usuario} logou')
                else:
                    enviar = '0'
                    print('Erro no login')
                con.send(enviar.encode())
            elif mensagem_str[0] == '2':
                email = mensagem_str[1]
                senha = mensagem_str[2]
                nome = mensagem_str[3]
                sobrenome = mensagem_str[4]
                nascimento = mensagem_str[5]
                if mensagem_str[-1] == 'a':
                    if sistema.cadastrar_aluno(email, senha, nome, sobrenome, nascimento):
                        enviar = '1'
                        print(f'Aluno {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar aluno no sistema')
                else:
                    if sistema.cadastrar_professor(email, senha, nome, sobrenome, nascimento):
                        enviar = '1'
                        print(
                            f'Professor {sistema.usuario} cadastrado no sistema')
                    else:
                        enviar = '0'
                        print('Erro ao cadastrar professor no sistema')
                con.send(enviar.encode())
            elif mensagem_str[0] == '0':
                print(f'Usuário {sistema.usuario} deslogou')
                sistema.logout()
            else:
                raise Exception('Conexão finalizada pelo cliente')
        except Exception as e:
            print(str(e))
            con.close()
            serv_socket.close()
            break


if __name__ == "__main__":
    import socket

    sistema = SistemaEducacional()
    sistema.login('jose@example.com', '1234')
    print(sistema.usuario.turmas)
    # main()
    sistema.fechar_bd()
