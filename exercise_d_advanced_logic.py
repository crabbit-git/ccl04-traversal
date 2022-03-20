# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
print([number for number in numbers if number % 2 == 0])

# 2. Print the difference between the largest and smallest value:
print(max(numbers) - min(numbers))

# 3. Print True if the list contains a 2 next to a 2 somewhere.
# for number in numbers:
#     if number == 2 and numbers.index((number - 1)) == 2:
#         print(True)
has_consecutive = False
index = 0
for number in numbers:
    if number == 2 and numbers[index - 1] == 2:
        has_consecutive = True
    index += 1
if has_consecutive == True:
    print(has_consecutive)

# 4. Print out a list containing only the prime numbers.
prime_only = []
for number in numbers:
    prime = True
    for int in range(2, number):
        if (number % int) == 0:
            prime = False
    if prime:
        prime_only.append(number)
print(prime_only)

# 5. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
total = 0
exclude = False
for number in numbers: 
    if number == 6:
        exclude = True
    elif exclude:
        if number == 7:
            exclude = False
    else:
        total += number
print(total)

# 6. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.
superstition = []
total = 0
index = 0
for number in numbers:
    if number == 13 or numbers[index - 1] == 13:
        superstition.append(number)
    index += 1
    if number not in superstition:
        total += number
print(total)
# There's probably a better way to do this, but I made a list of the numbers to exclude, then incremented a running total for each number in the
# main list if the numbers in the main list were not found in the exlusion list.