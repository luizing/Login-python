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
            linhas = arquivo.readlines()
            with open('usuarios.txt', 'w') as arquivo:
                for linha in linhas:
                    elementos = linha.split(',')
                    if elementos[0] == usuario and elementos[1] == senha:
                        nova_Senha = input('Digite sua nova senha: ')
                        elementos[1] = nova_Senha
                        for elemento in elementos:
                            linha = elementos[0] + ',' + elementos[1] + "," + "\n"
                    linha = elementos[0] + ',' + elementos[1] + "," + "\n"
                    arquivo.write(linha)




"""for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0] and senha == y[1]:
                    print("a")
                    for linhas in arquivo:
                        y = itens.split(',')
                        if usuario == y[0]:
                            nova_Senha = input("Digite sua nova senha: ")
                            with open('usuarios.txt','a') as arquivo:
                                arquivo.write(usuario + "," + nova_Senha + "," + '\n')
                                break"""
      