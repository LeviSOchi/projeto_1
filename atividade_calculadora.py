# -*- coding: utf-8 -*-
"""atividade_calculadora.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XTzXP-i8yo974hhesXYy_Gv5acffZn2h
"""

nome = input("Qual o seu nome? ")
print(f"Olá {nome}, vamos começar!")

#aqui criamos um loop infinito
while True:
    print("Se não quiser mais, digite 0 para finalizar!")
    num1 = int(input("Digite um número: "))

    #verificamos imediatamente se ele é 0
    if num1 == 0:
        break

    #só pedimos o segundo número se o primeiro não for 0
    num2 = int(input("Digite outro número: "))

    #Operadores da calculadora
    adi = num1 + num2
    sub = num1 - num2
    mult = num1 * num2
    div = num1 / num2

    print(f"A soma dos dois números é: {adi}")
    print(f"A subtração dos dois números é: {sub}")
    print(f"A multiplicação dos dois números é: {mult}")
    print(f"A divisão dos dois números é: {div}")

print(f"Obrigado {nome}! Até a próxima")