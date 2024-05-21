n = int(input())
cnt = 0
cntt = 0
for i in range(n):
	a = input()
	for j in a:
		if j=="(":
			cnt+=1
		else:
			cnt-=1
		if cnt<0:
			cntt+=1
	if cnt==0 and cntt==0:
		print("YES")
	else:
		print("NO")
	cnt = 0
	cntt=0