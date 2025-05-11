list_1 = [4, 9, 8, 7, 5, 2, 13]

def sort_and_subtract(lst):
    lst.sort(reverse=True)
    max_val = lst[0]
    min_val = lst[-1]
    subtraction = max_val - min_val
    return lst, subtraction

sorted_list, subtraction_result = sort_and_subtract(list_1)
print("Sorted list in descending order:", sorted_list)
print("Subtraction of max and min:", subtraction_result)
