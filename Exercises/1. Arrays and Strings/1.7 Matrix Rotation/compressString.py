
testcases = [
    
    [

        [1,2,3,4,5],
        [1,2,3,0,5],
        [1,2,3,4,5],
        [1,0,3,4,5],
        [1,0,3,4,5],
    ],
    [
        [0,2,3,4,5],
        [1,2,3,0,5],
        [1,2,3,4,5],
        [0,2,3,4,5],
        [1,0,3,4,5],
    ]

    
]


# function to compress tring
def ZeroMatrix(matrix):

    rowHasZero = False
    colHasZero = False

    #Check for zero in first row
    for j in range(0, len(matrix[0])):
        if(matrix[0][j] == 0):
            rowHasZero = True
            break

    #Check for zero in first col
    for i in range(0, len(matrix)):
        if(matrix[i][0] == 0):
            colHasZero = True
            break
    
    #check rest of the matrix for zeros and set values in first col and row
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            val = matrix[i][j]
            if(val == 0):
                matrix[i][0] = 0
                matrix[0][j] = 0

    nullifyRows(matrix)
    nullifyCols(matrix)

    if(rowHasZero):
        for j in range(0,len(matrix[i])):
            matrix[0][j] = 0

    if(colHasZero):
        for i in range(0,len(matrix)):
            matrix[i][0] = 0

    return matrix

    
def nullifyRows(matrix):
    for i in range(0, len(matrix)):
        if(matrix[i][0] == 0):
            for j in range(1,len(matrix[i])):
                matrix[i][j] = 0

def nullifyCols(matrix):
    for j in range(0, len(matrix[0])):
        if(matrix[0][j] == 0):
            for i in range(1,len(matrix)):
                matrix[i][j] = 0
        


def printMatrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=" ")
        print("")
    
    print("")

        


print("Zero matrix: ")
for t in testcases:
    print("Input: ") 
    printMatrix(t)   

    print("Output: ")
    printMatrix(ZeroMatrix(t))
    print("------------------------------ ")


