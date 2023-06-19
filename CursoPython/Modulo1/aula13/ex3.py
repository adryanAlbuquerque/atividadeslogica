num = input("Digite a hora atual: ")

if not num.isdigit():
    print(f"{num} não é um numero inteiro!")

else:
    num = int(num)
    if num >= 0 and num <= 11:
        print(f"Bom dia!")
    elif num >= 12 and num <= 17:
        print("Boa tarde!")
    elif num >=18 and num <=23:
        print("Boa noite!")
    else:
        print("invalido!")