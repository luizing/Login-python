import logado
from tkinter import *
import os
import funcoes






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


