num=int(input())
a=list(map(int,input().split()))
e=0
o=0
length=len(a)
for i in range(0,length):
    if i%2==0:
        e+=a[i]
for j in range(0,length):
    if j%2!=0:
        o+=a[j]
diff=e-o
print(abs(diff))