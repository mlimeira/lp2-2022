from autenticavel import AutenticavelInterface


class SistemaInterno():
    def login(self, objeto, senha):
        if isinstance(objeto, AutenticavelInterface):
            print(f'{objeto} é autenticavel')
            if objeto.autentica(senha):
                print(f'{objeto} está logado')
            else:
                print('senha incorreta')
        else:
            print(f'{objeto} não é autenticavel')