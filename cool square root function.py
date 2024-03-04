def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def primeFactorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def sqrt(n):
    if n < 0:
        n = abs(n)
        answer = sqrt(n)
        return f"{answer}i"
    if n == 0 or n == 1:
        return str(n)
    
    factors = primeFactorization(n)
    outside_sqrt = 1
    inside_sqrt = 1
    unique_factors = set(factors)
    
    for factor in unique_factors:
        count = factors.count(factor)
        outside_sqrt *= factor ** (count // 2)
        if count % 2 != 0:
            inside_sqrt *= factor
            
    if inside_sqrt == 1:
        return str(outside_sqrt)
    else:
        if outside_sqrt == 1:
            return f"sqrt({inside_sqrt})"
        else:
            return f"{outside_sqrt} * sqrt({inside_sqrt})"

def main():
    while True:
        x = input("Enter a number (or 'exit' to quit): ")
        if x.lower() == 'exit':
            break
        try:
            x = float(x)
            print(sqrt(x))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

main()