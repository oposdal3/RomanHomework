class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            self.cope = []
            for i in range(len(self.matrix)):
                cope = []
                for j in range(len(self.matrix[i])):
                    cope.append(self.matrix[i][j] + other.matrix[i][j])
                self.cope.append(cope)
            return Matrix(self.cope)
        else:
            return 'Данные матрицы не могут быть сложенны из-за разности их разрядов'

    def __str__(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end='\t')
            print()
        return ''


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[29, 38], [23, 7], [-1, -36]])
print(matrix1)
print(matrix1 + matrix2)
