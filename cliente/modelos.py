class Atividade:
    def __init__(self, id, nome, descricao, materia_id, turma_id, professor_id, questoes=None):
        self._id = id
        self._nome = nome
        self._descricao = descricao
        self._materia_id = materia_id
        self._turma_id = turma_id
        self._professor_id = professor_id
        self._questoes = questoes

    def __str__(self):
        return f'{self._id},{self._nome},{self._descricao},{self._materia_id},{self._turma_id},{self._professor_id}'
    
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome
    
    @property
    def descricao(self):
        return self._descricao

    @property
    def questoes(self):
        return self._questoes

    def add_questao(self, questao):
        self._questoes.append(questao)


class Questao:
    def __init__(self, id, atividade_id, enunciado, resposta, letra_a, letra_b, letra_c, letra_d, letra_e):
        self._id = id
        self._atividade_id = atividade_id
        self._enunciado = enunciado
        self._resposta = resposta
        self.letra_a = letra_a
        self.letra_b = letra_b
        self.letra_c = letra_c
        self.letra_d = letra_d
        self.letra_e = letra_e

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


if __name__ == '__main__':
    atividade = Atividade(1, 'função afim', 'atividade de função', 1, 1, 1)
    print(atividade.nome)
