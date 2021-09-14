def init():
    print('Bem Vindo!')
    print('Selecione uma opção:')
    print("1 - Alterar Senha")
    op = int(input("-> "))

    if op == 1:
        print("Digite seu usuário e senha novamente.")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        with open('usuarios.txt','r') as arquivo:
            for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0] and senha == y[1]:

                    with open('usuarios.txt','r') as arquivo:
                        for itens in arquivo:
                             y = itens.split(',')
                             if usuario == y[0]:
                                y[1] = input("Digite sua nova senha: ")
                                print(y[1])
                                break




      