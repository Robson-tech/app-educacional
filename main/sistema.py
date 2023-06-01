from formularios import FormularioAtividade, FormularioUsuario, FormularioQuestao
from autenticacao import Autenticacao


class Sistema:
    def __init__(self):
        self._autenticacao = Autenticacao()
        self._atividades = []

    def menu(self):
        while True:
            if self._autenticacao.esta_logado:
                if self._autenticacao.get_usuario().eh_professor():
                    print("1 - Cadastrar atividade")
                    print("2 - Listar atividades")
                    print("0 - Logout")
                    opcao = int(input("Digite a opção desejada: "))

                    if opcao == 1:
                        self._atividades.append(
                            FormularioAtividade().cadastrar(self._autenticacao.usuario))
                    elif opcao == 2:
                        for atividade in self._atividades:
                            print(atividade)
                    elif opcao == 0:
                        self._autenticacao.logout()
                    else:
                        print("Opção inválida!")
                else:
                    print("1 - Listar atividades")
                    print("0 - Logout")
                    opcao = int(input("Digite a opção desejada: "))

                    if opcao == 1:
                        for atividade in self._atividades:
                            print(atividade)
                    elif opcao == 0:
                        self._autenticacao.logout()
                    else:
                        print("Opção inválida!")
            else:
                if not self._autenticacao.get_usuarios():
                    FormularioUsuario(self._autenticacao).cadastrar()
                else:
                    print("1 - Cadastrar usuário")
                    print("2 - Login")
                    print("0 - Sair")
                    opcao = int(input("Digite a opção desejada: "))

                    if opcao == 1:
                        FormularioUsuario(self._autenticacao).cadastrar()
                    elif opcao == 2:
                        FormularioUsuario(self._autenticacao).login()
                    elif opcao == 0:
                        exit()
                    else:
                        print("Opção inválida!")


if __name__ == "__main__":
    sistema = Sistema()
    sistema.menu()
