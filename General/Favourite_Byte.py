#There is a also an elegent way to do it {ETAOIN SHLRDU}

#But here i am bruteforcing the xor

from pwn import xor

flag = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(1,255):
	res = xor(flag, bytes(chr(i), 'utf-8'))
	if res.startswith(b"crypto"):
		print(res)
		break



