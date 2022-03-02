# Space optimized Python
# implementation of LCS problem

# Returns length of LCS for
# X[0..m-1], Y[0..n-1]
def lcs(X, Y):
	
	# Find lengths of two strings
	x_len = len(X)
	y_len = len(Y)

	L = [[0 for i in range(y_len+1)] for j in range(2)]

	# Binary index, used to index current row and
	# previous row.
	bi = bool
	
	for i in range(x_len):
		# Compute current binary index
		bi = i&1

		for j in range(y_len+1):
			if (i == 0 or j == 0):
				L[bi][j] = 0

			elif (X[i] == Y[j - 1]):
				L[bi][j] = L[1 - bi][j - 1] + 1

			else:
				L[bi][j] = max(L[1 - bi][j],
							L[bi][j - 1])

	# Last filled entry contains length of LCS
	# for X[0..n-1] and Y[0..m-1]
	return L[bi][y_len]

# Driver Code
X = "ATCGTAC"
Y = "ATGTTAT"

print("Length of LCS is", lcs(X, Y))

# This code is contributed by Soumen Ghosh.
