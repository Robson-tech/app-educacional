from modelos import Usuario, Atividade
from autenticacao import Autenticacao


class Sistema:
    def __init__(self):
        self._autenticacao = Autenticacao()
        self._atividades = []

    def menu(self):
        if self._autenticacao.esta_logado:
            print("1 - Cadastrar atividade")
            print("2 - Listar atividades")
            print("3 - Logout")
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                self.cadastrar_atividade()
            elif opcao == 2:
                self.listar_atividades()
            elif opcao == 3:
                self.logout()
            else:
                print("Opção inválida!")
        else:
            print("1 - Cadastrar usuário")
            print("2 - Login")
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                self.cadastrar_usuario()
            elif opcao == 2:
                self.login()
            else:
                print("Opção inválida!")