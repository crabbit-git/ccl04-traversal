# We can put anything inside a list. Even another list!

letters = [
  ["a", "b", "c"],
  ["d", "e"],
  ["g", "h", "i"]
]

# # When accessing elements in a nested array by index, you will get back another list
# first_row = letters[0]
# print(first_row)

# # You can then access the indivial elements within that row by index
# a = first_row[0]
# print(f"first_row[0] = {a}")

# # You can do this in a single step using the following syntax:
# d = letters[1][0]
# print(f"letters[1][0] = {d}")

# h = letters[2][1]
# print(f"letters[2][1] = {h}")

# # We can loop over elements in nested arrays using a nested for loop
# for row in letters:
#   print(f"Currently looking at row {row}")
#   for letter in row:
#     print(f"Currently looking at letter {letter} of row {row}")



# 1. Add an additional row for j, k and l
letters.append(
  ["j", "k", "l"]
)

# 2. Add the letter f to the second row
letters[1].append("f")

# 3. Using loops, print out an uppercase version of every letter
for row in letters:
  for letter in row:
    print(letter.upper())

# 4. Using loops, print out the whole row every time you see a vowel
#    Python doesn't have a built-in function for checking vowels. You might want to Google this if you can't think of a way to do it.
vowels = ["a", "e", "i", "o", "u"]

print("Rows containing vowels:")
for row in letters:
  for letter in row:
    if letter in vowels:
      print(row)
  
# 5. Using loops, print out only the rows that do not contain any vowels
print("Rows without vowels:")
rows_with_vowels = []
for row in letters:
  for letter in row:
    if letter in vowels:
      rows_with_vowels.append(row)
  if row not in rows_with_vowels:
    print(row)