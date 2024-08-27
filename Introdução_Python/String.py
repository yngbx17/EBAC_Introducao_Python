#definição

nome = "Diego de Souza"
print(nome)
print(type(nome))

nome_vazio = ""
print(nome_vazio)
print(type(nome_vazio))

#concatenação
nome = "Diego"
sobrenome = "de Souza"
apresentação = "Olá meu nome é " + nome + ' ' + sobrenome + '.'
print(apresentação)

#formatação
nome = 'Diego'
sobrenome = 'de Souza'
apresentação = f'Olá meu nome é {nome} {sobrenome}.'
print(apresentação)

#fatiamento
email = 'diego.souza@gmail.com'
print('0: ' + email[0])
print('11: ' + email[11])
print('-1: ' + email[-1])
print('-2: ' + email[-2])

#intervalo
email_usuario = email[0:11]
print(email_usuario)

email_provedor = email[12:21]
print(email_provedor)

#métodos 
endereço = 'Praça Roberto Gomes Pedrosa, 1 - Morumbi, São Paulo, Brasil'

#upper()
print(endereço.upper())

#find()
posicao = endereço.find('Brasil')
print(posicao)

#replace()
print(endereço.replace('Praça', 'Pça'))

#conversão

idade = 10
print(type(idade))

idade = str(idade)
print(type(idade))

faturamento = 'R$ 35 MI'
print(faturamento)
print(type(str))

faturamento = int(faturamento[3:5])
print(faturamento)
print(type(faturamento))