n = int(input())
N = [float(i) for i in input().split(' ')]
w = [float(i) for i in input().split(' ')]

nr = 0
dr = 0 
for i in range(n):
    nr += N[i]*w[i] 

    dr += w[i]
print(nr/dr )
