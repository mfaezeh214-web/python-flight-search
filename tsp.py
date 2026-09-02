import itertools

cities = input("enter the name of the cities by space: ").split()
start_city = input("enter the start city: ")

distances = {}
print("enter the distances:")
for i, c1 in enumerate(cities):                                       # شماره اندیس و شهر اول
    for c2 in cities[i+1:]:                                           # فقط شهرهای بعدی در لیست
        d = float(input(f"distance {c1}-{c2}: "))
        distances[(c1, c2)] = d
        distances[(c2, c1)] = d

other_cities = [x for x in cities if x != start_city]

best_cost = None
best_path = []

for i in itertools.permutations(other_cities):
    path = [start_city] + list(i) + [start_city]

    cost = 0
    for i in range(len(path)-1):                                      # فاصله بین شهرهای متوالی
        cost += distances[(path[i], path[i+1])]

    if best_cost is None or cost < best_cost:
        best_cost = cost
        best_path = [path]
    elif cost == best_cost:
        best_path.append(path)

print("---------------------------------")
print("best cost: ", best_cost)
print("best path: ")
for i in best_path:
    print(" -> ".join(i))
