

   import math

class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Division by zero is not allowed"

    def solve_quadratic(self, a, b, c):
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root,
        else:
            return "No real roots"

# Create an instance of the Calculator class
calculator = Calculator()

# Example usage:
result_addition = calculator.add(5, 3)
result_subtraction = calculator.subtract(10, 4)
result_multiply = calculator.multiply(7, 2)
result_division = calculator.divide(6, 2)
result_quadratic = calculator.solve_quadratic(1, -3, 2)

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiply)
print("Division:", result_division)
print("Quadratic Roots:", result_quadratic)