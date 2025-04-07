##################################################
# 1: Repetições básicas (While e For)
##################################################
# A) Conta caracteres e imprime letras usando while
'''
palavra = input("Digite uma palavra: ")
contador = 0

print(f"\nA palavra '{palavra}' tem {len(palavra)} caracteres:")

while contador < len(palavra):
    print(contador, " - ",palavra[contador])
    contador =  contador + 1

'''

# B) Versão usando for para o mesmo problema
'''
palavra = input("Digite uma palavra: ")
print(f"\nA palavra '{palavra}' tem {len(palavra)} caracteres:")

for letra in palavra:
    print(letra.index)

'''

##################################################
# 2: Controle de fluxo no For (Demonstra break e continue)
##################################################

print("Números pares de 1 a 20 (para no 16):")

for num in range(1, 21):
    
    if num % 2 != 0: # Se for ímpar
        continue # Pula para próxima iteração

    if num > 16:
        break # Interrompe o loop
    
    print(num)

