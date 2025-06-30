import math

N = input()

dic = {'0':0, '1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
for i in N:
    dic[i] += 1

six_nine = dic['6'] + dic['9']
dic['6'] = dic['9'] = math.ceil(six_nine / 2)

print(max(dic.values()))