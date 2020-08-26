#For Euclidean algorithms-> https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

def gcd(a, b):
	if(a==0):
		return b
	return gcd(b%a, a)

print(gcd(52920, 66528))
