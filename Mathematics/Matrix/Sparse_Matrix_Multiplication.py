class Solution:
    # the naive solution to this is essentially doing linear algebra
    # time complexity O(n^3), space complexity O(1)
    # technically O(a_row * a_col * b_col)
    def multiply(self, A, B):
        a_row = len(A)
        a_col = len(A[0])
        b_col = len(B[0])

        res = [[0] * b_col for i in range(a_row)]

        for i in range(a_row):
            for j in range(b_col):
                for k in range(a_col):
                    res[i][j] += A[i][k]*B[k][j]

        return res

    # optimized solution
    # worse case, time complexity remains at O(n^3) but it will perform better when there are zeroes

    def multiply_optimized(self, A, B):
        a_row = len(A)
        a_col = len(A[0])
        b_col = len(B[0])

        res = [[0] * b_col for i in range(a_row)]

        for i in range(a_row):
            for j in range(a_col):
                if A[i][j] != 0:
                    for k in range(b_col):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j]*B[j][k]

        return res

    # time complexity remains at O(n^3) but interviewer is likely to look for this solution
    # this creates sparse matrices
    def multiply_sparse(self, A, B):
        a_row = len(A)
        b_col = len(B[0])

        res = [[0]*b_col for i in range(a_row)]

        sparse_A = self.sparse_matrices(A)
        sparse_B = self.sparse_matrices(B)

        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    res[i][y] += val_A * val_B
        return res

    def sparse_matrices(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        res = []

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    continue
                res.append((i, j, matrix[i][j]))

        return res


if __name__ == '__main__':
    A = [[1, 0, 0], [-1, 0, 3]]
    B = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
    # Solution().multiply(A, B)
    # Solution().multiply_sparse(A, B)
    print(Solution().multiply_sparse(A, B))
