stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

# I've commented out everything apart from the last task, but just uncomment the bits you want to run/check.

# #1. Add "Edinburgh Waverley" to the end of the list
# stops.append("Edinburgh Waverley")
# print(stops)

# #2. Add "Glasgow Queen St" to the start of the list
# stops.insert(0, "Glasgow Queen Street")
# print(stops)

# #3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
# stops.insert(4, "Polmont")
# print(stops)

# #4. Print out the index position of "Linlithgow"
# print(stops.index("Linlithgow"))

# #5. Remove "Livingston" from the list using its name
# stops.remove("Livingston")
# print(stops)

# #6. Delete "Cumbernauld" from the list by index
# stops.pop(2)
# print(stops)

# #7. Print the number of stops there are in the list
# print(len(stops))

# #8. Sort the list alphabetically
# stops.sort()
# print(stops)

# #9. Reverse the positions of the stops in the list
# stops.sort(reverse=True)
# print(stops)

# #10 Print out all the stops using a for loop
# for stop in stops:
#     print(stop)


# #11. Print out only the stops that begin with the letter L using a for loop
# for stop in stops:
#     if stop.startswith("L"):
#         print(stop)

#12. Remove all stops that begin with the letter C using a for loop
cless_stops = []
for stop in stops:
    if stop.startswith("C") == False:
        cless_stops.append(stop)

stops = cless_stops
print(stops)