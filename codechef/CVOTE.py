n, m = map(int, input().split())
chefs = {}
countries = {}
for i in range(n):
	chef, country = input().split()
	chefs[chef] = country

chefsvote = {}
for i in range(m):
	voteChef = input()
	voteCountry = chefs[ voteChef ]
	if voteCountry in countries.keys():
		countries[ voteCountry ] += 1
	else:
		countries[ voteCountry ] = 1

	if voteChef in chefsvote.keys():
		chefsvote[ voteChef ] += 1
	else:
		chefsvote[ voteChef ] = 1

print(sorted(list(countries.items()), key = lambda i : (-i[1],i[0]))[0][0])
print(sorted(list(chefsvote.items()), key = lambda i : (-i[1],i[0]))[0][0])
 
