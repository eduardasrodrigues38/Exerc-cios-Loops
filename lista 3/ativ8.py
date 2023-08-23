def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for num in range(1, 51):
    if eh_primo(num):
        print(num)
