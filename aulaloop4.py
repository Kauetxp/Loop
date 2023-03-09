tentativas = 3

while tentativas >=1:
    senha = "poipoi123"
    tentasenha = str(input("Digite a senha: "))
    
    if tentasenha == senha:
        print("Acesso concedido!")
        break
    else:
        print("Senha incorreta, tente novamente.")
        tentativas-=1
        print("Restam",tentativas,"tentativas.")
else:
    print("Núméro de tentativas excedido!")
    