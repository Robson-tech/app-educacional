from modelos import Usuario
from formularios import FormularioUsuario


class Autenticacao:
    def __init__(self):
        self._usuarios = {}
        self._modelo = Usuario
        self._usuario = None
    
    @property
    def esta_logado(self):
        return self._usuario is not None
    
    def get_usuarios(self):
        return self._usuarios
    
    def get_usuario(self):
        return self._usuario

    def autenticar(self, email, senha):
        if email in self._usuarios:
            return self._usuarios[email].valida_senha(senha)
    
    def cadastrar(self, email, senha, info):
        if self._modelo.valida_email(None, email):
            self._usuarios[email] = self._modelo(email, senha, info)
            self._usuario = self._usuarios[email]
            return True, "Cadastro realizado com sucesso!"
        else:
            return False, "Email inválido!"
    
    def login(self, email, senha):
        if self._usuario is None:
            if not self._usuarios:
                return False, "Não há usuários cadastrados!"
            else:
                if self.autenticar(email, senha):
                    self._usuario = self._usuarios[email]
                    return True, "Login realizado com sucesso!"
                else:
                    return False, "Email ou senha incorretos!"
        else:
            return False, "Você já está logado!"
    
    def logout(self):
        if self._usuario is not None:
            self._usuario = None
            return True, "Logout realizado com sucesso!"
        else:
            return False, "Você não está logado!"