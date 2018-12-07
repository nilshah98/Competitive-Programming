S = raw_input()
N = len(S)

A = 0
for i in xrange(N):
	D = 0
	Q = 0
	for j in xrange(i, N):
		D += S[j] == '('
		D -= S[j] == ')'
		Q += S[j] == '?'

		if D + Q < 0:
			break

		if Q > D:
			D, Q = Q, D

		if Q == D:
			A += 1
print A