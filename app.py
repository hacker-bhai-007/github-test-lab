def greet(name):
    return f"Hello, {name}!"

def validate_numbers_list(numbers):
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("All elements in the list must be numbers.")

def sum_list(numbers):
    validate_numbers_list(numbers)
    return sum(numbers)

def product_list(numbers):
    validate_numbers_list(numbers)
    product = 1
    for n in numbers:
        product *= n
    return product

def max_list(numbers):
    validate_numbers_list(numbers)
    return max(numbers)

def min_list(numbers):
    validate_numbers_list(numbers)
    return min(numbers)

def main():
    print(greet("GitHub Tester"))
    
    numbers = [2, 3, 5, 7]
    
    try:
        print("Numbers:", numbers)
        print("Sum:", sum_list(numbers))
        print("Product:", product_list(numbers))
        print("Maximum:", max_list(numbers))
        print("Minimum:", min_list(numbers))
        
        # This will raise error
        print("Sum with invalid input:", sum_list([2, 'a', 3]))
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
