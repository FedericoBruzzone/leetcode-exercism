class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [[int(el) for el in row.split()] for row in matrix_string.split("\n")] 
        print(self.matrix)

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [i[index-1] for i in self.matrix]

    def __str__(self):
        head = ' ' * 3 + '{:^3}' * len(self.matrix[0]) + '\n' + \
               ' ' * 2 + '|' + '-' *len(self.matrix[0]) * 3 + '\n'
        body = '{:<2}|' + '{:^3}' * len(self.matrix[0]) + '\n'
        template = head + body * len(self.matrix)

        x = [[i] + row for i, row in enumerate(self.matrix, 1)]
        res = template.format(*range(1, len(self.matrix[0])+1), *[j for i in x for j in i])
        return res
