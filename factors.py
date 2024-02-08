import sys

def factorize(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append((i, n//i))
            n //= i
    if n > 1:
        factors.append((n, 1))
    return factors

def main(input_file):
    with open(input_file, 'r') as f:
        numbers = f.readlines()
    
    for number in numbers:
        n = int(number)
        factor_pairs = factorize(n)
        for pair in factor_pairs:
            print(f"{n}={pair[0]}*{pair[1]}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    input_file = sys.argv[1]
    main(input_file)
