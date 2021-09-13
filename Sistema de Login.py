    #Sistema de Login
import funcoes

correto = 0

while correto == 0:

    print("=+=" *20)
    print("Digite a opção desejada:")
    print("1 - Fazer Login")
    print("2 - Cadastrar-se")
    print("3 - Verificar lista de usuários")
    print("=+=" *20)
    opcao = int(input("-> "))
    print("=+=" *20)


    if opcao == 1 :
        funcoes.Login()

    if opcao == 2 :
        funcoes.Cadastro()

    if opcao == 3 :
        funcoes.Lista()

"""if opcao != 1 and opcao != 2 and opcao != 3:
    print("Digite 1, 2 ou 3")
    print("=+=" *20)
    print("Digite a opção desejada:")
    print("1 - Fazer Login")
    print("2 - Cadastrar-se")
    print("3 - Verificar lista de usuários")
    print("=+=" *20)
    opcao = input("-> ")"""