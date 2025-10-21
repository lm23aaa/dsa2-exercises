def powerset(s):
    if not s:
        return [[]]
    first = s[0]
    rest = powerset(s[1:])
    with_first = [[first] + r for r in rest]
    return rest + with_first

def knapsack_bruteforce(weight_capacity: int, items: list[tuple[str, int]]) -> tuple[list[tuple[str, int]], list[int]]:
    output_item_lists = []
    output_count_list = []

    for list in powerset(items):
        count = 0

        for item in list:
            (title, weight) = item
            count += weight

        if count <= weight_capacity and count > 0:
            output_item_lists.append(list)
            output_count_list.append(count)

    return (output_item_lists, output_count_list)

def knapsack(
    weight_capacity: int, 
    items: list[tuple[str, int]], 
    should_sort: bool = False, 
    should_reverse: bool = False
) -> tuple[int, list[str]]:
    count = 0
    inner_items = items.copy()
    if should_sort:
        inner_items = sorted(inner_items, key=lambda item: item[1])
    if should_reverse:
        inner_items.reverse()
    return_items = []

    for i in range(0, len(inner_items)):
        (title, weight) = inner_items[i]

        if count + weight < weight_capacity:
            count += weight
            return_items.append(title)
        else:
            continue

    return (count, return_items)


def fractional_knapsack(
    weight_capacity: float, 
    items: list[tuple[str, float, float, float]]
):
    count = 0.0
    inner_items = []
    return_items = []

    for item in items:
        inner_items.append((item[0], item[1], item[2], item[2] / item[1]))

    inner_items = sorted(inner_items, key=lambda item: item[3])
    inner_items.reverse()
    # print(inner_items)

    for item in inner_items:
        (title, weight, value, wv) = item

        if count + weight < weight_capacity:
            count += weight
            return_items.append((title, weight, value, 1))
        elif count + weight > weight_capacity and count < weight_capacity:
            current_target = weight_capacity - count
            percent = current_target / weight
            count += current_target
            return_items.append((title, weight * percent, value, percent))

    return (count, return_items)

# print(knapsack(18, [
#     ('sleepingbag', 5),
#     ('tent', 8),
#     ('food', 7),
#     ('water', 4),
#     ('stove', 11),
# ], False, False))

print(fractional_knapsack(
    25.0,
    [
        ('one', 7.0, 6.0),
        ('two', 9.0, 9.0),
        ('three', 10.0, 9.0),
        ('four', 22.0, 19.0),
    ]
))