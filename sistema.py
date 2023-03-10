from controles.ControladorSistema import ControladorSistema

if __name__ == "__main__":
    ControladorSistema().inicia_sistema()

    from telas.TelaSistema import TelaSistema
from controles.ControladorUsuario import ControladorUsuario


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__tela_usuario = ControladorUsuario()

    def inicia_sistema(self):
        self.abre_tela()

    def cadastra_usuario(self):
        self.__tela_usuario.cadastro_usuario()

    def login_usuario(self):
        pass

    def encerra(self):
        exit(0)

    def abre_tela(self):
        funcao_escolhida = self.__tela_sistema.mostra_opcoes()
        if funcao_escolhida == 1:
            self.__tela_usuario.cadastro_usuario()
            self.inicia_sistema()
        elif funcao_escolhida == 2:
            #self.login_usuario()
            print('AINDA NÃO ESTÁ DISPONIVEL')
            self.inicia_sistema()
        elif funcao_escolhida == 0:
            self.encerra()
        else:
            print('ESSA NÃO É UMA OPÇÃO VÁLIDA')
            self.inicia_sistema()
class TelaUsuario:
    def cadastro_usuario_dados(self):
        print("------CADASTRO------")

        nome = input('nome:')
        email = input('email:')
        senha = input('senha:')
        telefone = input('telefone:')
        rg = input('rg:')
        cpf = input('cpf:')
        titulo = input('titulo:')

        return {'nome': nome, 'email': email, 'senha': senha, 'telefone': telefone, 'rg': rg, 'cpf': cpf,
                'titulo': titulo} 

from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario


class ControladorUsuario:
    def __init__(self):
        self.usuarios = []
        self.__telausuario = TelaUsuario()

    def cadastro_usuario(self):
        dados_usuario = self.__telausuario.cadastro_usuario_dados()
        usuario = Usuario(dados_usuario['nome'], dados_usuario['email'], dados_usuario['senha'],
                          dados_usuario['telefone'], dados_usuario['rg'],
                          dados_usuario['cpf'], dados_usuario['titulo'])

        if (self.usuarios == None) or usuario.nome != self.usuarios:
            self.usuarios.append((usuario))
        else:
            print("usuario ja cadastrado")
        print(self.usuarios)
