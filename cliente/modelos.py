class Questao:
    def __init__(self, id, atividade_id, resposta, letra_a, letra_b, letra_c, letra_d, letra_e, enunciado=None):
        self._id = id
        self._atividade_id = atividade_id
        self._resposta = resposta
        self.letra_a = letra_a
        self.letra_b = letra_b
        self.letra_c = letra_c
        self.letra_d = letra_d
        self.letra_e = letra_e
        self._enunciado = enunciado

    def __str__(self):
        return f'{self.id}|{self.atividade_id}|{self.resposta}|{self.letra_a}|{self.letra_b}|{self.letra_c}|{self.letra_d}|{self.letra_e}|{self.enunciado}'

    @property
    def id(self):
        return self._id

    @property
    def atividade_id(self):
        return self._atividade_id

    @property
    def resposta(self):
        return self._resposta

    @property
    def enunciado(self):
        return self._enunciado

    @enunciado.setter
    def enunciado(self, enunciado):
        self._enunciado = enunciado

    def valida_resposta(self, resposta):
        if resposta == self._resposta:
            return True
        else:
            return False