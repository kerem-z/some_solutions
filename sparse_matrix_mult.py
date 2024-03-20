def sparse_matrix_multiplication(matrix_a, matrix_b):
    """
    Multiplies two sparse matrices represented as 2D lists and returns the result.

    Parameters:
    matrix_a (list of list of int/float): The first matrix to multiply.
    matrix_b (list of list of int/float): The second matrix to multiply.

    Returns:
    list of list of int/float: The resulting matrix of the multiplication.
    """
    # Check if the number of columns in A matches the number of rows in B
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Matrix A's column count must match Matrix B's row count.")

    # Convert matrices to sparse representation
    sparse_a = get_dict_non_zero_cells(matrix_a)
    sparse_b = get_dict_non_zero_cells(matrix_b)

    # Initialize the result matrix with zeros
    matrix_c = [[0 for _ in range(len(matrix_b[0]))] for _ in range(len(matrix_a))]

    # Perform sparse matrix multiplication
    for (i, k), a_val in sparse_a.items():
        for j in range(len(matrix_b[0])):
            if (k, j) in sparse_b:
                matrix_c[i][j] += a_val * sparse_b[(k, j)]

    return matrix_c

def get_dict_non_zero_cells(matrix):
    """
    Converts a matrix into a sparse representation using a dictionary.

    Parameters:
    matrix (list of list of int/float): The matrix to convert.

    Returns:
    dict: A dictionary where the keys are tuples of (row, column) indices,
          and the values are the non-zero elements of the matrix.
    """
    dict_of_non_zero_cells = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:
                dict_of_non_zero_cells[(i, j)] = matrix[i][j]
    return dict_of_non_zero_cells

