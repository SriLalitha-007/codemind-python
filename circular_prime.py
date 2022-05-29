num=int(input())
count=0
b= int(str(num)[::-1])
for i in range(2,num):
    if num%i==0:
        break
else:
    count=1
for j in range(2,b):
    if b%j==0:
        break
else:    
    count=2
if count==0:
    print("not prime")
elif count==1:
    print("prime but not a circular prime")
elif count==2:
    print("circular prime")