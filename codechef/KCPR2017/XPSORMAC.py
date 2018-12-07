row_1=['q','w','e','r','t','y','u','i','o','p']
row_2=['a','s','d','f','g','h','j','k','l']
row_3=['z','x','c','v','b','n','m']
t=input()
for i in range(int(t)):
  no_words=input()
  words=list(map(str, input().split()))
  counter_1=0
  counter_2=0
  counter_3=0
  answer=[]
  for i in words:
    for j in i:
      if j.lower() in row_1:
        counter_1+=1
      elif j.lower() in row_2:
        counter_2+=1
      elif j.lower() in row_3:
        counter_3+=1
    if counter_1 == len(i) or counter_2 == len(i) or counter_3 == len(i):
      counter_1=0
      counter_2=0
      counter_3=0
    else:
      counter_1=0
      counter_2=0
      counter_3=0
      answer.append(i)
  print(len(answer))
  print(" ".join(answer))