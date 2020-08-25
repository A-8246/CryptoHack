s = "label"
i = 13
final=""
for x in s:
	final+=chr(ord(x)^int(i))
print(final)
