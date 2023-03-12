from tqdm import tqdm
import time


class Usuario():
    def __init__(self, nome, cpf, email, senha) -> None:
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._senha = senha

    @property
    def nome(self):
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @property
    def email(self):
        return self._email

    @property
    def senha(self):
        return self._senha

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @email.setter
    def email(self, email):
        self._email = email

    @senha.setter
    def senha(self, senha):
        self._senha = senha


class Jogos():
    def __init__(self, Nome, Valor, Dev) -> None:
        self._nome = Nome
        self._valor = Valor
        self._dev = Dev

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self ._valor

    @property
    def dev(self):
        return self._dev

    @nome.setter
    def set_nome(self, nome):
        self._nome = nome

    @valor.setter
    def set_valor(self, valor):
        self._valor = valor

    @dev.setter
    def set_dev(self, dev):
        self._dev = dev


class Administrador(Usuario):
    def __init__(self, nome='root', cpf=9734, email='root@abc.com', senha='root') -> None:
        super().__init__(nome, cpf, email, senha)


class Loja():
    def __init__(self, saldo=0) -> None:
        self._saldo = saldo
        self._listclientes = {}
        self.list_jogos = {
            'Jogo 1': Jogos('Jogo 1', 20, 'Desenvolvedor 1'),
            'Jogo 2': Jogos('Jogo 2', 30, 'Desenvolvedor 2'),
            'Jogo 3': Jogos('Jogo 3', 25, 'Desenvolvedor 1')
        }
        self.biblioteca = {}
        self.historico = Historico()
        self.admin = Administrador()

    def add_cliente(self, cpf, usuario):
        if cpf in self._listclientes.keys():
            print('Cpf ja cadastrado')
        else:
            self._listclientes[cpf] = usuario

    def add_jogos(self, nome, jogo):
        if nome in self.list_jogos:
            print('Jogo ja cadastrado na loja')
        else:
            self.list_jogos[nome] = jogo

    def remover_jogos(self, nome):
        self.list_jogos.pop(nome)

    def imprir_listCLientes(self):
        for usuario in self._listclientes.values():
            print(
                f'Nome:{usuario.nome},CPF:{usuario.cpf},Email:{usuario.email},Senha:{usuario.senha}')

    def imprimir_jogos(self):
        for c in self.list_jogos.values():
            print(f'Nome: {c._nome}, Valor:{c._valor}, Desenvolvedor:{c._dev}')

    def deposita(self, valor):
        self._saldo += valor
        self.historico.add('Deposito realizado!')

    def comprar(self, nome):
        if nome in self.list_jogos:
            jogo = self.list_jogos[nome]

            if self._saldo >= jogo._valor:
                print('Jogo comprado com sucesso! e adcionado a biblibioteca')
                self._saldo -= jogo._valor
                self.biblioteca[nome] = nome
                self.historico.add('Jogo comprado com sucesso')

            else:
                print('Saldo insuficiente!')

    def dowload(self, nome):
        if nome in self.biblioteca:
            for i in tqdm(range(5)):
                time.sleep(1)
            print(f'Dowload do jogo {nome} concluido com sucesso!')
            self.historico.add('Dowload realizado com sucesso')
        else:
            print('Esse jogo nao existe na sua biblioteca! ')

    def exbir_bibliotrca(self):
        for c in self.biblioteca.values():
            print(c)

    def remover_biblioteca(self, nome):
        self.biblioteca.pop(nome)

    def login_cliente(self, email, senha):
        if email in self._listclientes:
            usuario = self._listclientes[email]
            if usuario.senha == senha:
                print('Login realizado com sucesso')
                while True:
                    print('==== Menu do cliente ====')
                    print('\n1 - Para comprar jogos')
                    print('2 - Para depositar na conta')
                    print('3 - Jogos disponiveis no catalogo: ')
                    print('4 - Exibir jogos na sua biblioteca')
                    print('5 - Dowload dos jogos')
                    print('6 - Para remover um jogo da sua biblioteca')
                    print('7 - fazer logout')
                    opc = input('')
                    if opc == '1':
                        nome = input(
                            'Informe o nome do jogo que deseja comprar: ')
                        self.comprar(nome)
                    elif opc == '2':
                        valor = int(
                            input('Informe o valor que deseja depositar: '))
                        self.deposita(valor)
                    elif opc == '3':
                        self.imprimir_jogos()
                    elif opc == '4':
                        self.exbir_bibliotrca()
                    elif opc == '5':
                        nome = input('Qual jogo vc deseja baixar? ')
                        self.dowload(nome)
                    elif opc == '6':
                        nome = input(
                            'Informe o nome do jogo que deseja remover da sua biblioteca: ')
                        self.remover_biblioteca(nome)
                    elif opc == '7':
                        break
                    else:
                        print('Informe uma opçao valida')
            else:
                print('Senha incorreta')
        else:
            print('CPF não cadastrado na loja')

    def login_adm(self, nome, senha):
        if self.admin.senha == senha and self.admin._nome == nome:
            print('Adminstrador logado com sucesso!')
            while True:
                print('==== Menu de administrador ====')
                print('\n1- Adicionar jogos ao catalogo')
                print('2- Remover jogos do catalogo')
                print('3- Exibir Lista de clientes')
                print('4- Historico de transaçes realziadas na conta')
                print('5- Sair da conta administrador')
                opc = input('')
                if opc == '1':
                    nome = input('Informe o nome do jogo: ')
                    valor = int(input('Informe o valor do jogo: '))
                    dev = input('Informe o desenvolvedor do jogo: ')
                    j = Jogos(nome, valor, dev)
                    self.add_jogos(nome, j)

                elif opc == '2':
                    nome = input('Informe o nome do jogo que deseja remover: ')
                    self.remover_jogos(nome)
                elif opc == '3':
                    self.imprir_listCLientes()
                elif opc == '4':
                    self.historico.imprimir()
                elif opc == '5':
                    break

                else:
                    print('Informe uma opçao valida')
        else:
            print('Informaçoes de login de adminstrador incorretas!')


class Historico():
    def __init__(self) -> None:
        self.historico = []

    def add(self, t):
        self.historico.append(t)

    def imprimir(self):
        for i in self.historico:
            print(i)
