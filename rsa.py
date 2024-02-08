import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def pollard_rho(n):
    x = 2
    y = 2
    d = 1
    f = lambda x: (x**2 + 1) % n
    while d == 1:
        x = f(x)
        y = f(f(y))
        d = gcd(abs(x - y), n)
    return d

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        if n == 1:
            break
        if n % 2 == 0:
            factors.append(2)
            n //= 2
        else:
            factor = pollard_rho(n)
            factors.append(factor)
            n //= factor
    return factors

def main(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()

    for number in numbers:
        n = int(number)
        factor_list = factorize(n)
        print(f"{n}={'*'.join(map(str, factor_list))}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    input_file = sys.argv[1]
    main(input_file)
