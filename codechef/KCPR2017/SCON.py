t=input()
for i in range(int(t)):
  rows,columns=(map(int, input().split()))
  field=[]
  for i in range(rows):
  	c=list(map(int, input().split()))
  	field.append(c)
  maxstep_field=[[0 for x in range(columns)] for y in range(rows)] 
  for i in range(rows):
  	for j in range(columns):
  		if i==0 and j==0:
  			maxstep_field[i][j]=field[i][j]
  		elif i==0:
  			maxstep_field[i][j]=maxstep_field[i][j-1]+field[i][j]
  		elif j==0:
  			maxstep_field[i][j]=maxstep_field[i-1][j]+field[i][j]
  		else:
  			maxstep_field[i][j]=max(maxstep_field[i][j-1],maxstep_field[i-1][j])+field[i][j]
  print(maxstep_field[rows-1][columns-1]) 