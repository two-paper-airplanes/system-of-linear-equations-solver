# trying out a MA1522 challenge on creating a "solver" to reduce matrices to REF and RREF (gauss jordan method)
import numpy as np

input_matrix = input()
input_matrix = input_matrix[1:-1]
temp = input_matrix.split("; ")
working_matrix = []
for row in temp:
    new_row = row.split(', ')
    working_matrix.append(new_row)

#convert all strings to floats
for i in range(len(working_matrix)):
    for j in range(len(working_matrix[i])):
        working_matrix[i][j] = float(working_matrix[i][j])

# sort rows in descending first number order
working_matrix.sort(key=lambda row: row[0], reverse=True)

# ensure first row first column is non-zero and then find multiple of all other first numbers w the first row
if working_matrix[0][0] != 0:
    for row in working_matrix[1:]:
        multiple = row[0] / working_matrix[0][0]
        for i in range(len(row)):
            row[i] -= multiple * working_matrix[0][i]
else:
    working_matrix.sort(key=lambda row: row[1], reverse=True)

# make first leading entry 1
if working_matrix[0][0] != 0:
    multiple = 1 / working_matrix[0][0]
    for i in range(len(working_matrix[0])):
        working_matrix[0][i] *= multiple

# sort the remaining rows in descending order of the second column
working_matrix[1:].sort(key=lambda row: row[1], reverse=True)

# use a loop to go thru the same steps for all the remaining rows
for i in range(1, len(working_matrix)):
    # ensure the leading entry is non-zero and then find multiple of all other first numbers w the first row
    if working_matrix[i][i] != 0:
        for row in working_matrix[i + 1:]:
            multiple = row[i] / working_matrix[i][i]
            for j in range(len(row)):
                row[j] -= multiple * working_matrix[i][j]
    else:
        working_matrix[i:].sort(key=lambda row: row[i + 1], reverse=True)

    # make leading entry 1
    if working_matrix[i][i] != 0:
        multiple = 1 / working_matrix[i][i]
        for j in range(len(working_matrix[i])):
            working_matrix[i][j] *= multiple

    # sort the remaining rows in descending order of the next column
    working_matrix[i + 1:].sort(key=lambda row: row[i + 1], reverse=True)

print(working_matrix)