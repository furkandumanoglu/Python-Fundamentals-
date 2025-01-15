def linear_search_dictionary(my_dict, target_value):
    for key, value in my_dict.items():
        if value == target_value:  
            print(f"Found value at key '{key}'.")
            return key  
    print(f"Failure! Value not found in the dictionary.")
    return None
my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
print(linear_search_dictionary(my_dictionary, 5))  
print(linear_search_dictionary(my_dictionary, 3))  
print(linear_search_dictionary(my_dictionary, 8))  