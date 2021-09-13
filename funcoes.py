import logado

def Login():
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    correto = 0

    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if usuario == y[0] and senha == y[1]:
                correto = 1
                print("Usuario Aprovado")
                logado.init()
            if correto == 0:
                print("Usuario ou senha incorreta.")
                break
        
            
    

def Cadastro():
    print("Digite o nome de usuário desejado:")
    usuario = input("-> ")
    print("Digite uma senha:")
    senha = input("-> ")

    with open('usuarios.txt','a') as arquivo:
        arquivo.write(usuario + "," + senha + "," + '\n')

def Lista():
    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if y[0] == '':
                print("Nenhum Usuário cadastrado até o momento.")
            else:
                print(y[0])
            

