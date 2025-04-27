# String de entrada
texto = input("Digite um texto: ").lower()  # Converte para minúsculas

# Lista de vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Contador de vogais
contador = 0

# Percorre cada caractere do texto
for letra in texto:
    if letra in vogais:
        contador += 1

# Exibe o resultado
print(f"O texto tem {contador} vogais.")