import abc
import datetime


class Usuario(abc.ABC):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login):
        self._id = id
        self._email = email
        self._senha = senha
        self._nome = nome
        self._sobrenome = sobrenome
        self._nascimento = nascimento
        self._data_cadastro = data_cadastro
        self._ultimo_login = ultimo_login

    def __str__(self):
        return self.email

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def sobrenome(self):
        return self._sobrenome

    @property
    def nascimento(self):
        return self._nascimento

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    @property
    def ultimo_login(self):
        return self._ultimo_login

    @id.setter
    def id(self, id):
        self._id = id

    @abc.abstractmethod
    def validar_email(self, email):
        pass

    @abc.abstractmethod
    def validar_senha(self, senha):
        pass


class Diretor(Usuario):
    def __init__(self, email, senha, nome, sobrenome, nascimento):
        super().__init__(email, senha, nome, sobrenome, nascimento)

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Professor(Usuario):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, materias_professor=[], turmas_professor={}, atividades_professor={}, salario=1320):
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._materias_professor = materias_professor
        self._turmas_professor = turmas_professor
        self._atividades_professor = atividades_professor
        self._salario = salario

    def __str__(self):
        return f'{self._id}\n{self._email}\n{self._senha}\n{self._nome}\n{self._sobrenome}\n{self._nascimento}\n{self._data_cadastro}\n{self._ultimo_login}\n{self._materias_professor}\n{self._turmas_professor}\n{self._atividades_professor}\n{self._salario}'

    @property
    def materias(self):
        return self._materias_professor

    def add_materia(self, materia):
        self._materias_professor.append(materia)

    @property
    def turmas(self):
        return self._turmas_professor
    
    @property
    def atividades(self):
        return self._atividades_professor

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Aluno(Usuario):
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, turma, pontuacao=0):
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._turma = turma
        self._pontuacao = pontuacao

    def validar_email(self, email):
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class Materia:
    def __init__(self, id, nome, atividades={}, professores=[]):
        self._id = id
        self._nome = nome.capitalize()
        self._atividades = atividades
        self._professores = professores

    def __str__(self):
        return f'{self._id}-{self._nome}'

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def atividades(self):
        return self._atividades

    # def add_atividade(self, atividade):
    #     self._atividades.append(atividade)

    def abrir(self, usuario):
        for num, atividade in self._atividades.items():
            print(f'{num} - {atividade.titulo}')
        opc = int(input('Digite o número da atividade: '))
        while opc:
            try:
                if self._atividades[opc].questoes:
                    self._atividades[opc].abrir(usuario)
                    for num, atividade in self._atividades.items():
                        print(f'{num} - {atividade.titulo}')
                    print('0 - Sair')
                else:
                    print('Atividade sem questões')
                opc = int(input('Digite o número da atividade: '))
            except KeyError:
                print('Atividade não encontrada')
                opc = int(input('Digite o número da atividade: '))


class Turma:
    def __init__(self, id, nome, num_sala, atividades={}, alunos={}, professores={}):
        self._id = id
        self._nome = nome
        self._num_sala = num_sala
        self._atividades = atividades
        self._alunos = alunos
        self._professores = professores

    def __str__(self):
        return f'{self._id}-{self._nome}'

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def atividades(self):
        return self._atividades

    @property
    def alunos(self):
        return self._alunos

    @property
    def professores(self):
        return self._professores

    # def add_aluno(self, aluno):
    #     self._alunos.append(aluno)

    def abrir(self, sistema):
        for num, atividade in self._atividades.items():
            print(f'{num} - {atividade.titulo}')
        print(
            '+ - Adicionar atividade\n'
            '- - Remover atividade\n'
            '0 - Sair'
        )
        opc = input('Digite a opção: ')
        opc = int(opc) if opc.isdigit() else opc
        while opc:
            if opc == '+':
                nova = None
                while not nova:
                    titulo = input('Digite o título da atividade: ')
                    descricao = input('Digite a descrição da atividade: ')
                    print('Materias:')
                    for materia in sistema.usuario.materias:
                        print(f'{materia[0]} - {materia[1].capitalize()}')
                    materia_id = int(input('Digite o id da matéria: '))
                    if materia_id in [materia[0] for materia in sistema.usuario.materias]:
                        nova = sistema.cadastrar_atividade(titulo, descricao, self.id, materia_id)
                    else:
                        print('Matéria não encontrada')
                    if nova:
                        self._atividades[nova.id] = nova
            elif opc == '-':
                pass
            else:
                try:
                    self._atividades[opc].abrir(sistema)
                except KeyError:
                    print('Atividade não encontrada')
            for num, atividade in self._atividades.items():
                print(f'{num} - {atividade.titulo}')
            print('0 - Sair')
            opc = input('Digite a opção: ')
            opc = int(opc) if opc.isdigit() else opc


class Atividade:
    def __init__(self, id, titulo, descricao, professor_id, turma_id, materia_id, questoes={}):
        self._id = id
        self._titulo = titulo
        self._descricao = descricao
        self._professor_id = professor_id
        self._turma_id = turma_id
        self._materia_id = materia_id
        self._questoes = questoes
        self._respondidas = 0
        self._pontuacao = 0

    def __str__(self):
        return f'{self._id}-{self._titulo}-{self._descricao}-{self._materia_id}-{self._turma_id}-{self._professor_id}'
    
    def imprimir_questoes(self):
        for num, questao in self._questoes.items():
            print(f'{num} - {questao.enunciado}')
            print(f'A) {questao.letra_a}')
            print(f'B) {questao.letra_b}')
            print(f'C) {questao.letra_c}')
            print(f'D) {questao.letra_d}')
            print(f'E) {questao.letra_e}')

    @property
    def id(self):
        return self._id

    @property
    def titulo(self):
        return self._titulo

    @property
    def descricao(self):
        return self._descricao
    
    @property
    def turma_id(self):
        return self._turma_id

    @property
    def questoes(self):
        return self._questoes

    def add_questao(self, questao):
        self._questoes[len(self._questoes) * -1] = questao

    def remover_questao(self, num):
        try:
            self._questoes.pop(num)
        except KeyError:
            print('Questão não encontrada')

    def editar_questao(self, num):
        try:
            print(
                f'{num} - {self._questoes[num].enunciado}\n'
                f'A) {self._questoes[num].letra_a}\n'
                f'B) {self._questoes[num].letra_b}\n'
                f'C) {self._questoes[num].letra_c}\n'
                f'D) {self._questoes[num].letra_d}\n'
                f'E) {self._questoes[num].letra_e}\n'
                '1 - Enunciado\n'
                '2 - Resposta\n'
                'a - Alternativa A\n'
                'b - Alternativa B\n'
                'c - Alternativa C\n'
                'd - Alternativa D\n'
                'e - Alternativa E\n'
                '0 - Sair'
            )
            opc = input('Digite a opção: ')
            opc = int(opc) if opc.isdigit() else opc
            while opc:
                if opc == 1:
                    enunciado = input('Digite o enunciado: ')
                    self._questoes[num].enunciado = enunciado
                elif opc == 2:
                    resposta = input('Digite a resposta: ')
                    self._questoes[num].resposta = resposta
                elif opc.isalpha() and opc.lower() == 'a':
                    letra_a = input('Digite a alternativa A: ')
                    self._questoes[num].letra_a = letra_a
                elif opc.isalpha() and opc.lower() == 'b':
                    letra_b = input('Digite a alternativa B: ')
                    self._questoes[num].letra_b = letra_b
                elif opc.isalpha() and opc.lower() == 'c':
                    letra_c = input('Digite a alternativa C: ')
                    self._questoes[num].letra_c = letra_c
                elif opc.isalpha() and opc.lower() == 'd':
                    letra_d = input('Digite a alternativa D: ')
                    self._questoes[num].letra_d = letra_d
                elif opc.isalpha() and opc.lower() == 'e':
                    letra_e = input('Digite a alternativa E: ')
                    self._questoes[num].letra_e = letra_e
                else:
                    print('Opção inválida')
                print(
                    '1 - Enunciado\n'
                    '2 - Resposta\n'
                    'a - Alternativa A\n'
                    'b - Alternativa B\n'
                    'c - Alternativa C\n'
                    'd - Alternativa D\n'
                    'e - Alternativa E\n'
                    '0 - Sair'
                )
                opc = input('Digite a opção: ')
                opc = int(opc) if opc.isdigit() else opc
        except KeyError:
            print('Questão não encontrada')

    def resetar(self):
        self._respondidas = 0
        self._pontuacao = 0
        for questao in self._questoes.values():
            questao.respondida = False

    def abrir(self, sistema):
        if isinstance(sistema.usuario, Aluno):
            self.imprimir_questoes()
            print('0 - Sair')
            while self._respondidas < len(self._questoes):
                try:
                    num, resposta = input(
                        'Digite o número da questão e a resposta: ').split()
                    num = int(num)
                    if not self._questoes[num].respondida:
                        if self._questoes[num].validar_resposta(resposta):
                            self._pontuacao += 1
                        self._respondidas += 1
                    else:
                        print('Questão já respondida')
                except ValueError:
                    print('Digite um número e uma letra')
                except KeyError:
                    print('Questão não encontrada')
            print(f'Você acertou {self._pontuacao} questões')
            self.resetar()
        elif isinstance(sistema.usuario, Professor):
            self.imprimir_questoes()
            print(
                '1 - Adicionar questão\n'
                '2 - Remover questão\n'
                '3 - Editar questão\n'
                '0 - Sair'
            )
            opc = int(input('Digite a opção: '))
            while opc:
                if opc == 1:
                    nova = None
                    while not nova:
                        enunciado = input('Digite o enunciado: ')
                        resposta = input('Digite a resposta: ')
                        letra_a = input('Digite a alternativa A: ')
                        letra_b = input('Digite a alternativa B: ')
                        letra_c = input('Digite a alternativa C: ')
                        letra_d = input('Digite a alternativa D: ')
                        letra_e = input('Digite a alternativa E: ')
                        nova = sistema.cadastrar_questao(self.id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e)
                        if nova:
                            self.add_questao(nova)
                elif opc == 2:
                    num = int(input('Digite o número da questão: '))
                    self.remover_questao(num)
                elif opc == 3:
                    num = int(input('Digite o número da questão: '))
                    self.editar_questao(num)
                else:
                    print('Opção inválida')
                self.imprimir_questoes()
                print(
                    '1 - Adicionar questão\n'
                    '2 - Remover questão\n'
                    '3 - Editar questão\n'
                    '0 - Sair'
                )
                opc = int(input('Digite a opção: '))


class Questao:
    def __init__(self, id, atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e):
        self._id = id
        self._atividade_id = atividade_id
        self._resposta = resposta
        self.enunciado = enunciado
        self.letra_a = letra_a
        self.letra_b = letra_b
        self.letra_c = letra_c
        self.letra_d = letra_d
        self.letra_e = letra_e
        self.respondida = False

    def __str__(self):
        return f'{self.id}|{self.atividade_id}|{self.enunciado}|{self.resposta}|{self.letra_a}|{self.letra_b}|{self.letra_c}|{self.letra_d}|{self.letra_e}'

    @property
    def id(self):
        return self._id

    @property
    def atividade_id(self):
        return self._atividade_id

    @property
    def resposta(self):
        return self._resposta
    
    @resposta.setter
    def resposta(self, resposta):
        self._resposta = resposta

    def validar_resposta(self, resposta):
        if not self.respondida:
            self.respondida = True
            if resposta == self._resposta:
                return True
            else:
                return False
        else:
            print('Questão já respondida')
            return False


if __name__ == "__main__":
    professor = Professor(
        1,
        'rafael@example.com',
        '123456',
        'Rafael',
        'Santos',
        datetime.date(1999, 1, 1),
        datetime.datetime.now(),
        datetime.datetime.now(),
        materias_professor=[(1, 'Matemática'), (2, 'Português')],
        turmas_professor=[(1, '1A'), (2, '1B')],
        atividades_professor=[
            (1, 'Atividade 1', 'Descrição 1'), (2, 'Atividade 2', 'Descrição 2')],
    )
    questao = Questao(
        1,
        1,
        '(FCC) Qual é a velocidade escalar média, em km//h, de uma pessoa que percorre a pé 1200 m em 20 min?',
        'a',
        '4,8',
        '3,6',
        '2,7',
        '2,1',
        '1,2',
    )
    atividade = Atividade(
        1,
        'Atividade 1',
        'Descrição 1',
        1,
        1,
        1,
        questoes={
            1: questao
        }
    )
    turma = Turma(
        1,
        '1A',
        1,
        atividades={
            1: atividade
        },
        professores={
            1: professor
        }
    )
    turma.abrir(professor)