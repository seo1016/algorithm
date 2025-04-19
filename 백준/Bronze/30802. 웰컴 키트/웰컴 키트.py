N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundles = sum((size + T - 1) // T for size in sizes)

pen_bundles = N // P
single_pens = N % P

print(shirt_bundles)
print(pen_bundles, single_pens)