n = int(input("Digite quantos números da sequência de Fibonacci você deseja gerar: "))
fibonacci = []

if n >= 1:
    fibonacci.append(0)
if n >= 2:
    fibonacci.append(1)

for i in range(2, n):
    next = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next)

print("Os primeiros"+ str(n) + "números da sequência de Fibonacci são: "+str(fibonacci))

