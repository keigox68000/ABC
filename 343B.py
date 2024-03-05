N = int(input())
x,y = N,N
matrix = []

for i in range(x):
    row_input = input()
    row = [int(num) for num in row_input.split()]
    matrix.append(row)

for row in matrix:
    a = ""
    for element_index, element in enumerate(row):
        if element == 1:
            a += str(element_index + 1) + " "
    print(a)