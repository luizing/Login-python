from tkinter import *
import tkinter
import logado

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
                janela.destroy()
                logado.init()
            else:
                print("incorreto")
                


janela = Tk()
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