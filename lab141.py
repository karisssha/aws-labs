def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Display and store prime numbers
prime_numbers = [str(num) for num in range(1, 251) if is_prime(num)]

with open('results.txt', 'w') as file:
    file.write('\n'.join(prime_numbers))

print("Prime numbers between 1 to 250 have been saved in results.txt.")
