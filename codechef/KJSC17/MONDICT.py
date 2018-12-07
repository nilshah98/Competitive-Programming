import itertools
t=input()
for i in range(int(t)):
  to_find=input()
  digits=sorted(list(to_find))
  total_outcomes=(list(itertools.permutations(digits, len(digits))))
  print(len(total_outcomes[total_outcomes.index(tuple(to_find))+1::])) 