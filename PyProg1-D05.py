places = []


for i in range(1, 6):
    place = input(f"Enter the name of place {i}: ")
    places.append(place)


print("Places stored in list:", places)

result = ", ".join(p.upper() for p in places)

print("All places separated by comma and space and in uppercase:", result)