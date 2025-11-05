def sort_dicts_manual(data, key):
    """
    Manual implementation to sort list of dictionaries by key
    Uses bubble sort algorithm
    """
    # Your manual implementation here
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][key] > data[j+1][key]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

# Test data
test_data = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 20}
]

# Test the function
sorted_data = sort_dicts_manual(test_data.copy(), 'age')
print("Manual sort result:", sorted_data)