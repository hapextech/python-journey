# Problem
# Given a matrix (a list containing rows of numbers), calculate and display the total of each row, the total of each column, and the average of each row.
# Examples
# Starting matrix: matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
# Row 1 total: 12 | Row 1 average: 4.0
# Row 2 total: 9 | Row 2 average: 3.0
# Row 3 total: 60 | Row 3 average: 20.0
# Column 1 total: 13
# Column 2 total: 27
# Column 3 total: 41

matrix = [[2, 4, 6],
           [1, 3, 5], 
           [10, 20, 30]]
def matrix(matrix):
    row_sum = []
    average = []
    for x in range(len(matrix)):
        sum = 0
        for row in matrix[x]:
            sum += row 
        row_sum.append(sum)
        avg = sum / len(matrix[x])
        average.append(avg)
    row1, row2, row3 = row_sum
    avg1, avg2, avg3 = average


    print(f"Row 1 total: {row1} | Row 1 average: {avg1}")
    print(f"Row 2 total: {row2} | Row 2 average: {avg2}")
    print(f"Row 3 total: {row3} | Row 3 average: {avg3}")
    col_sum = []
    for z in range(len(matrix[0])):
        colsum = 0
        for y in range(len(matrix)):
            colsum += matrix[y][z]
        col_sum.append(colsum)
    col1, col2, col3 = col_sum
    print(f"Column 1 total: {col1}")
    print(f"Column 2 total: {col2}")
    print(f"Column 3 total: {col3}")



matrix([[2, 4, 6], [1, 3, 5], [10, 20, 30]])