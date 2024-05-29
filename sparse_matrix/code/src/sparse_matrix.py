class SparseMatrix:
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = {}

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        numRows = int(lines[0].split('=')[1].strip())
        numCols = int(lines[1].split('=')[1].strip())
        matrix = cls(numRows, numCols)

        for line in lines[2:]:
            if not line.strip():
                continue
            try:
                row, col, value = map(int, line.strip(' ()\n').split(','))
                matrix.setElement(row, col, value)
            except ValueError:
                raise ValueError("Input file has wrong format")

        return matrix

    def getElement(self, row, col):
        return self.elements.get((row, col), 0)

    def setElement(self, row, col, value):
        if value != 0:
            self.elements[(row, col)] = value
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def __add__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(self.numRows, self.numCols)
        all_keys = set(self.elements.keys()).union(other.elements.keys())
        for key in all_keys:
            result.setElement(key[0], key[1], self.getElement(key[0], key[1]) + other.getElement(key[0], key[1]))
        return result

    def __sub__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(self.numRows, self.numCols)
        all_keys = set(self.elements.keys()).union(other.elements.keys())
        for key in all_keys:
            result.setElement(key[0], key[1], self.getElement(key[0], key[1]) - other.getElement(key[0], key[1]))
        return result

    def __mul__(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix A's columns must equal Matrix B's rows for multiplication")
        result = SparseMatrix(self.numRows, other.numCols)
        for (i, k), v in self.elements.items():
            for j in range(other.numCols):
                result.setElement(i, j, result.getElement(i, j) + v * other.getElement(k, j))
        return result

def select_operation():
    print("Select matrix operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter choice (1/2/3): ")
    return int(choice)

def main():
    file1 = input("Enter the path to the first matrix file: ")
    file2 = input("Enter the path to the second matrix file: ")
    output_file = input("Enter the path to the output file: ")

    matrix1 = SparseMatrix.from_file(file1)
    matrix2 = SparseMatrix.from_file(file2)

    operation = select_operation()

    if operation == 1:
        result = matrix1 + matrix2
    elif operation == 2:
        result = matrix1 - matrix2
    elif operation == 3:
        result = matrix1 * matrix2
    else:
        print("Invalid choice")
        return

    with open(output_file, 'w') as f:
        for (row, col), value in result.elements.items():
            f.write(f"({row}, {col}, {value})\n")

if __name__ == "__main__":
    main()
