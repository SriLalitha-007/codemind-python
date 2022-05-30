n=int(input())
a=list(map(int,input().split()))
sum=0
count=0
for i in a:
    sum+=i
    avg=sum//n
for j in a:
    if j==avg:
        count=1
        break
else:
    count=0
if count==1:
    print("True")
else:
    print("False")