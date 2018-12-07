t=input()
for i in range(int(t)):
  array_len,cards=(map(int, input().split()))
  array_lvl=list(map(int, input().split()))
  array_lvl.sort()
  array_card=[]
  for i in range(len(array_lvl)):
    if i==(array_len-1):
      array_card.append(array_lvl[i]*2)
    else:
      array_card.append(array_lvl[i]*3)
  card_remove=array_card[::]
  card_remove[array_len-1]+=array_lvl[array_len-2]
  if cards<array_card[0]:
  	array_card=[]
  extra=sum(array_card)-cards
  while extra>0:
    for i in range(array_len):
      if card_remove[i]>=extra:
        array_lvl=array_lvl[:i]+array_lvl[i+1:]
        array_len-=1
        array_card=[]
        card_remove=[]
        for i in range(len(array_lvl)):
      	  if i==(array_len-1):
        	  array_card.append(array_lvl[i]*2)
      	  else:
        		array_card.append(array_lvl[i]*3)
        card_remove=array_card[::]
        card_remove[array_len-1]+=array_lvl[array_len-2]
        extra=sum(array_card)-cards
        break
    if extra<=0:
    	break
    else:
      j=card_remove.index(max(card_remove))
      array_lvl=array_lvl[:j]+array_lvl[j+1:]
      array_len-=1
      array_card=[]
      card_remove=[]
      for i in range(len(array_lvl)):
      	if i==(array_len-1):
        	array_card.append(array_lvl[i]*2)
      	else:
        	array_card.append(array_lvl[i]*3)
      card_remove=array_card[::]
      card_remove[array_len-1]+=array_lvl[array_len-2]
      extra=sum(array_card)-cards
  if array_card:
  	print(sum(array_card))
  	print(array_card)
  else:
  	print(0) 

