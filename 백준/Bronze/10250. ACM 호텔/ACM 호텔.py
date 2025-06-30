T = int(input())
for _ in range(T):
    cnt = 0
    H, W, N = map(int, input().split())
    for i in range(1, W+1):
        for j in range(1, H+1):
            cnt += 1
            if cnt == N:
                if i < 10:
                    print(f"{j}0{i}")
                else:
                    print(f"{j}{i}")