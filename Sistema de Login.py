    #Sistema de Login

from tkinter import *
import funcoes
import os


global lista
lista = ''

while True:

    #Interface:

    janela = Tk()
    janela.title("Opções")

    titulo = Label(janela, text="Início")
    titulo.grid(column = 0, row= 0)

    opLogin = Button(janela, text="Fazer Login", command=funcoes.Login)
    opLogin.grid(column = 0, row = 1)

    opCadastro = Button(janela, text="Cadastrar-se", command=funcoes.Cadastro)
    opCadastro.grid(column = 0, row = 2)

    opLista = Button(janela, text="Lista de Usuários", command=funcoes.Lista)
    opLista.grid(column = 0, row = 3)

    opConsole = Button(janela, text="Usar Console", command=funcoes.Console)
    opConsole.grid(column = 0, row = 4)




    janela.mainloop()

    #Código

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
