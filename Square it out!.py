# Pre-made list of squared numbers
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(numbers)
# Separate odd and even squares
even_squares = [sq for sq in numbers if sq % 2 == 0]
odd_squares = [sq for sq in numbers if sq % 2 != 0]

# Print results
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
