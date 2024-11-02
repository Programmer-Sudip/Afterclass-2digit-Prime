def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_two_digit_primes():
    """Find all two-digit prime numbers."""
    two_digit_primes = []
    for num in range(10, 100):
        if is_prime(num):
            two_digit_primes.append(num)
    return two_digit_primes

# Output the two-digit prime numbers
two_digit_primes = find_two_digit_primes()
print("Two-digit prime numbers:", two_digit_primes)

