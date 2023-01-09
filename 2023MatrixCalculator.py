# Subtraction
# Multiplication

repeater = True

while repeater is True:
    print("What do you want to do? ")
    print("1 Generate ")
    print("2 Addition ")
    print("3 Subtraction ")
    print("4 Multiplication ")
    choiceOperation = input()

    # generate
    if choiceOperation == "1":
        rows = int(input("Give the number of rows:"))
        columns = int(input("Give the number of columns:"))
        print("Input number and press enter for every entry.")

        # initialize matrix
        matrix = []
        for row in range(rows):  # loop for row
            a = []  # empty list
            for col in range(columns):  # loop for column
                a.append(int(input()))  # add user input to list
            matrix.append(a)

        # print matrix
        for row in range(rows):
            for col in range(columns):
                print(matrix[row][col], end=" ")
            print()
        print()

        # repeater
        repeatCalculation = input("Do you want to do solve something else? YES or NO")
        if repeatCalculation == "NO":
            repeater = False
        else:
            repeater = True

    # addition
    if choiceOperation == "2":
        matrixSize = (input("Does both matrix have the same size? Input 'YES' or 'NO'"))

        if matrixSize == "YES":
            rows = int(input("Give the number of rows:"))
            columns = int(input("Give the number of columns:"))
            print("Input number and press enter for every entry.")
            matrix1 = [[int(input()) for col in range(columns)] for row in range(rows)]
            print("Input number and press enter for every entry.")
            matrix2 = [[int(input()) for col in range(columns)] for row in range(rows)]

            # print matrices
            # print matrix 1
            print("Matrix 1:")
            for row in matrix1:
                print(row)

            # print matrix 2
            print("Matrix 2:")
            for row in matrix2:
                print(row)

            matrixAnswer = [[0 for col in range(columns)] for row in
                            range(rows)]  # Creates an empty array to store the answer, acts like a placeholder
            print("When both matrices are added, the answer is:")

            # add and print matrices
            for row in range(rows):
                for col in range(columns):
                    matrixAnswer[row][col] = matrix1[row][col] + matrix2[row][col]
            for i in matrixAnswer:
                print(i)
        if matrixSize == "NO":
            print("Sorry, it is not possible to add matrix with different size")

        # repeater
        repeatCalculation = input("Do you want to do solve something else? YES or NO")
        if repeatCalculation == "NO":
            repeater = False
        else:
            repeater = True

    # Subtraction
    if choiceOperation == "3":
        matrixSize = (input("Does both matrix have the same size? Input 'YES' or 'NO'"))

        if matrixSize == "YES":
            rows = int(input("Give the number of rows:"))
            columns = int(input("Give the number of columns:"))
            print("Input number and press enter for every entry.")
            matrix1 = [[int(input()) for col in range(columns)] for row in range(rows)]
            print("Input number and press enter for every entry.")
            matrix2 = [[int(input()) for col in range(columns)] for row in range(rows)]

            # print matrices
            # print matrix 1
            print("Matrix 1:")
            for row in matrix1:
                print(row)

            # print matrix 2
            print("Matrix 2:")
            for row in matrix2:
                print(row)

            matrixAnswer = [[0 for col in range(columns)] for row in
                            range(rows)]  # Creates an empty array to store the answer, acts like a placeholder
            print("When both matrices are subtracted, the answer is:")

            # add and print matrices
            for row in range(rows):
                for col in range(columns):
                    matrixAnswer[row][col] = matrix1[row][col] - matrix2[row][col]
            for i in matrixAnswer:
                print(i)
        if matrixSize == "NO":
            print("Sorry, it is not possible to subtract matrix with different size")

        # repeater
        repeatCalculation = input("Do you want to do solve something else? YES or NO")
        if repeatCalculation == "NO":
            repeater = False
        else:
            repeater = True

    # multiplication
    if choiceOperation == "4":
        # matrix 1 user input
        rows1 = int(input("Give the number of rows in matrix 1:"))
        columns1 = int(input("Give the number of columns in matrix 1:"))
        print("Input number and press enter for every entry.")
        matrix1 = [[int(input()) for col in range(columns1)] for row in range(rows1)]

        # matrix 2 user input
        rows2 = int(input("Give the number of rows in matrix 2:"))
        columns2 = int(input("Give the number of columns in matrix 2:"))

        # if it is impossible to multiply
        if columns1 != rows2:
            print("Sorry, it is not possible to multiply these matrices")
            # repeater
            repeatCalculation = input("Do you want to do solve something else? YES or NO")
            if repeatCalculation == "NO":
                repeater = False
            else:
                repeater = True

        else:
            print("Input number and press enter for every entry.")
            matrix2 = [[int(input()) for col in range(columns2)] for row in range(rows2)]

            # Creates an empty array to store the answer, acts like a placeholder
            matrixAnswer = [[0 for col in range(columns2)] for row in
                            range(rows1)]

            # multiply
            for x in range(len(matrix1)):
                for y in range(len(matrix2[0])):
                    for z in range(len(matrix2)):
                        matrixAnswer[x][y] += matrix1[x][z] * matrix2[z][y]
            # result
            # print matrices
            # print matrix 1
            print("Matrix 1:")
            for row in matrix1:
                print(row)

            # print matrix 2
            print("Matrix 2:")
            for row in matrix2:
                print(row)

            print("When both matrices are multiplied, the answer is:")
            for row in matrixAnswer:
                print(row)

            # repeater
            repeatCalculation = input("Do you want to do solve something else? YES or NO")
            if repeatCalculation == "NO":
                repeater = False
            else:
                repeater = True
