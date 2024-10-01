def printTable(tableData):
    
    # Determine the number of columns (same as the number of inner lists)
    numCols = len(tableData)
    
    # Find the longest string in each column and store its length in colWidths
    colWidths = [0] * numCols # Initialize a list to store the column widths
    
    for i in range(numCols):
        colWidths[i] = len(max(tableData[i], key=len)) # Get max length of each column
        
    # Transpose the table to make it easier to print row by row
    numRows = len(tableData[0])
    for row in range(numRows):
        for col in range(numCols):
            # Print the value right-justified with the width of the longest string in the column
            print(tableData[col][row].rjust(colWidths[col]), end=' ')
        print() # Print a newline at the end of each row
        
        
# Test the function with the provided table
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)