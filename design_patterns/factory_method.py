from abc import ABCMeta, abstractmethod


class Secao(metaclass=ABCMeta):

    @abstractmethod
    def descricao(self):
        pass


class SecaoPessoal(Secao):
    def descricao(self):
        print('secao pessoal')

class SecaoAlbum(Secao):
    def descricao(self):
        print('secao secao de fotos')

class SecaoPatente(Secao):
    def descricao(self):
        print('secao patente')

class SecaoPublicacao(Secao):
    def descricao(self):
        print('secao publicacao')



class Profile(metaclass=ABCMeta):
    def __init__(self, *args, **kwargs):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secoes(self, secao):
        self.secoes.append(secao)


class Facebook(Profile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def criar_perfil(self):
        self.add_secoes(SecaoPessoal())
        self.add_secoes(SecaoPatente())
        self.add_secoes(SecaoPublicacao())


class Twitter(Profile):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def criar_perfil(self):
        self.add_secoes(SecaoAlbum())
        self.add_secoes(SecaoPessoal())


if __name__ == '__main__':
    tipo_perfil = 'Facebook'
    perfil = eval(tipo_perfil)()
    print(perfil.get_secoes())
