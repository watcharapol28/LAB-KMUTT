def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        #print(n,i)
        if n % i == 0:
            return False
    return True


def next_prime(N):
    if N + 1 == 2 :
        return 2

    if N % 2 == 0:
        N += 1
    else:
        N += 2
    while(True):
        if is_prime(N):
            return N
        N += 2
    return N


def next_twin_prime(N):
    if N % 2 == 0:
        N += 1
    else:
        N += 2
    while(True):
        if is_prime(N) and is_prime(N + 2):
            return (N, N+2)
        N += 2


exec(input().strip())