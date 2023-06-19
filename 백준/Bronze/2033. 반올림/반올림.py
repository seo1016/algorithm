n = int(input())
s = str(n)
for i in range(1, len(s)):
	s = str(n)
	if 5 <= int(s[-i]):
		n //= 10**i
		n += 1
		n *= 10**i
	else:
		n //= 10**i
		n *= 10**i
print(n)