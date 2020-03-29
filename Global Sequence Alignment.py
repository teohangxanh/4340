import pandas as pd

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
                    
    # trace_back = [[len(result)-1, len(result[0])-1]]
    # # Priotity in diagonal, then left
    # for row in range(len(result)-1, 0, -1):
    #     for col in range(row - abs(len(str1) - len(str2)), -1, -1):
    #         current = result[row][col]
    #         diag = result[row-1][col-1]
    #         if current == diag + match or current == diag + mismatch:
    #             trace_back.append([row-1, col-1])
    #             print(result[row-1][col-1])
    #         else:
    #             left = result[row][col-1]
    #             if current  == left + gap:
    #                 trace_back.append([row, col-1])
    #                 print(result[row][col-1])
    #             else:
    #                 trace_back.append([row-1, col])
    #                 print(result[row-1][col])
    #         break
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