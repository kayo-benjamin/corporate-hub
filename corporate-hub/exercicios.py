# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else 
# para determinar se o número é par ou ímpar.
# numero = int(input("Digite um número: "))
# if numero % 2 == 0:
#     print(f"{numero} é par.")
# else:
#     print(f"{numero}é ímpar.")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
# para classificar a idade em categorias de acordo com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# idade = int(input("Qual a sua idade? "))

# if idade <= 12:
#     print('Criança: 0 a 12 anos.')
# elif idade <= 18:
#     print('Adolescente: 13 a 18 anos.')
# else:
#     print('Adulto: acima de 18 anos.')


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar 
# se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# usuario = input('Digite seu usuario: ')
# senha = input('Digite sua senha: ')
# user = 'admin'
# password = 'adm192'
# if usuario == user and senha == password:
#     print('Bem vindo!')
# else:
#     print('Usuario ou Senha incorretos!')


# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura 
# if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de 
# acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# x = float(input("Qual o valor de x? "))
# y = float(input("Qual o valor de y? "))

# if x > 0 and y > 0:
#     print("Primeiro Quadrante.")
# elif x < 0 and y > 0:
#     print("Segundo Quadrante.")
# elif x < 0 and y < 0:
#     print("Terceiro Quadrante.")
# elif x > 0 and y < 0:
#     print("Quarto Quadrante.")  
# else:
#     print("Ponto do eixo ou origem.")
    
    
# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# numeros = [1,2,3,4,5,6,7,8,9,10]
# nomes = ['João', 'Maria', 'Pedro', 'Ana']
# nascimento_e_atual = [2004, 2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num:
#     print(i)

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# soma = 0
# for i in range(1, 11, 2):
#     soma += 1
# print(soma)
        

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# for i in range(10, 0, -1):
#     print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir 
# a tabuada desse número, indo de 1 a 10.

# tab = int(input("Informe qual tabuada você quer? "))
# for i in range(1, 11):
#     print(f"{tab} x {i} = {tab * i}")
    

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
# Utilize um bloco try-except para lidar com possíveis exceções.
#num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#soma = 0
# try:
#     for i in num:
#         soma += i
#         print(soma)
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. 
# Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
# lista_valores = [15, 20, 25, 30]
# soma_valores = 0

# try:
#     for valor in lista_valores:
#         soma_valores += valor
#     media = soma_valores / len(lista_valores)
#     print(f"Média dos valores: {media}")
# except ZeroDivisionError:
#     print("A lista está vazia, não é possível calcular a média.")
# except Exception as e:
#     print(f"Ocorreu um erro: {e}")

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
info = [{"nome": 'Kayo', "idade": 20, "cidade": 'Ribeirão Preto'}]

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
info('idade') = 22

# Adicione um campo de profissão para essa pessoa;
info['profissão'] = 'Desenvolvedor'
# Remova um item do dicionário.
del info['cidade']
# 3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.
quad = {x: x**2 for x in range(1,6)}
print(quad)
# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.
dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'Minas'}
if 'nome' in dicionario:
    print('A chave existe no dicionário')
else:
    print('A chave nao existe no dicionario')
# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.
    frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)