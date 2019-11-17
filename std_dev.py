from math import sqrt
n = int(input())
m = input()
x = [int(i) for i in m.split(' ')]
mu = sum(x)/n
v=0
for i in x:
    v += (i-mu)**2
print(sqrt(v/n))
