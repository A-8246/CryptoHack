#Euclidean Algorithm-> https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
def gcdExtended(a, b): 
	if a == 0 : 
		return b, 0, 1
	gcd, x1, y1 = gcdExtended(b%a, a) 
	u = y1 - (b//a) * x1 
	v = x1 
	return gcd, u, v 
	
a, b = 26513, 32321
g, u, v = gcdExtended(a, b) 
print(u)
print(v)
print("gcd(", a , "," , b, ") = ", g) 
