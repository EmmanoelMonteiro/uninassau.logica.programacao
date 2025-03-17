#5. Manipulação de Texto
#-------------------------------------------------------
'''
Strings em Python podem ser manipuladas de várias formas, 
como concatenação, fatiamento e formatação.
'''
############################################################
#A)	Concatenação de strings:
############################################################
'''
nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print(nome_completo)
'''

############################################################
#B)	Fatiamento de strings:
############################################################
'''
texto = "Python é incrível"
print(texto[0:6])  # Saída: "Python"
print(texto[10:18])  # Saída: "incrível"
'''

############################################################
#C)	Formatação de strings (f-strings):
############################################################
'''
nome = "Carlos"
idade = 30
mensagem = f"{nome} tem {idade} anos."
print(mensagem)
'''
