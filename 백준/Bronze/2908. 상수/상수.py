a, b = input().split()
a_list = list(a)
b_list = list(b)
a_list.reverse()
b_list.reverse()
if a_list>b_list:
    print("".join(a_list))
elif a_list<b_list:
    print("".join(b_list))