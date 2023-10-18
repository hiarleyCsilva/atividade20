# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM
import random


# Gera um número aleatório entre 0 e 5
numero_aleatorio = random.randint(0, 5)

# Solicita que o usuário adivinhe o número
try:
    numero_usuario = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))
except ValueError:
    print("Por favor, insira um número válido.")
    exit()

# Verifica se o número do usuário está correto
if numero_usuario == numero_aleatorio:
    print("Parabéns! Você acertou o número.")
else:
    print(f"Desculpe, o número correto era {numero_aleatorio}. Você perdeu.")
