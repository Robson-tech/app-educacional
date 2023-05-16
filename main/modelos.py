import datetime


class Usuario:
    def __init__(self, email, senha, info):
        self._email = email
        self._senha = senha
        self._info = info

    def __str__(self):
        return f"{self._email}" \
               f"{self._info}"

    def get_email(self):
        return self._email
    
    def valida_email(self, email):
        if "@" in email:
            return True
        else:
            return False
        
    def valida_senha(self, senha):
        if self._senha == senha:
            return True
        else:
            return False


class InfoUsuario:
    def __init__(self, nome, sobrenome, data_nascimento, sexo):
        self._nome = nome
        self._sobrenome = sobrenome
        self._data_nascimento = data_nascimento
        self._sexo = sexo
        self._eh_professor = False
        self._lista_atividades = {}
    
    def __str__(self):
        return f"Nome: {self._nome}\n" \
            f"Sobrenome: {self._sobrenome}\n" \
            f"Data de nascimento: {self._data_nascimento}\n" \
            f"Sexo: {self._sexo}\n"


class Atividade:
    def __init__(self, titulo, descricao, usuario, questoes):
        self._titulo = titulo
        self._descricao = descricao
        self._data = datetime.datetime.now()
        self._usuario = usuario
        self._questoes = questoes
    
    def __str__(self):
        return f"Titulo: {self._titulo}\n" \
            f"Descricao: {self._descricao}\n" \
            f"Data: {self._data}\n" \
            f"Usuario: {self._usuario}\n" \
            f"Questoes: {self._questoes}\n"

    def get_titulo(self):
        return self._titulo

    def get_descricao(self):
        return self._descricao

    def get_data(self):
        return self._data

    def get_usuario(self):
        return self._usuario

    def get_questoes(self):
        return self._questoes

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_data(self, data):
        self._data = data

    def set_usuario(self, usuario):
        self._usuario = usuario

    def set_questoes(self, questoes):
        self._questoes = questoes


class Questao:
    def __init__(self, numero, enunciado, alternativas, resposta):
        self._numero = numero
        self._enunciado = enunciado
        self._alternativas = alternativas
        self._resposta = resposta

    def __str__(self):
        return f"Numero: {self._numero}\n" \
            f"Enunciado: {self._enunciado}\n" \
            f"Alternativas: {self._alternativas}\n" \
            f"Resposta: {self._resposta}\n"

    def get_numero(self):
        return self._numero

    def get_enunciado(self):
        return self._enunciado

    def get_alternativas(self):
        return self._alternativas

    def get_resposta(self):
        return self._resposta

    def set_numero(self, numero):
        self._numero = numero

    def set_enunciado(self, enunciado):
        self._enunciado = enunciado

    def set_alternativas(self, alternativas):
        self._alternativas = alternativas

    def set_resposta(self, resposta):
        self._resposta = resposta

    def valida_resposta(self, resposta):
        if resposta == self._resposta:
            return True
        else:
            return False

if __name__ == "__main__":
    usuario = Usuario("joao@example.com", "123456")
