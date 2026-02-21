def greet(name):
    return f"Hello, {name}!"

def validate_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")

def add(a, b):
    validate_numbers(a, b)
    return a + b

def subtract(a, b):
    validate_numbers(a, b)
    return a - b

def multiply(a, b):
    validate_numbers(a, b)
    return a * b

def divide(a, b):
    validate_numbers(a, b)
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator():
    print("\nSimple Calculator")
    print("Operations: +  -  *  /")
    
    while True:
        try:
            op = input("\nEnter operation (+, -, *, /) or 'q' to quit: ")
            if op.lower() == 'q':
                print("Exiting calculator.")
                break
            
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if op == '+':
                print("Result:", add(a, b))
            elif op == '-':
                print("Result:", subtract(a, b))
            elif op == '*':
                print("Result:", multiply(a, b))
            elif op == '/':
                print("Result:", divide(a, b))
            else:
                print("Invalid operation.")
        
        except ValueError as e:
            print("Error:", e)

def main():
    print(greet("GitHub Tester"))
    
    try:
        print("2 + 3 =", add(2, 3))
        print("2 - 1 =", subtract(2, 1))
        print("2 * 3 =", multiply(2, 3))
        print("6 / 2 =", divide(6, 2))
        print("2 + 'a' =", add(2, "a"))  # This will raise error
    except ValueError as e:
        print("Error:", e)
    
    calculator()

if __name__ == "__main__":
    main()
