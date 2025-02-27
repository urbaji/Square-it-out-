def filter_square_values(numbers):
    odd_squares = []
    even_squares = []

    for num in numbers:
        square = num ** 2
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    print("Odd squares:", odd_squares)
    print("Even squares:", even_squares)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
filter_square_values(numbers)