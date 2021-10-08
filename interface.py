import os
from tkinter import *
import funcoes

def aprov():
    a = Tk()

def Cadastro():

    def cadastro():
        usuario = usuarioE.get()
        senha = passE.get()

        existe = 0

        with open('usuarios.txt','r') as arquivo:
            for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0]:

                    #Mensagem de "Usuário já existente"
                    jaExiste = Tk()
                    jaExiste.title("Erro")
                    texto = Label(jaExiste, text="Usuário já cadastrado!")
                    texto.pack(side = TOP)
                    botao = Button(jaExiste, text = "OK", command = jaExiste.destroy)
                    botao.pack(side = BOTTOM)

                    jaExiste.mainloop()

                    existe = 1
                    break

        if existe == 0:
            with open('usuarios.txt','a') as arquivo:
                arquivo.write(usuario + "," + senha + "," + '\n')
            janela.destroy()

    cad=Tk()
    janela.title("Cadastro")

    titulo = Label(janela, text="Cadastro")
    titulo.grid(column= 0, row = 0)

    usuarioL = Label(janela, text="Usuário:")
    usuarioL.grid(column = 0, row = 1)

    usuarioE = Entry(janela)
    usuarioE.grid(column = 1, row = 1)

    passL = Label(janela, text="Senha:")
    passL.grid(column = 0, row = 2)

    passE = Entry(janela)
    passE.grid(column = 1, row = 2)

    button = Button(janela, text = "Cadastrar", command = cadastro)
    button.grid(column =2 , row = 2)

    cad.mainloop()

def Lista():
    lista = ''
    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if y[0] == '':
                lista = ''
            else:
                lista = lista + y[0] +"\n"


    #Interface
    users=Tk()
    users.title("Lista de usuários")

    lista = Label(janela, text= lista)
    lista.grid(column = 0, row=1)

    users.mainloop()

def Login():

    def logar():
        usuario = usuarioE.get()
        senha = passE.get()

        with open('usuarios.txt','r') as arquivo:
            for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0] and senha == y[1]:
                    correto = 1
                    aprov()
                else:
                    print("incorreto")


    login=Tk()
    login.title("Login")

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

    login.mainloop()

def console():
    janela.destroy
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
            funcoes.Login()

        if opcao == 2 :
            funcoes.Cadastro()

        if opcao == 3 :
            funcoes.Lista()

        if opcao == 4:
            os.system('cls||clear')


janela = Tk()
janela.title("Opções")

titulo = Label(janela, text="Início")
titulo.grid(column = 0, row= 0)

opLogin = Button(janela, text="Fazer Login", command=Login)
opLogin.grid(column = 0, row = 1)

opCadastro = Button(janela, text="Cadastrar-se", command=Cadastro)
opCadastro.grid(column = 0, row = 2)

opLista = Button(janela, text="Lista de Usuários", command=Lista)
opLista.grid(column = 0, row = 3)

opConsole = Button(janela, text="Console", command= console)
opConsole.grid(column = 0, row = 4)

janela.mainloop()