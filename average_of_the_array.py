n=float(input())
a=list(map(float,input().split()))
sum=0
count=0
for i in a:
    sum+=i
    avg=sum/n
print("%.2f"%avg)
