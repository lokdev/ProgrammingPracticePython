#Coloured Loops
#Given m x n matrix filled with chars
#determine if the matrix has a loop or not
#example:
# A A A A
# A B B A
# A B A A
# A A A B
# since the loop is formed with all the A's the answer is true
#
# example:
# A A A A
# A B C A
# A A A A
# true
#
#example:
# A A A A
# A B C A
# A B A A
# false
#
# definition of a loop: it starts and begins at the same point
class ColoredLoop(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def isValid(self, row, col, letter, temp):
        if(row >= 0 and col >= 0):
            if(row < len(temp) and col < len(temp[0])):
                if(self.matrix[row][col] == letter and temp[row][col] == 0):
                    return True
        return False

    def findLoop(self, row, col, letter, temp):
        #return condition
        if(temp[row][col] == 1):
            return True
        temp[row][col] == 1
        #it doesn't matter what direction you came from as long as you don't go back to same spot you came from
        #up
        if(self.isValid(row-1, col, letter, temp)):
            self.findLoop(row-1, col, letter, temp)
        #down
        if(self.isValid(row+1, col, letter, temp)):
            self.findLoop(row+1, col, letter, temp)
        #left
        if(self.isValid(row, col-1, letter, temp)):
            self.findLoop(row, col-1, letter, temp)
        #right
        if(self.isValid(row, col+1, letter, temp)):
            self.findLoop(row, col+1, letter, temp)

    def logic(self):
        temp = [[0 for col in range(len(matrix[0]))] for row in range(len(matrix))]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[0])):
                if(self.findLoop(row, col, self.matrix[row][col], temp)):
                    return True
        return False



#Main
matrix1 = [
    ['A', 'A', 'A', 'A'],
    ['A', 'B', 'B', 'A'],
    ['A', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'B']
]
matrix2 = [
    [ 'A', 'A', 'A', 'A'],
    [ 'A', 'B', 'C', 'A'],
    [ 'A', 'B', 'A', 'A']
]
matrix3 = [
    ['A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'B', 'A', 'B', 'A'],
    ['A', 'B', 'A', 'A', 'A', 'B', 'A'],
    ['A', 'B', 'B', 'B', 'B', 'B', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'B', 'A']
]
obj = ColoredLoop(matrix1)
obj.logic()
