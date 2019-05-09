n = int(input())
words = []

for i in range(2*n - 2):
    temp = input()
    words.append([-len(temp),temp,i])

words.sort()

flag = True
curr = words[0][1]

# print(words)

for i in range(2,len(words),2):
    if words[i][1] == curr[:n - i//2 - 1] or words[i+1][1] == curr[:n - i//2 - 1]:
        continue
    else:
        flag = False
        break

if flag and words[0][1][1:] == words[1][1][:-1] :
    word = words[0][1] + words[1][1][-1]
    words[0].append("P")
    words[1].append("S")
else:
    word = words[1][1] + words[0][1][-1]
    words[0].append("S")
    words[1].append("P")


# print(word)

for i in range(2,len(words),2):
    if words[i][1] == word[:n - i//2 - 1]:
        words[i].append("P")
        words[i+1].append("S")
    else:
        words[i].append("S")
        words[i+1].append("P")

answer = ["" for _ in range(2*n - 2)]

for i in words:
    answer[i[2]] = i[3]

print("".join(answer))