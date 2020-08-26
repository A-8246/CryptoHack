from pwn import xor

flag = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
known="crypto{"
def result():
	key = ''
	n = len(known)
	for i in range(n):
		key+=chr(flag[i] ^ ord(known[i]))
	key += 'y' #Based on obtained key pattern
	print(xor(flag, key))

result()
