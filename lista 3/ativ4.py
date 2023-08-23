quant=int(input("Digite quantos numeros voce quer na sua lista: "))
i=1 
par=0
impar=0
while i < quant+1:
    num=int(input("Digite o numero:  "))
    i += 1

    if num % 2 == 0:
        par= par +1      
    else:
        impar= impar +1
      
print("pares: "+str(par))
print("impares: "+str(impar))

