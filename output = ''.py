# Define the height and width of the L shape
height = 5
width = 5

# Outer loop for rows
for i in range(height):
    # Inner loop for columns
    for j in range(width):
        # Print '*' for the first column and the last row
        # Print ' ' (space) for all other positions
        if j == 0 or i == height - 1:
            print('*', end='')
        else:
            print(' ', end='')
    # Move to the next line after each row is printed
    print()
