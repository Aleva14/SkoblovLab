
class Matrix():
    def __init__(self, data):
        for row in data:
            if (not isinstance(row, list)) or (len(row) != len(data)):
                raise ValueError('Wrong argument')
        self.data = data

    def __len__(self):
        return len(self.data)

    def __add__(self, other):

        if len(other) != len(self):
            raise ValueError('Different dimensions')

        result = []
        for i in range(0, len(self)):
            result.append([self.data[i][j] + other.data[i][j] for j in range(0, len(self))])
        return Matrix(result)

    def transposed(self):
        result = [[] for i in range(0, len(self))]
        for i in range(0, len(self)):
           for j in range(0, len(self)):
               result[j].append(self.data[i][j])
        return Matrix(result)

    def line_product(self, a, b):
        result = 0
        for i in range(0, len(self)):
            result += a[i] * b[i]
        return result

    def __mul__(self, other):
        if type(other) == Matrix:
            a = self.data
            b = other.transposed().data
            result = []
            for i in range(0, len(self)):
                result.append([])
                for j in range(0, len(self)):
                    result[i].append(self.line_product(a[i], b[j]))
            return Matrix(result)


        result = Matrix(self.data)
        for i in range(0, len(self)):
            for j in range(0, len(self)):
                result.data[i][j] *= other
        return result

    def __repr__(self):
        s = ''
        for i in self.data:
            s += str(i) + '\n'
        return s



m1 = Matrix([[1, 2], [2, 1]])
m2 = Matrix(([[0, -1], [1, 0]]))
m3 = m1 + m2
print(m3.__repr__())
m3 = m3.transposed()
print (m3.__repr__())
m3 = m1 * m2
print(m3.__repr__())
m3 = m1 * 3
print(m3.__repr__())
