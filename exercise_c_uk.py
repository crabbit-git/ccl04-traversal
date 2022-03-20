united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
# This can be done directly by index because the dataset is transparent, but this may not always be the case:
# united_kingdom[1]["capital"] = "Cardiff"
# A more adaptible method might be something like this:
for country in united_kingdom:
  if country["name"] == "Wales":
    country["capital"] = "Cardiff"
print(f"The capital of {united_kingdom[1]['name']} is {united_kingdom[1]['capital']}")

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
united_kingdom.append(
  {
    "name":"Northern Ireland",
    "population":1811000,
    "capital":"Belfast"
  }
)
# If you want to make sure it worked, you could uncomment this:
# print(united_kingdom)

# 3. Use a loop to print the names of all the countries in the UK.
print("\nThe United Kingdom of Great Britain and Northern Ireland consists of the following countries:")
for country in united_kingdom:
  print(country["name"])

# 4. Use a loop to find the total population of the UK.
total_pop = 0
for country in united_kingdom:
  total_pop += country["population"]
print(f"\nThe total population of the UK amounts to approximately {total_pop} people")

# 5. Use a loop to find the country with the highest population and print out its capital.
# I would think the easiest way to do this with the tools I know of in Python so far is to start with the first list item in a variable
# and compare it to the rest, replacing it if the next list item has a larger population.
busiest_country = united_kingdom[0]
for country in united_kingdom:
  if country["population"] > busiest_country["population"]:
    busiest_country = country
print(f"\n{busiest_country['name']} is the most populous country in the UK")