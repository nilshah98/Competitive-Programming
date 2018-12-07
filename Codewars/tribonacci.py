def tribonacci(signature,n):
    if len(signature)>n and n>0:
        answer=[]
        for i in range(n):
            answer.append(signature[i])
        return answer
    elif n==0:
        return []
    while len(signature)<4 and len(signature)<n:
        signature.append(sum(signature))
    while len(signature)<n:
        signature.append(sum(signature[:len(signature)-4:-1]))
    return signature