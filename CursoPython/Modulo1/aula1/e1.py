num = input("Digite a primeira nota: ")
num2 = input(("Digite a segunda nota: "))


if num.isdigit() and num2.isdigit():
    media = (num + num2) / 2
    print(f"Sua média é = {media}")

else:
    print("Formato inválido!")