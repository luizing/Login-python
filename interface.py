import os
from tkinter import *
import funcoes






def alterarSenha():

    def okNovaSenha():
        global nova_Senha
        nova_Senha = nova__Senha.get()
        novaSenha.destroy()

    with open('usuarios.txt','r') as arquivo:
            linhas = arquivo.readlines()
            with open('usuarios.txt', 'w') as arquivo:
                for linha in linhas:
                    elementos = linha.split(',')
                    if elementos[0] == usuario and elementos[1] == senha:

                        #interface
                        novaSenha = Tk()        
                        
                        titulo = Label(novaSenha, text= "Digite sua nova senha:")
                        titulo.grid(column=0, row=0)
                        
                        nova__Senha = Entry(novaSenha)
                        nova__Senha.grid(column=0, row = 1)

                        Ok = Button(novaSenha, text="Ok",command = okNovaSenha)
                        Ok.grid(column= 2 , row = 2)
                        novaSenha.mainloop()


                        #fim da interface
                        global nova_Senha
                        elementos[1] = nova_Senha
                        for elemento in elementos:
                            linha = elementos[0] + ',' + elementos[1] + "," + "\n"
                    linha = elementos[0] + ',' + elementos[1] + "," + "\n"
                    arquivo.write(linha)

def Apagar():
    with open('usuarios.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        with open('usuarios.txt', 'w') as arquivo:
            for linha in linhas:
                elementos = linha.split(',')
                if elementos[0] == usuario and elementos[1] == senha:
                        linha =''
                        arquivo.write(linha)
                else:
                    linha = elementos[0] + ',' + elementos[1] + "," + "\n"
                    arquivo.write(linha)
    
    Aviso = Tk()   

    titulo = Label(Aviso, text= "Usuário Apagado!")
    titulo.pack(side=TOP)

    Ok = Button(Aviso, text="Ok",command = titulo.destroy)
    Ok.pack(side=BOTTOM)

    Aviso.mainloop()
    

def aprov():
    Inicio = Tk()

    titulo = Label(Inicio, text="Bem Vindo!")
    titulo.grid(column = 1, row= 0)
    titulo.config(font=("Courier", 44))

    altSenha = Button(Inicio, text="Alterar Senha", command = alterarSenha)
    altSenha.grid(column= 0 , row= 1)

    apagar = Button(Inicio, text= "Apagar Usuario",command= Apagar)
    apagar.grid(column= 2, row = 1)


    Inicio.mainloop()

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

    janela=Tk()
    janela.title("Cadastro")

    """titulo = Label(janela, text="Cadastro")
    titulo.grid(column= 0, row = 0)"""

    usuarioL = Label(janela, text="Usuário:")
    usuarioL.grid(column = 0, row = 1)

    usuarioE = Entry(janela)
    usuarioE.grid(column = 1, row = 1)

    passL = Label(janela, text="Senha:")
    passL.grid(column = 0, row = 2)

    passE = Entry(janela)
    passE.grid(column = 1, row = 2)

    button = Button(janela, text = "Cadastrar", command = cadastro)
    button.grid(column =1 , row = 3)
    button.config(width=10)

    
    janela.geometry("210x70")

    janela.mainloop()

def Lista():
    lista = ''
    with open('usuarios.txt','r') as arquivo:
        for itens in arquivo:
            y = itens.split(',')
            if y[0] == '':
                lista = lista + ''
            else:
                lista = lista + y[0] +"\n"
    if lista == "":
        lista == "Não há usuários cadastrados."

    #Interface
    janela=Tk()
    janela.title("Lista de usuários")

    title = Label(janela, text= "Lista de Usuários:")
    title.pack(side=TOP)
    title.config(font=("Courier", 20))

    lista = Label(janela, text= lista)
    lista.pack(side=BOTTOM)

    janela.mainloop()

def Login():

    def logar():
        global usuario
        global senha
        usuario = usuarioE.get()
        senha = passE.get()

        with open('usuarios.txt','r') as arquivo:
            correto = 0
            for itens in arquivo:
                y = itens.split(',')
                if usuario == y[0] and senha == y[1]:
                    correto =+ 1
                    aprov()
                
            if correto == 0:
                jaExiste = Tk()
                jaExiste.title("Erro")
                texto = Label(jaExiste, text="Usuário ou Senha incorretos")
                texto.pack(side = TOP)
                botao = Button(jaExiste, text = "OK", command = jaExiste.destroy)
                botao.pack(side = BOTTOM)

                jaExiste.mainloop()


    janela=Tk()
    janela.title("Login")

    """titulo = Label(janela, text="Fazer Login")
    titulo.grid(column= 0, row = 0)"""

    usuarioL = Label(janela, text="Usuário:")
    usuarioL.grid(column = 0, row = 1)

    usuarioE = Entry(janela)
    usuarioE.grid(column = 1, row = 1)

    passL = Label(janela, text="Senha:")
    passL.grid(column = 0, row = 2)

    passE = Entry(janela)
    passE.grid(column = 1, row = 2)

    button = Button(janela, text = "Logar", command = logar)
    button.grid(column =1 , row = 3)
    button.config(width=10)

    janela.geometry("210x70")

    janela.mainloop()

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
titulo.config(font=("Courier", 44))


opLogin = Button(janela, text="Fazer Login", command=Login, width=15)
opLogin.grid(column = 0, row = 1)

opCadastro = Button(janela, text="Cadastrar-se", command=Cadastro, width=15)
opCadastro.grid(column = 0, row = 2)

opLista = Button(janela, text="Lista de Usuários", command=Lista, width=15)
opLista.grid(column = 0, row = 3)

opConsole = Button(janela, text="Console", command= console , fg="red", width=15)
opConsole.grid(column = 0, row = 4)

janela.geometry("220x190")

janela.mainloop()