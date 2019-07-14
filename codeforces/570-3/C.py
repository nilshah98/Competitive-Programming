q = int(raw_input())

for _ in range(q):
    k,n,a,b = map(int, raw_input().split())

    maxaTurn = max((k-a)//a,0)
    if (k-a)%a and (k)>a:
        maxaTurn += 1
    
    minbTurn = max((k - (maxaTurn*a) - b)//b,0)
    if (k - (maxaTurn*a) - b)%b and (k - (maxaTurn*a))>b:
        minbTurn += 1

    maxbTurn = max((k-b)//b,0)
    if (k-b)%b and (k)>b:
        maxbTurn += 1
    
    if maxbTurn < n:
        print(-1)
    elif maxaTurn + minbTurn >= n:
        print(min(n,maxaTurn))
    else:
        #Binary search on aTurns
        ll = 0
        rl = maxaTurn

        while( rl >= ll ):
            mid = ll + ((rl - ll)//2)

            bTurn = max((k - (mid*a) - b)//b,0)
            if (k - (mid*a) - b)%b and (k - (mid*a))>b:
                bTurn += 1

            # print(ll,rl,mid)

            if mid + bTurn >= n:
                ll = mid + 1
            elif mid + bTurn < n:
                rl = mid - 1

        print(min(n,rl))
        # print(ll,rl)
    '''
    Issues-
    1. -1//2 = -1
    2. If the number of turns satisfied for some value, it still means A can be made better, do not break
    '''