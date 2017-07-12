# https://mingrammer.com/introduce-comprehension-of-python
# List test
no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
print(no_primes)

# Set test
no_primes = {j for i in range(2, 9) for j in range(i * 2, 50, i)}
print(no_primes)
