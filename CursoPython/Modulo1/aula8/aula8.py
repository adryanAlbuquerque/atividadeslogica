"""
Condições   IF - ELIF - ELSE
"""

nome = input("Qual seu nome? ")
idade = int(input("Quantos anos você tem? "))

if idade > 18:
    print(f"{nome} pode fazer um empréstimo!")

else:
    print(f"{nome} não pode fazer empréstimo pois é menor de idade!")