dict1 = {'age': 13, 'id': 12, 'address': 'Banani', 'course': 'Python'}
dict2 = {'address': 'Rupnagar', 'id': 25, 'course': 'MERN'}

def common_items_by_keys(dict1, dict2):
    common_keys = dict1.keys() & dict2.keys()
    common_items = {}
    
    for key in common_keys:
        common_items[key] = (dict1[key], dict2[key])
    
    return common_items

result = common_items_by_keys(dict1, dict2)
print("Common items based on keys:")
print(result)
