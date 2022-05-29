num=int(input())
a=list(map(int,input().split()))
e=0
s=0
o=0
length=len(a)
for i in a:
    if i%2==0:
        e+=i
for j in a:
    if j%2!=0:
        o+=j
diff=(o-e)
print(abs(diff))    