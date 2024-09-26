grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# Loop through each column (y-coordinates)
for y in range(len(grid[0])):  # There are 6 columns
    for x in range(len(grid)):  # There are 9 rows
        print(grid[x][y], end='')  # Print the character without newline
    print()  # Print a newline after each column is printed
