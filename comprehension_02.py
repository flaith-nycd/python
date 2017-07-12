# Get the percent of a list of values from their sum
vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)  # 545

percent = [x / amount * 100 for x in vals]
print(percent)

total_percent = sum(percent)
print(total_percent)

# no_primes = [j for i in range(2, 9) for j in range(i * 2, 50, i)]
no_primes = []
for i in range(2, 9):
    for j in range(i * 2, 50, i):
        no_primes.append(j)

print(no_primes)
