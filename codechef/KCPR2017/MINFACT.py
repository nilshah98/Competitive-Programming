import itertools
import functools
t=input()
for i in range(int(t)):
  digits=sorted(list(map(str, input().split())))
  total_outcomes=(list(itertools.permutations(digits, len(digits))))
  final=[]
  factors_list=[]
  for i in total_outcomes:
    number=''
    for j in i:
      number+=j
    final.append(number)
  for i in final:
    n=int(i)
    factors=len(set(functools.reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    factors_list.append(factors)
  print(int(final[factors_list.index(min(factors_list))])) 