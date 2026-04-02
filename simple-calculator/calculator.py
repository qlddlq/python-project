def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        
        if choice == '5':
            print("Thank you for using the calculator!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"{x} + {y} = {add(x, y)}")
                elif choice == '2':
                    print(f"{x} - {y} = {subtract(x, y)}")
                elif choice == '3':
                    print(f"{x} * {y} = {multiply(x, y)}")
                elif choice == '4':
                    print(f"{x} / {y} = {divide(x, y)}")
            except ValueError:
                print("Invalid input. Please enter numbers.")
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    calculator()