maiornum = -9999999999
num = int(input("Entre com um número ou digite -1 para parar: "))
while num != -1:
    if num > maiornum:
        maiornum = num
    num = int(input("Entre com um número ou digite -1 para parar: "))
print("O maior número foi:",maiornum)
