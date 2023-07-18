import abc


class Usuario(abc.ABC):
    """
    Classe abstrata que representa um usuário do sistema

    ...

    Attributes
    ---------
    id : int
        id do usuário
    email : str
        email do usuário
    senha : str
        senha do usuário
    nome : str
        nome do usuário
    sobrenome : str
        sobrenome do usuário
    nascimento : str
        data de nascimento do usuário
    data_cadastro : str
        data de cadastro do usuário
    ultimo_login : str
        data do último login do usuário

    Methods
    -------
    validar_email(email)
        Valida o email do usuário
    validar_senha(senha)
        Valida a senha do usuário
    """
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login):
        """
        Parameters
        ----------
        id : int
            id do usuário
        email : str
            email do usuário
        senha : str
            senha do usuário
        nome : str
            nome do usuário
        sobrenome : str
            sobrenome do usuário
        nascimento : str
            data de nascimento do usuário
        data_cadastro : str
            data de cadastro do usuário
        ultimo_login : str
            data do último login do usuário
        """
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
        """
        Valida o email do usuário

        Parameters
        ----------
        email : str
            email do usuário
        """
        pass

    @abc.abstractmethod
    def validar_senha(self, senha):
        """
        Valida a senha do usuário

        Parameters
        ----------
        senha : str
            senha do usuário
        """
        pass


class Diretor(Usuario):
    """
    Classe que representa um diretor do sistema

    ...

    Attributes
    ---------
    id : int
        id do usuário
    email : str
        email do usuário
    senha : str
        senha do usuário
    nome : str
        nome do usuário
    sobrenome : str
        sobrenome do usuário
    nascimento : str
        data de nascimento do usuário
    data_cadastro : str
        data de cadastro do usuário
    ultimo_login : str
        data do último login do usuário

    Methods
    -------
    validar_email(email)
        Valida o email do usuário
    validar_senha(senha)
        Valida a senha do usuário
    """
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login):
        """
        Parameters
        ----------
        id : int
            id do usuário
        email : str
            email do usuário
        senha : str
            senha do usuário
        nome : str
            nome do usuário
        sobrenome : str
            sobrenome do usuário
        nascimento : str
            data de nascimento do usuário
        data_cadastro : str
            data de cadastro do usuário
        ultimo_login : str
            data do último login do usuário
        """
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)

    def validar_email(self, email):
        """
        Valida o email do usuário

        Parameters
        ----------
        email : str
            email do usuário

        Returns
        -------
        bool
            True se o email for válido, False caso contrário
        """
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        """
        Valida a senha do usuário

        Parameters
        ----------
        senha : str
            senha do usuário
        
        Returns
        -------
        bool
            True se a senha for válida, False caso contrário
        """
        if self._senha == senha:
            return True
        else:
            return False


class Professor(Usuario):
    """
    Classe que representa um professor do sistema
    
    ...

    Attributes
    ---------
    id : int
        id do usuário
    email : str
        email do usuário
    senha : str
        senha do usuário
    nome : str
        nome do usuário
    sobrenome : str
        sobrenome do usuário
    nascimento : str
        data de nascimento do usuário
    data_cadastro : str
        data de cadastro do usuário
    ultimo_login : str
        data do último login do usuário
    materias_professor : list
        lista de matérias que o professor leciona
    turmas_professor : dict
        dicionário de turmas que o professor leciona
    atividades_professor : dict
        dicionário de atividades que o professor criou
    salario : float
        salário do professor

    Methods
    -------
    validar_email(email)
        Valida o email do usuário
    validar_senha(senha)
        Valida a senha do usuário
    """
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, materias_professor=[], turmas_professor={}, atividades_professor={}, salario=1320):
        """
        Parameters
        ----------
        id : int
            id do usuário
        email : str
            email do usuário
        senha : str
            senha do usuário
        nome : str
            nome do usuário
        sobrenome : str
            sobrenome do usuário
        nascimento : str
            data de nascimento do usuário
        data_cadastro : str
            data de cadastro do usuário
        ultimo_login : str
            data do último login do usuário
        """
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._materias_professor = materias_professor
        self._turmas_professor = turmas_professor
        self._atividades_professor = atividades_professor
        self._salario = salario

    def __str__(self):
        return f'{self._id},{self._email},{self._senha},{self._nome},{self._sobrenome},{self._nascimento},{self._data_cadastro},{self._ultimo_login},salario={self._salario}'

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
        """
        Valida o email do usuário

        Parameters
        ----------
        email : str
            email do usuário

        Returns
        -------
        bool
            True se o email for válido, False caso contrário
        """
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        """
        Valida a senha do usuário

        Parameters
        ----------
        senha : str
            senha do usuário

        Returns
        -------
        bool
            True se a senha for válida, False caso contrário
        """
        if self._senha == senha:
            return True
        else:
            return False


class Aluno(Usuario):
    """
    Classe que representa um aluno do sistema

    ...

    Attributes
    ---------
    id : int
        id do usuário
    email : str
        email do usuário
    senha : str
        senha do usuário
    nome : str
        nome do usuário
    sobrenome : str
        sobrenome do usuário
    nascimento : str
        data de nascimento do usuário
    data_cadastro : str
        data de cadastro do usuário
    ultimo_login : str
        data do último login do usuário
    turma : str
        turma do aluno
    pontuacao : int
        pontuação do aluno

    Methods
    -------
    validar_email(email)
        Valida o email do usuário
    validar_senha(senha)
        Valida a senha do usuário
    """
    def __init__(self, id, email, senha, nome, sobrenome, nascimento, data_cadastro, ultimo_login, turma, pontuacao=0):
        """
        Parameters
        ----------
        id : int
            id do usuário
        email : str
            email do usuário
        senha : str
            senha do usuário
        nome : str
            nome do usuário
        sobrenome : str
            sobrenome do usuário
        nascimento : str
            data de nascimento do usuário
        data_cadastro : str
            data de cadastro do usuário
        ultimo_login : str
            data do último login do usuário
        turma : str
            turma do aluno
        pontuacao : int
            pontuação do aluno
        """
        super().__init__(id, email, senha, nome, sobrenome,
                         nascimento, data_cadastro, ultimo_login)
        self._turma = turma
        self._pontuacao = pontuacao

    def __str__(self):
        return f'{self._id},{self._email},{self._senha},{self._nome},{self._sobrenome},{self._nascimento},{self._data_cadastro},{self._ultimo_login},{self._turma},{self._pontuacao}'

    def validar_email(self, email):
        """
        Valida o email do usuário

        Parameters
        ----------
        email : str
            email do usuário

        Returns
        -------
        bool
            True se o email for válido, False caso contrário
        """
        if email.find("@") != -1:
            return True
        else:
            return False

    def validar_senha(self, senha):
        """
        Valida a senha do usuário

        Parameters
        ----------
        senha : str
            senha do usuário

        Returns
        -------
        bool
            True se a senha for válida, False caso contrário
        """
        if self._senha == senha:
            return True
        else:
            return False
        
        
class Materia:
    """
    Classe que representa uma matéria

    ...

    Attributes
    ---------
    id : int
        id da matéria
    nome : str
        nome da matéria
    atividades : dict
        dicionário de atividades da matéria
    professores : list
        lista de professores que lecionam a matéria

    Methods
    -------
    abrir(usuario)
        Abre as atividades da matéria
    """
    def __init__(self, id, nome, atividades={}, professores=[]):
        """
        Parameters
        ----------
        id : int
            id da matéria
        nome : str
            nome da matéria
        atividades : dict
            dicionário de atividades da matéria
        professores : list
            lista de professores que lecionam a matéria
        """
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

    # def abrir(self, usuario):
        """
        Abre as atividades da matéria

        Parameters
        ----------
        usuario : Usuario
            usuário que está abrindo as atividades
        """
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
    """
    Classe que representa uma atividade

    ...

    Attributes
    ---------
    id : int
        id da atividade
    titulo : str
        título da atividade
    descricao : str
        descrição da atividade
    professor_id : int
        id do professor que criou a atividade
    turma_id : int
        id da turma da atividade
    materia_id : int
        id da matéria da atividade
    questoes : dict
        dicionário de questões da atividade
    respondidas : int
        quantidade de questões respondidas
    pontuacao : int
        pontuação da atividade

    Methods
    -------
    imprimir_questoes()
        Imprime as questões da atividade
    add_questao(questao)
        Adiciona uma questão à atividade
    remover_questao(num)
        Remove uma questão da atividade
    editar_questao(num)
        Edita uma questão da atividade
    resetar()
        Reseta a atividade
    abrir(sistema)
        Abre a atividade
    """
    def __init__(self, id, titulo, descricao, professor_id, turma_id, materia_id, questoes={}):
        """
        Parameters
        ----------
        id : int
            id da atividade
        titulo : str
            título da atividade
        descricao : str
            descrição da atividade
        professor_id : int
            id do professor que criou a atividade
        turma_id : int
            id da turma da atividade
        materia_id : int
            id da matéria da atividade
        questoes : dict
            dicionário de questões da atividade
        """
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
        return f'{self._id}//{self._titulo}//{self._descricao}//{self._professor_id}//{self._turma_id}//{self._materia_id}//{self._respondidas}//{self._pontuacao}'
    
    def imprimir_questoes(self):
        """
        Imprime as questões da atividade
        
        """
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
    def materia_id(self):
        return self._materia_id

    @property
    def questoes(self):
        return self._questoes

    # def add_questao(self, questao):
    #     """
    #     Adiciona uma questão à atividade

    #     Parameters
    #     ----------
    #     questao : Questao
    #         questão a ser adicionada
    #     """
    #     self._questoes[len(self._questoes) * -1] = questao

    # def remover_questao(self, num):
    #     """
    #     Remove uma questão da atividade

    #     Parameters
    #     ----------
    #     num : int
    #         número da questão a ser removida
    #     """
    #     try:
    #         self._questoes.pop(num)
    #     except KeyError:
    #         print('Questão não encontrada')

    # def editar_questao(self, num):
    #     """
    #     Edita uma questão da atividade

    #     Parameters
    #     ----------
    #     num : int
    #         número da questão a ser editada
    #     """
    #     try:
    #         print(
    #             f'{num} - {self._questoes[num].enunciado}\n'
    #             f'A) {self._questoes[num].letra_a}\n'
    #             f'B) {self._questoes[num].letra_b}\n'
    #             f'C) {self._questoes[num].letra_c}\n'
    #             f'D) {self._questoes[num].letra_d}\n'
    #             f'E) {self._questoes[num].letra_e}\n'
    #             '1 - Enunciado\n'
    #             '2 - Resposta\n'
    #             'a - Alternativa A\n'
    #             'b - Alternativa B\n'
    #             'c - Alternativa C\n'
    #             'd - Alternativa D\n'
    #             'e - Alternativa E\n'
    #             '0 - Sair'
    #         )
    #         opc = input('Digite a opção: ')
    #         opc = int(opc) if opc.isdigit() else opc
    #         while opc:
    #             if opc == 1:
    #                 enunciado = input('Digite o enunciado: ')
    #                 self._questoes[num].enunciado = enunciado
    #             elif opc == 2:
    #                 resposta = input('Digite a resposta: ')
    #                 self._questoes[num].resposta = resposta
    #             elif opc.isalpha() and opc.lower() == 'a':
    #                 letra_a = input('Digite a alternativa A: ')
    #                 self._questoes[num].letra_a = letra_a
    #             elif opc.isalpha() and opc.lower() == 'b':
    #                 letra_b = input('Digite a alternativa B: ')
    #                 self._questoes[num].letra_b = letra_b
    #             elif opc.isalpha() and opc.lower() == 'c':
    #                 letra_c = input('Digite a alternativa C: ')
    #                 self._questoes[num].letra_c = letra_c
    #             elif opc.isalpha() and opc.lower() == 'd':
    #                 letra_d = input('Digite a alternativa D: ')
    #                 self._questoes[num].letra_d = letra_d
    #             elif opc.isalpha() and opc.lower() == 'e':
    #                 letra_e = input('Digite a alternativa E: ')
    #                 self._questoes[num].letra_e = letra_e
    #             else:
    #                 print('Opção inválida')
    #             print(
    #                 '1 - Enunciado\n'
    #                 '2 - Resposta\n'
    #                 'a - Alternativa A\n'
    #                 'b - Alternativa B\n'
    #                 'c - Alternativa C\n'
    #                 'd - Alternativa D\n'
    #                 'e - Alternativa E\n'
    #                 '0 - Sair'
    #             )
    #             opc = input('Digite a opção: ')
    #             opc = int(opc) if opc.isdigit() else opc
    #     except KeyError:
    #         print('Questão não encontrada')

    # def resetar(self):
    #     """
    #     Reseta a atividade
    #     """
    #     self._respondidas = 0
    #     self._pontuacao = 0
    #     for questao in self._questoes.values():
    #         questao.respondida = False

    # def abrir(self, sistema):
        """
        Abre a atividade

        Parameters
        ----------
        sistema : Sistema
            sistema que está abrindo a atividade
        """
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
    """
    Classe que representa uma questão

    ...

    Attributes
    ---------
    id : int
        id da questão
    atividade_id : int
        id da atividade da questão
    enunciado : str
        enunciado da questão
    resposta : str
        resposta da questão
    letra_a : str
        alternativa A da questão
    letra_b : str
        alternativa B da questão
    letra_c : str
        alternativa C da questão
    letra_d : str
        alternativa D da questão
    letra_e : str
        alternativa E da questão
    respondida : bool
        True se a questão foi respondida, False caso contrário

    Methods
    -------
    validar_resposta(resposta)
        Valida a resposta da questão
    """
    def __init__(self, id, atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e):
        """
        Parameters
        ----------
        id : int
            id da questão
        atividade_id : int
            id da atividade da questão
        enunciado : str
            enunciado da questão
        resposta : str
            resposta da questão
        letra_a : str
            alternativa A da questão
        letra_b : str
            alternativa B da questão
        letra_c : str
            alternativa C da questão
        letra_d : str
            alternativa D da questão
        letra_e : str
            alternativa E da questão
        """
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
        """
        Valida a resposta da questão

        Parameters
        ----------
        resposta : str
            resposta da questão

        Returns
        -------
        bool
            True se a resposta for válida, False caso contrário
        """
        if not self.respondida:
            self.respondida = True
            if resposta == self._resposta:
                return True
            else:
                return False
        else:
            print('Questão já respondida')
            return False


if __name__ == '__main__':
    atividade = Atividade(1, 'função afim', 'atividade de função', 1, 1, 1)
    print(atividade.nome)
