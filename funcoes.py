import logado
from tkinter import *
import os
import funcoes
import extras




def Login():

    #Interface:
    def logar():
        usuario = usuarioE.get()
        senha = passE.get()

        with open('usuarios.txt','r') as arquivo:
            for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0] and senha == y[1]:
                    correto = 1
                    print("Usuario Aprovado")
                    print("=+=" *20)
                    logado.init()
                else:
                    print("incorreto")


    janela=Tk()
    janela.title("Login")

    titulo = Label(janela, text="Fazer Login")
    titulo.grid(column= 0, row = 0)

    usuarioL = Label(janela, text="Usuário:")
    usuarioL.grid(column = 0, row = 1)

    usuarioE = Entry(janela)
    usuarioE.grid(column = 1, row = 1)

    passL = Label(janela, text="Senha:")
    passL.grid(column = 0, row = 2)

    passE = Entry(janela)
    passE.grid(column = 1, row = 2)

    button = Button(janela, text = "Logar", command = logar)
    button.grid(column =2 , row = 2)



    


    janela.mainloop()

    
    

    

    


    #Codigo
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")

    correto = 0



    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if usuario == y[0] and senha == y[1]:
                correto = 1
                print("Usuario Aprovado")
                print("=+=" *20)
                logado.init()
            
        
    if correto == 0:
        print("=+=" *20)
        print("Usuario ou senha incorreta.")           
    

def Cadastro():
    print("Digite o nome de usuário desejado:")
    usuario = input("-> ")
    print("Digite uma senha:")
    senha = input("-> ")

    existe = 0

    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if usuario == y[0]:
                print("Usuário já cadastrado.")
                existe = 1
                break

    if existe == 0:
        with open('usuarios.txt','a') as arquivo:
            arquivo.write(usuario + "," + senha + "," + '\n')

def Lista():

    #Codigo
    global lista

    lista = ''
    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if y[0] == '':
                print("Nenhum Usuário cadastrado até o momento.")
                lista = ''
            else:
                print(y[0])
                lista = lista + y[0] +"\n"

    #Interface
    janela=Tk()
    janela.title("Lista de usuários")

    lista = Label(janela, text= lista,)
    lista.grid(column = 0, row=1)

    janela.mainloop()


def Console():

    while True:

        print("=+=" *20)
        print("Digite a opção desejada:")
        print("1 - Fazer Login")
        print("2 - Cadastrar-se")
        print("3 - Verificar lista de usuários")
        print("4 - Limpar console")
        print("=+=" *20)
        opcao = int(input("-> "))
        print("=+=" *20)


        if opcao == 1 :
            Login()

        if opcao == 2 :
            Cadastro()

        if opcao == 3 :
            Lista()

        if opcao == 4:
            os.system('cls||clear')
            

