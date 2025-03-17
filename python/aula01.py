# Declaração de Variáveis Primitivas
#-------------------------------------------------------
'''
Variáveis são usadas para armazenar dados. Em Python, 
não é necessário declarar o tipo da variável explicitamente.
'''
########################################################
### A)	Números inteiros e decimais:
########################################################
'''
idade = 25  # Inteiro
altura = 1.75  # Decimal (float)

print("A idade é: ", idade)
print("A altura é: ", altura)
'''
########################################################
### B) Texto (strings):
########################################################
'''
nome = "João"
mensagem = 'Seja bem-vindo'

print(mensagem, nome)
'''

# 3. Leitura de Dados com input()
#-------------------------------------------------------
'''
O comando input() permite ler dados digitados pelo usuário.
'''
########################################################
### A) Ler um nome:
########################################################
'''
nome = input("Digite seu nome: ")

print("Olá,", nome)
'''
########################################################
### B) Ler um número:
########################################################
'''
idade = int(input("Digite sua idade: "))  # Converte o input para inteiro

print("Você tem", idade, "anos.")
'''
