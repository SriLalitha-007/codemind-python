num=int(input())
rev=0
rev1=0
s=0
count=0
count1=0
for j in range(2,num):
     if num%j==0:
        count1+=1
while(num>0):
    s=num%10
    rev=rev*10+s
    num//=10
for i in range(2,rev):
    if rev%i==0:
        count+=1
if count==0:
    print("circular prime")
elif count1!=0:
    print("not prime")
else:
    print("prime but not a circular prime")