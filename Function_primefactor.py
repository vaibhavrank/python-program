def get_prime_factors(n, divisor=2, factors=None):
    if factors is None:
        factors = []  # Initialize factors list on first call

    if n < 2:  # Base case: if number is less than 2, no prime factors
        return factors

    if n % divisor == 0:  # Check if divisor is a factor of n
        factors.append(divisor)
        return get_prime_factors(n // divisor, divisor, factors)  # Recursive call

    else:
        return get_prime_factors(n, divisor + 1, factors)  # Try next divisor


# Example usage:
n = int(input("Enter a positive integer: "))  # Input from user
prime_factors = get_prime_factors(n)
print("Prime factors of", n, "are:", prime_factors)
