nome_cad = input("Cadastre seu nome: ")
senha_cad = int(input("Cadastre sua senha: "))
print("Login")
login_nome = input("Nome:")
login_senha= int(input("Senha:"))

"""if not b > a:
    print(f'{b}(b) não é maior que {a}(a)')
else:
    print(f'{b}(b) é maior que {a}(a)')"""

'''if not a:
    print("a não tem valor")'''

"""if 'jo'in nome:
    print(f"Acesso liberado {nome}")
else:
    print(f'{nome} você não está cadastrado, acesso negado!')"""

if nome_cad == login_nome and senha_cad == login_senha:
    print("Login Efetuado com Sucesso!")

else:
    print("Usuário ou Senha inválidos!")

