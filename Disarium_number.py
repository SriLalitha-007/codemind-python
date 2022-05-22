num=eval(input())
c=len(str(num))
temp=num
s=0
while num!=0:
    a=num%10
    num//=10
    m=a**c
    s+=m
    c-=1
if s==temp:
    print("True")
else:
    print('False')