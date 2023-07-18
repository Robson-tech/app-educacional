IP_SERVIDOR = 'LOCALHOST'
PORTA_SERVIDOR = 5000

TABELAS_SISTEMA_EDUCACIONAL = {}
TABELAS_SISTEMA_EDUCACIONAL['usuarios'] = (
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
TABELAS_SISTEMA_EDUCACIONAL['turmas'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.turmas ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL,'
    'num_sala INT NOT NULL,'
    'UNIQUE (nome),'
    'UNIQUE (num_sala)'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['alunos'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.alunos ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'turma_id INT NOT NULL,'
    'pontuacao_geral INT NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id),'
    'FOREIGN KEY (turma_id) REFERENCES turmas(id)'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'usuario_id INT NOT NULL,'
    'salario DECIMAL(10,2) NOT NULL,'
    'FOREIGN KEY (usuario_id) REFERENCES usuarios(id)'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['turmas_professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.turmas_professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'turma_id INT NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (turma_id) REFERENCES turmas(id),'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['materias'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'nome VARCHAR(255) NOT NULL'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['materias_professores'] = (
    'CREATE TABLE IF NOT EXISTS sistema_educacional.materias_professores ('
    'id INT AUTO_INCREMENT PRIMARY KEY,'
    'materia_id INT NOT NULL,'
    'professor_id INT NOT NULL,'
    'FOREIGN KEY (materia_id) REFERENCES materias(id),'
    'FOREIGN KEY (professor_id) REFERENCES professores(id)'
    ')'
)
TABELAS_SISTEMA_EDUCACIONAL['atividades'] = (
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
TABELAS_SISTEMA_EDUCACIONAL['questoes'] = (
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
TABELAS_SISTEMA_EDUCACIONAL['atividades_alunos'] = (
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