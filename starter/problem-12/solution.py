list1 = [3, 5, 7, 4, 8, 8]
list2 = [4, 9, 8, 7, 1, 1, 13]

def sum_of_common_items(list1, list2):
    common_items = set(list1) & set(list2)
    total_sum = sum(common_items)
    return total_sum

result = sum_of_common_items(list1, list2)
print(f"The sum of common items is: {result}")
