def greedy_knapsack_01(weights, values, W):
    n = len(weights)
    vpw_list = [(values[i] / weights[i], i) for i in range(n)]         # list: value per wight
    vpw_list.sort(key=lambda x: x[0], reverse=True)

    total_value = 0
    remaining_capacity = W
    taken_items = []                                                   # اندیس آیتم های انتخاب شده

    for vpw, i in vpw_list:                                            # بررسی آیتم های سورت شده
        if weights[i] <= remaining_capacity:
            taken_items.append(i)
            total_value += values[i]
            remaining_capacity -= weights[i]
    return total_value, taken_items

n = int(input("enter the number of items: "))
weights = []
values = []

for i in range(n):
    w = int(input(f"item weight {i+1}: "))
    v = int(input(f"item value {i+1}: "))
    weights.append(w)
    values.append(v)

W = int(input("enter the knapsack capacity: "))

max_value, selected_items = greedy_knapsack_01(weights, values, W)     # فراخوانی مسیله

print("most value: ", max_value)
print("chosen items: ", [i+1 for i in selected_items])
