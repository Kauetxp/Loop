tipo = input("Digite o tipo de número que deseja imprimir (Par ou Impar): ")
for i in range(1,11):
    tipo = tipo.upper()
    if tipo == "PAR" and i%2==0:
        print(i)
    elif tipo == "IMPAR" and i%2!=0:
        print(i)
        
        