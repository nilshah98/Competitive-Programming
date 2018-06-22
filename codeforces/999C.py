from collections import Counter
n,k = map(int, input().split())
word = input()

keys = sorted(list(set(list(word))))
freq = Counter(word)
complete = set()
partial = []
for i in keys:
    k -= freq[i]
    if k >= 0:
        complete.add(i)
    else:
        partial.append(i)
        k += freq[i]
        break
ans = []
for i in word:
    if i not in complete:
        if i in partial:
            if k>0:
                k-=1
            else:
                ans.append(i)
        else:
            ans.append(i)
print("".join(ans))
