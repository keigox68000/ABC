sq = []
a = 0
while a*a*a <= (10**18):
    sq.append(a*a*a)
    a+=1
N = int(input())
for i in sq[::-1]:
    if N < i:
        continue
    elif str(i) == str(i)[::-1]:
        print(str(i))
        exit()