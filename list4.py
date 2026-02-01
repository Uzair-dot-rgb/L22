def find_and_filter_squares(start_num, end_num):
    """
    Calculates the squares of numbers in a given range, 
    then filters and prints the odd and even square values using lists.

    Args:
        start_num (int): The beginning of the range (inclusive).
        end_num (int): The end of the range (inclusive).
    """
    numbers = range(start_num, end_num + 1)
    
    squares = [num ** 2 for num in numbers]
    
    odd_squares = []
    even_squares = []
    
    for square in squares:
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
            
    print(f"Range of numbers: {list(numbers)}")
    print(f"Calculated squares: {squares}")
    print(f"Odd square values: {odd_squares}")
    print(f"Even square values: {even_squares}")

find_and_filter_squares(2, 7)
