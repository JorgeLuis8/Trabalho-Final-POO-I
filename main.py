from trabfinalv2 import Loja,Administrador,Usuario
loja = Loja()
a = Administrador()
while True:
    print("=== Loja de Jogos ===")
    print("1 - Cadastro de Cliente")
    print("2 - Login no sistema")
    print('3 - Exibir lista de jogos disponiveis')
    print("4 - Login como adm")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input('Informe seu nome: ')
        cpf = input('Informe seu cpf: ')
        email = input('Informe seu email: ')
        senha = input('Informe sua senha: ')
        u = Usuario(nome, cpf, email, senha)
        loja.add_cliente(cpf, u)
    if opcao == '2':
        cpf = input('Informe seu email: ')
        senha = input('Informe sua senha: ')
        loja.login_cliente(cpf, senha)
    if opcao == '3':
        loja.imprimir_jogos()

    if opcao == '4':
        nome = input('Nome adm: ')
        senha = input('senha adm: ')
        loja.login_adm(nome, senha)
    elif opcao == '5':
        break
    else:
        print('Informe uma opçao valida')
