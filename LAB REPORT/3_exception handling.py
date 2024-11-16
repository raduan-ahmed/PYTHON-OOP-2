# Divide Elements Function

def divide_elements(values, divisor):
    try:
        # Check if divisor is numeric
        if not isinstance(divisor, (int, float)):
            raise TypeError("Divisor must be a numeric type.")
        
        # Process each value in the list
        results = []
        for value in values:
            try:
                result = value / divisor
                results.append(result)
            except ZeroDivisionError:
                print(f"Error: Cannot divide {value} by zero.")
                results.append(None)  # Append None for division by zero
        return results
    except TypeError as e:
        print(f"Error: {e}")

# Example usage
values = [10, 20, 30, 40]
divisor = 0  # Change this to test different scenarios
output = divide_elements(values, divisor)
print(output)
