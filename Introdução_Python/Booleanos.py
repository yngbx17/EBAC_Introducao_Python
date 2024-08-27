#definição

verdadeiro = True
falso = False

print(verdadeiro)
print(falso)

#> (maior)
#< (menor)
#== (igual)
#>= (maior ou igual)
#<= (menor ou igual)
#!= (diferente)


saldo = 200
saque = 100

pode_sacar = saque<= saldo
print(pode_sacar) # True

codigo = '852'
codigo_cadastro = '010'

pode_pagar = codigo == codigo_cadastro
print(pode_pagar) # False

#Operações (| & or not)

print(True|True)
print(True|False)
print(False|False)
print(False|True)

print(True & True)
print(True & False)
print(False & False)
print(False & True)

print( not True)
print( not False)

#conversão

idade = 20
tipo_sangue = '0-'
filhos = 0
telefone_fixo = None
telefone_fixo = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo)) # False
print(bool(telefone_fixo)) # False
