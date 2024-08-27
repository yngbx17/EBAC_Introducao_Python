
#Faça um programa que verifica se uma senha fornecida pelo usuário é válida.
#A senha deve atender aos seguintes critérios:
# -Ter pelo menos 8 caracteres.
# -Incluir pelo menos uma letra maiúscula.
# -Incluir pelo menos um número.

senha = input("Digite sua senha: ")

caracteres = len(senha) >= 8 #verifica a quantidade de caracter
maiuscula = any(c.isupper() for c in senha) #verifica se tem pelo menos uma maiscula
num = any(c.isdigit() for c in senha)#verifica se tem pelo menos um numero

if caracteres and maiuscula and num:
    print("Senha válida!")
else:
    print("Senha inválida! Ela precisa:")
    if not caracteres:
        print("- Ter pelo menos 8 caracteres")
    if not maiuscula:
        print("- Incluir pelo menos uma letra maiúscula")
    if not num:
        print("- Incluir pelo menos um número")