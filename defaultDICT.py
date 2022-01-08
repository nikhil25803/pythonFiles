from collections import defaultdict

d=defaultdict(int)

print(d['B'])

L=['A','B','C','D','E','A']

# L=[1,2,3,4,2,1,2]

for i in L:
    d[i]+=1


print(d)