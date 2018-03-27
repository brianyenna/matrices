class matrix(object):
    def __init__(self, num_rows, num_columns):
        '''
        num_rows: type = int
        num_columns: type = int

        num_rows is the number of rows in the matrix
        num_columsn is the number of columns in the matrix

        matrix_obj is initialised to all zeros
        '''
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.matrix_obj = {i:[0 for j in range(num_columns)] for i in range(num_rows)}

    def __repr__(self):
        return 'matrix({},{})'.format(self.num_rows, self.num_columns)

    def print_matrix(self):
        print('\n')
        for i in range(self.num_rows):
            for j in range(self.num_columns):
                print(self.matrix_obj[i][j], end = ' ')
            print('\n')
        print('\n')

    def get_num_rows(self):
        return self.num_rows

    def get_num_columns(self):
        return self.num_columns

    def add_col_to_matrix(self, col, col_index):
        '''
        col: type = list, or any other iterable
        col_index: type = int

        col_index is the column number, 0 <= col_index <= n-1 (from left to right)
        '''
        assert col_index < self.num_columns, 'col_index not in matrix'
        assert len(col) == self.num_rows, 'column length is incorrect'
        for i in range(len(col)):
            self.matrix_obj[i][col_index] = col[i]

    def add_row_to_matrix(self, row, row_index):
        '''
        row: type = list, or any other iterable
        row_index: type = int

        row_index is the column number, 0 <= col_index <= m-1 (top to bottom)
        '''
        assert row_index < self.num_rows, 'row_index not in matrix'
        assert len(row) == self.num_columns, 'row length is incorrect'
        self.matrix_obj[row_index] = row

    def get_row(self, row_index):
        '''
        Returns a list
        '''
        assert row_index < self.num_rows, 'row_index not in matrix'
        return self.matrix_obj[row_index]

    def get_column(self, col_index):
        '''
        Returns a list
        '''
        assert col_index < self.num_columns, 'col_index not in matrix'
        ans = []
        for i in self.matrix_obj:
            ans.append(self.matrix_obj[i][col_index])
        return ans


    def __mul__(self, other):
        '''
        Multiplies the matrix object with another matrix object.

        Returns a new matrix object
        '''
        assert self.num_columns == other.num_rows, 'matrices are of incompatible dimensions'

        ##Not sure whether this would be a potential problem. Maybe you have to write matrices.matrix???
        ans = matrix(self.num_rows, other.num_columns)

        for i in range(self.num_rows):
            temp_row = self.get_row(i)
            for j in range(other.num_columns):
                temp_column = other.get_column(j)
                count = 0
                for num in range(self.num_columns):
                    count += temp_row[num]*temp_column[num]
                ans.matrix_obj[i][j] = count
        return ans

    def __pow__(self, other):
        '''
        Does element-wise multiplication with another matrix object

        Returns a new matrix object
        '''
        assert self.num_columns == other.num_columns, 'matrices are of incompatible dimensions'
        assert self.num_rows == other.num_rows, 'matrices are of incompatible dimensions'


        ans = matrix(self.num_rows, other.num_columns)

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                ans.matrix_obj[i][j] = self.matrix_obj[i][j] * other.matrix_obj[i][j]

        return ans

    def __add__(self, other):
        '''
        Returns a new matrix object
        '''
        assert self.num_columns == other.num_columns, 'matrices are of incompatible dimensions'
        assert self.num_rows == other.num_rows, 'matrices are of incompatible dimensions'

        ans = matrix(self.num_rows, other.num_columns)

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                ans.matrix_obj[i][j] = self.matrix_obj[i][j] + other.matrix_obj[i][j]

        return ans

    def __sub__(self, other):
        '''
        Returns a new matrix object
        '''
        assert self.num_columns == other.num_columns, 'matrices are of incompatible dimensions'
        assert self.num_rows == other.num_rows, 'matrices are of incompatible dimensions'

        ans = matrix(self.num_rows, other.num_columns)

        for i in range(self.num_rows):
            for j in range(self.num_columns):
                ans.matrix_obj[i][j] = self.matrix_obj[i][j] - other.matrix_obj[i][j]

        return ans



# a = matrix(3,3)
# a.add_row_to_matrix([1,1,3], 0)
# a.add_row_to_matrix([2,2,2], 1)
# a.add_row_to_matrix([3,3,1], 2)
# a.print_matrix()
# b = matrix(3,3)
# b.add_col_to_matrix([1,0,1],0)
# b.add_col_to_matrix([2,0,1],1)
# b.add_col_to_matrix([3,1,2],2)
# b.print_matrix()
# # b.add_col_to_matrix([3,1,2],3)
# # b.add_col_to_matrix([3,1,3],4)
# c = a-b
# c.print_matrix()
# # # print(a.get_row(2))
# # # print(a.get_column(1))
# # a.print_matrix()
