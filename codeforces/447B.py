MOD=10**9+7

# def ipow(base, exp):
#     result = 1
#     base=base%MOD
#     while (exp):
#         if (exp & 1):
#             result = (result*base)%MOD
#         exp >>= 1
#         base = (base*base)%MOD
#     return result

n,m,k=map(int, raw_input().split())
if k == 1 or (n % 2 == m % 2):
	print pow(2,((n-1)*(m-1)), MOD)
	#n-1 and m-1, since we can put any values there, and then, put the closing values at the end
	# never knew it had an extra argument in pow for modular exponention
else:
	print 0
	#0 when there are odd no of rows, and even no of columns, so -1 becomes +1 in one, and -1 in other.