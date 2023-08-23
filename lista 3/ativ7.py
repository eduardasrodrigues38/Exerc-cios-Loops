n = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1

if n < 0:
    print("O fatorial não está definido para números negativos.")
elif n == 0:
    print("O fatorial de 0 é 1.")
else:
    for i in range(1, n + 1):
        fatorial *= i

    print("O fatorial de "+str(n)+ " é "+str(fatorial) )
