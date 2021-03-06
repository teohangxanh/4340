import pandas as pd

'''
Author: Ted Dang
Date created: 03/30/2020
Usage: Returns the matrix representing Global Sequence Alignment and 
       its trace back positions
'''
def gsa(str1, str2, match, mismatch, gap):
    result = [[0 for i in range((len(str1) + 1))] for j in range(len(str2) + 1)]
    for row in range(len(result)):
        for col in range(len(result[row])):
            if row == 0:
                result[row][col] = col * gap
            else:
                if col == 0:
                    result[row][col] = row * gap
                else:
                    left = result[row][col-1] + gap
                    up = result[row-1][col] + gap
                    diag = result[row-1][col-1] 
                    if str1[col-1] == str2[row-1]:
                        diag += match
                    elif str1[col-1] != str2[row-1]:
                        diag += mismatch
                    result[row][col] = max([left, up, diag])
                    
    trace_back = [[len(result)-1, len(result[0])-1]]
    # Priotity: up, diagonal, and left
    row = trace_back[-1][0]
    col = trace_back[-1][1]
    print('val', '[r,', 'col]')
    print(result[trace_back[-1][0]][trace_back[-1][1]], end = ' ')
    print(trace_back[-1])
    while row > 0:
        while col > 0:
            current = result[row][col]
            diag = result[row-1][col-1]
            up = result[row-1][col]
            if current == up + gap:
                trace_back.append([row-1, col])
            elif current == diag + match or current == diag + mismatch:
                trace_back.append([row-1, col-1])
                col -= 1
            else:
                trace_back.append([row, col-1])
                col -= 1
                row += 1
            print()
            print('val', '[r,', 'col]')
            print(result[trace_back[-1][0]][trace_back[-1][1]], end = ' ')
            print(trace_back[-1])
            break
        row -= 1
    # print(trace_back)
                    
    index = ['-']
    for i in str2:
        index.append(i)
    
    columns = ['-']
    for i in str1:
        columns.append(i)
    
    result = pd.DataFrame(result, index, columns)
    print(result)
 
'''
Author: Ted Dang
Date created: 03/30/2020
Usage: Returns the position of the max of the matrix
'''    
def max_pos(matrix):
    ans = matrix[0][0]
    row = 0
    col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if ans < matrix[i][j]:
                ans = matrix[i][j]
                row = i
                col = j
    return (row, col)

'''
Author: Ted Dang
Date created: 03/30/2020
Usage: Returns the matrix representing Local Sequence Alignment and 
       its trace back positions
'''
def lsa(str1, str2, match, mismatch, gap):
    result = [[0 for i in range((len(str1) + 1))] for j in range(len(str2) + 1)]
    for row in range(len(result)):
        for col in range(len(result[row])):
            if row != 0 and col != 0:
                left = max(result[row][col-1] + gap, 0)
                up = max(result[row-1][col] + gap, 0)
                diag = result[row-1][col-1] 
                if str1[col-1] == str2[row-1]:
                    diag += match
                elif str1[col-1] != str2[row-1]:
                    diag += mismatch
                result[row][col] = max([left, up, diag])
                    
    row_start, column_start = max_pos(result)
    trace_back = [[row_start, column_start]]
    # Priotity: up, diagonal, and left
    row = row_start
    col = column_start
    print('val', '[r,', 'col]')
    print(result[trace_back[-1][0]][trace_back[-1][1]], end = ' ')
    print(trace_back[-1])
    while row > 0:
        while col > 0:
            current = result[row][col]
            diag = result[row-1][col-1]
            up = result[row-1][col]
            if current == up + gap:
                trace_back.append([row-1, col])
            elif current == diag + match or current == diag + mismatch:
                trace_back.append([row-1, col-1])
                col -= 1
            else:
                trace_back.append([row, col-1])
                col -= 1
                row += 1
            print()
            print('val', '[r,', 'col]')
            print(result[trace_back[-1][0]][trace_back[-1][1]], end = ' ')
            print(trace_back[-1])
            break
        row -= 1
    # print(trace_back)
                    
    index = ['-']
    for i in str2:
        index.append(i)
    
    columns = ['-']
    for i in str1:
        columns.append(i)
    
    result = pd.DataFrame(result, index, columns)
    print(result)
    
    
a = 'acggctc'
b = 'atggcctc'
gsa(a, b, 1, -3, -4)