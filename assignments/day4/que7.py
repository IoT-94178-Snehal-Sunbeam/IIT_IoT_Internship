
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

def matrix_operations(list_matrix, tuple_matrix):
    addition_result = []
    subtraction_result = []

    for i in range(len(list_matrix)):
        add_row = []
        sub_row = []
        for j in range(len(list_matrix[0])):
            add_row.append(list_matrix[i][j] + tuple_matrix[i][j])
            sub_row.append(list_matrix[i][j] - tuple_matrix[i][j])
        addition_result.append(add_row)
        subtraction_result.append(sub_row)
    
    return addition_result, subtraction_result

add_matrix, sub_matrix = matrix_operations(matrix_list, matrix_tuple)

print("Addition of matrices:")
for row in add_matrix:
    print(row)

print("\nSubtraction of matrices:")
for row in sub_matrix:
    print(row)
