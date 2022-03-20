users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "Fluffy",
      "species": "cat"
    },
    {
      "name": "Fido",
      "species": "dog"
    },
    {
      "name": "Spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "Nemo",
      "species": "fish"
    },
    {
      "name": "Kevin",
      "species": "fish"
    },
    {
      "name": "Spike",
      "species": "dog"
    },
    {
      "name": "Rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "Monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(f"\nJonathan's Twitter username is \"{users['Jonathan']['twitter']}\"")
# 2. Get Erik's hometown
print("\nErik's hometown is", users["Erik"]["home_town"])
# 3. Get the array of Erik's lottery numbers
print("\nErik's lottery numbers are...")
for number in users["Erik"]["lottery_numbers"]:
  print(number)
# 4. Get the species of Avril's pet Monty
for pet in users["Avril"]["pets"]:
  print(f"\nAvril has a pet {pet['species']} named {pet['name']}")
# 5. Get the smallest of Erik's lottery numbers
erik_lotto = sorted(users["Erik"]["lottery_numbers"])
print(f"\nThe lowest lottery number Erik has is {erik_lotto[0]}")
# 6. Return an array of Avril's lottery numbers that are even
print("\nAvril has the following even lottery numbers:")
even_avrils = [number for number in users["Avril"]["lottery_numbers"] if number % 2 == 0]
for number in even_avrils:
  print(number)
# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)
print("\nErik missed a \"7\". His lottery numbers should actually be...")
for number in users["Erik"]["lottery_numbers"]:
  print(number)
# 8. Change Erik's hometown to Edinburgh
print(f"\nAllegedly, Erik is from {users['Erik']['home_town']},")
users["Erik"]["home_town"] = "Edinburgh"
print(f"but he's actually from {users['Erik']['home_town']}.")
# 9. Add a pet dog to Erik called "Fluffy"
users["Erik"]["pets"].append(
  {
    "name":"Fluffy",
    "species":"dog"
  }
)
for pet in users["Erik"]["pets"]:
  if pet["name"] == "Fluffy":
    print(f"\nErik has a pet {pet['species']} named {pet['name']}")
# 10. Add another person to the users dictionary
users["Jim"] = {
  "twitter":"penguinboy",
  "lottery_numbers":[4, 7, 22, 1, 93, 15],
  "home_town":"Polbeth",
  "pets":[
  {
    "name":"Boab",
    "species":"goldfish"
  }
  ]
}
print("\nMeet Jim...")
print(f"Twitter username: {users['Jim']['twitter']}")
print(f"Lottery numbers: {users['Jim']['lottery_numbers']}")
print(f"Hometown: {users['Jim']['home_town']}")
print("Pets:")
for pet in users["Jim"]["pets"]:
  print(f"{pet['name']} the {pet['species']}")
# 11. Print a list of the numbers that appear in both Jonathon and Avril's lottery numbers
lotto_in_common = [number for number in users["Jonathan"]["lottery_numbers"] if number in users["Avril"]["lottery_numbers"]]
print(f"\nJonathon and Avril have the following lottery numbers in common:")
for number in lotto_in_common:
  print(number)
# 12. Print a list of the species of Erik's pets without duplicates
erik_pets = users["Erik"]["pets"]
erik_petspec = []
for pet in erik_pets:
  if pet["species"] not in erik_petspec:
    erik_petspec.append(pet["species"])
print("\nErik has the following as pets:")
for species in erik_petspec:
  print(species)