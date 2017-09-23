class Matrix(object):
    def __init__(self,matrix = None):
        self._matrix = matrix
    
    def __iter__(self):
        return Matrix.MatrixIterator(self)
    
    def __str__(self):
        return str(self._matrix)
    
    class MatrixIterator(object):
        def __init__(self,host):
            # print("host = "+str(host)+" line 10")
            self._host = host
            self._length = len(host._matrix)
            self._index = 0

        def next(self):
            if self._index == self._length :
                raise StopIteration()
            result = self._host._matrix[self._index]
            self._index += 1
            # self._index %= self._length
            return result

