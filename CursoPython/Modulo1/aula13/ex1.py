num = input("Digite um numero inteiro: ")

if not num.isdigit():
    print(f"{num} não é numero não é inteiro!")

else:
    num = int(num)

    if num % 2 == 0:
        print(f"{num} é par!")
    else:
        print(f"{num} é impar!")