zoo = ("deer", "dog", "gorilla", "lion", "monkey")

print(zoo)
print("\n")

temp_animal = zoo.index("gorilla")
print("Gorilla is indexed at " + str(temp_animal) + " inside of zoo tuple.")
print("\n")

if "snake" in zoo:
  print(f'Snake is at position {str(zoo.index("snake"))} in zoo tuple.')
else:
  print(f'Snake is not in zoo tuple.')
print("\n")

if "monkey" in zoo:
  print(f'Monkey is at position {str(zoo.index("monkey"))} in zoo tuple.')
else:
  print(f'Monkey is not in zoo tuple.')
print("\n")

(deer, dog, middle, lion, last) = zoo
print("Middle variable", middle.title())
print("\n")
print("Last variable", last.upper())

zoo = list(zoo)
print("Zoo as list:", zoo)
print("\n")


zoo.append("snake")
zoo.append("horse")
zoo.append("goat")

print("Zoo after append:", zoo)
print("\n")


zoo = tuple(zoo)
print("Zoo as a tuple:", zoo)
print("\n")