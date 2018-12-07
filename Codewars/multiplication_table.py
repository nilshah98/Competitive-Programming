def multiplication_table(row,col):
    answer=[]
    for i in range(1, row+1):
        row=[]
        for j in range(1, col+1):
            row.append(i*j)
        answer.append(row)
    return answer