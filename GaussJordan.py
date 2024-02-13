##########################################
# Gauss-Jordan elimination
# Returns the inverse of a square matrix, without altering it.
def invert(matrix):
    n = len(matrix)     # matrix is a list of rows.
    for row in matrix:
        if len(row) != n:
            raise Exception('Matrix is not square')

    # The work area will be two square matrices M & INV "side by side". 
     # INV starts as the identity matrix and ends as inverse of M, which ends as the identity matrix.
        
    M = [row[:] for row in matrix]  # Create a copy so that the calling script does not have its variable altered
    INV = [[float(i == j) for i in range(n)] for j in range(n)] # A simple way to create an identity matrix

    # Treat the rows with index i (i.e. have each row i as a pivot row in its turn).
    for i in range(n):
        max_abs = abs(M[i][i])  # find the maximal element in column i. 
        max_row = i             # the initial finding being in row i.
        for k in range(i+1, n):             # Continue search belo row i.
            if abs(M[k][i]) > max_abs:
                max_abs = abs(M[k][i])
                max_row = k
        if max_row != i:                                # If the initial finding changed,
            M[i], M[max_row] = M[max_row], M[i]            # swap rows to get the maximal on row i
            INV[i], INV[max_row] = INV[max_row], INV[i]    # do the same swap in the INV side.
        pivot = M[i][i]                                 # (Note: the real, not abs value, of course.)

        if pivot == 0:
            raise Exception('Matrix is singular and cannot be inverted')
        
        # Divide the pivot row with the pivot element, also in the INV.
        M[i][i] = 1             # =pivot/pivot
        for j in range(n):
            if j > i:           # On the left, the pivot row is zero.
                M[i][j] /= pivot
            INV[i][j] /= pivot 

        # Treat with index k the rows below and above row i, doing ...
        for k in range(n):                 # ... subtractions with the pivot M[i][i] that became 1.
            if k==i:
                continue            # k==i is for the pivot row which is already treated.

            c = M[k][i]         # Store this pivot column element before zeroing it,...
            M[k][i] = 0             # ... because it is the multiplier for other subtractions on row k.
            # Treat the remaining columns of M, index them with j.
            for j in range(i+1, n):
                M[k][j] -= c * M[i][j]
            # Treat the whole row k of INV, using column index j.
            for j in range(n):
                INV[k][j] -= c * INV[i][j]
    return INV