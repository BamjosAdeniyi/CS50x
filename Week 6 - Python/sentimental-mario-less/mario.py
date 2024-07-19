def print_space(height, row):
    """Print spaces for the given row"""
    print(' ' * (height - row), end='')

def print_hash(count):
    """Print hashes for the given count"""
    print('#' * count, end='')

def main():
    height = 0
    # To make sure the user's input is valid
    while height < 1 or height > 8:
        try:
            height = int(input("Height: "))
            if height >= 1 and height <= 8:
                break
        except ValueError:
            continue

    # Prompt the user for the height and build the pyramid
    for i in range(1, height + 1):
        print_space(height, i)
        print_hash(i)
        print()  # Move to the next line

main()

