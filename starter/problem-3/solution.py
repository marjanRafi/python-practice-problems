# Function to find the elder brother
def find_eldest(age1, age2):
    if age1 > age2:
        return "Brother 1 is the elder."
    elif age2 > age1:
        return "Brother 2 is the elder."
    else:
        return "Both brothers are of the same age."

# Test the function with two ages
age_of_brother1 = 25
age_of_brother2 = 22

# Call the function and print the result
result = find_eldest(age_of_brother1, age_of_brother2)
print(result)
