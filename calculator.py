class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        
        return a - b
        
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    
    def divide(self, a, b):
        """Divide two numbers safely."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Raise a number to a power."""
        return a ** b
