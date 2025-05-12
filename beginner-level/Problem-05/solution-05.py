# Flatten a Nested List

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

if __name__ == "__main__":
    nested_list = [1, [2, 3], [4, [5]]]
    print(f"Flattened List: {flatten(nested_list)}")