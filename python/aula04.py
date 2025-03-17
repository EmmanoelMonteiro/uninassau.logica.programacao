# Entendendo operadores e estruturas de controle (IF/ELSE)
################################################

# 1. Verificação de Número Positivo ou Negativo
'''
 > Descrição: Escreva um programa que receba um número 
 e verifique se ele é positivo, negativo ou zero.
 > Exemplo de Entrada: -5
 > Exemplo de Saída: O número -5 é negativo.
'''

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print("O número é zero.")

# 2. Verificação de Par ou Ímpar
'''
 > Descrição: Escreva um programa que receba um número 
 e verifique se ele é par ou ímpar.
 > Exemplo de Entrada: 7
 > Exemplo de Saída: O número 7 é ímpar.
'''

# 3. Calculadora Simples
'''
 > Descrição: Escreva um programa que receba dois números 
 e uma operação matemática (+, -, *, /), execute a operação
 e exiba o resultado.
 > Exemplo de Entrada: 5, 3, *
 > Exemplo de Saída: 5 * 3 = 15
'''

# 4. Verificação de Senha
'''
> Descrição: Escreva um programa que peça ao usuário 
para digitar uma senha e verifique se ela está correta.
> Senha Correta: python123
> Exemplo de Entrada: python123
> Exemplo de Saída: Senha correta!
'''