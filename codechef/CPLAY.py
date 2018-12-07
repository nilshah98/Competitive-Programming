while True:
	try:
		penalties=raw_input()
		teamA=0
		teamB=0
		flag=False
		reqshots=0
		for i in range(10):
			if(i%2):
				if penalties[i]=="1":
					teamB+=1
			else:
				if penalties[i]=="1":
					teamA+=1


			if teamA > teamB:
				if (teamB + (9-i)/2 + (i+1)%2) < teamA:
					reqshots=i+1
					flag=True
					break
			elif teamB > teamA:
				if(teamA + (9-i)/2) < teamB:
					reqshots=i+1
					flag=True
					break

		if flag:
			maximum=max(teamA,teamB)
			if maximum==teamA:
				print "TEAM-A",reqshots
			else:
				print "TEAM-B",reqshots

		else:
			for i in range(10,20):
				if(i%2):
					if penalties[i]=="1":
						teamB+=1
				else:
					if penalties[i]=="1":
						teamA+=1

				if (i%2):
					if(teamA!=teamB):
						flag=True
						reqshots=i+1
						break

			if flag:
				maximum=max(teamA,teamB)
				if maximum==teamA:
					print "TEAM-A",reqshots
				else:
					print "TEAM-B",reqshots
			else:
				print "TIE"	
	except EOFError:
		break
# penalties=raw_input()
