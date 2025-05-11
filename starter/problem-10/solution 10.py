data_list = [13, 24, 'Karim', {'name': 'guru'}, 45, 17]

def clean_data():
    cleaned_list = [item for item in data_list if isinstance(item, (int, float))]
    return cleaned_list

cleaned_data = clean_data()
print(cleaned_data)
