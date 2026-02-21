def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both inputs must be numbers.")
    return a + b

def main():
    print(greet("GitHub Tester"))
    
    try:
        print("2 + 3 =", add(2, 3))
        print("2 + 'a' =", add(2, "a"))  # This will raise error
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
