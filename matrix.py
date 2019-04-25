"""LOGIC:
1. Read number grid from textfile by row and a list of lists
2. Sum the values in each sub-list and append
3. Sort by summed values
For column sorting:
1. Create new list sorting by column values
"""
import operator

def read_matrix(filename):
    """ loads a text file of a grid of integers and creates a list of lists
    of integers representing the matrix. matrix[r][c] is the element on
    row #r and column #c """
    with open(filename, 'r') as input_file:
        return [[int(column) for column in row.split()] for row in input_file]
        
def return_matrix():
        matrix = read_matrix('testmatrix0.txt')
        #Loop through each sub-list
        col_sum1 = 0
        col_sum2 = 0
        col_sum3 = 0
        col_sum4 = 0
        for x in range(len(matrix)):
                row_sum = 0
                #Loop through sub-list elements and sum
                #Append to a different list dependant on index position
                for i in range(len(matrix[x])):
                        row_sum += matrix[x][i]
                        #Col list creation
                        if x == 0 and i == 0:
                                col_sum1 += matrix[x][i]
                                sublist1 = [matrix[x][i]]
                        elif x == 0 and i == 1:
                                col_sum2 += matrix[x][i]
                                sublist2 = [matrix[x][i]]
                        elif x == 0 and i == 2:
                                col_sum3 += matrix[x][i]
                                sublist3 = [matrix[x][i]]
                        elif x == 0 and i == 3:
                                col_sum4 += matrix[x][i]
                                sublist4 = [matrix[x][i]]
                        elif x > 0 and i == 0:
                                col_sum1 += matrix[x][i]
                                sublist1.append(matrix[x][i])
                        elif x > 0 and i == 1:
                                col_sum2 += matrix[x][i]
                                sublist2.append(matrix[x][i])
                        elif x > 0 and i == 2:
                                col_sum3 += matrix[x][i]
                                sublist3.append(matrix[x][i])
                        elif x > 0 and i == 3:
                                col_sum4 += matrix[x][i]
                                sublist4.append(matrix[x][i])                
                matrix[x].append(row_sum)        
        
        #Sort by 5th element in list, ie. sum
        matrix.sort(key = operator.itemgetter(4))
        #Output
        for x in range(len(matrix)):
                print(matrix[x][0], matrix[x][1], matrix[x][2], matrix[x][3]) 

        sublist1.append(col_sum1)
        sublist2.append(col_sum2)
        sublist3.append(col_sum3)
        sublist4.append(col_sum4)
        
        col_matrix = [sublist1,sublist2,sublist3,sublist4]
        col_matrix.sort(key = operator.itemgetter(3))
        col_row1 = []
        col_row2 = []
        col_row3 = []
        
        for x in range(len(col_matrix)):
                #Loop through sub-list elements and output [0][0],[1][0],[2][0],[3][0], then
                #[0][1],[1][1],[2][1],[3][1] 
                for i in range(len(col_matrix[x])-1):
                        if i == 0:
                                col_row1.append(col_matrix[x][i])
                        elif i == 1:
                                col_row2.append(col_matrix[x][i])
                        elif i == 2:
                                col_row3.append(col_matrix[x][i])                         
        
        print(col_row1)
        print(col_row2)
        print(col_row3)
        
return_matrix()