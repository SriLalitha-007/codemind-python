num=int(input())
a=list(map(int,input().split()))
s=0
length=len(a)
for i in range(0,length):
    if i%2!=0:
        s+=a[i]
print(s)
    