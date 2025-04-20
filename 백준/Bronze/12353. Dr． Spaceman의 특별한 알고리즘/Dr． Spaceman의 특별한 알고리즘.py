import sys, math

def to_inches(h):
    f, rest = h.split("'")
    return int(f) * 12 + int(rest[:-1])

input = sys.stdin.readline
T = int(input())
for case in range(1, T+1):
    gender, mom_str, dad_str = input().split()
    mom = to_inches(mom_str)
    dad = to_inches(dad_str)

    delta = 5 if gender == 'B' else -5
    mid = (mom + dad + delta) / 2.0

    low = math.ceil(mid - 4)
    high = math.floor(mid + 4)

    lo_f, lo_i = divmod(low, 12)
    hi_f, hi_i = divmod(high, 12)

    print(f"Case #{case}: {lo_f}'{lo_i}\" to {hi_f}'{hi_i}\"")