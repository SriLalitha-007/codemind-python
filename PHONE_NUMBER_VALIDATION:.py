num=int(input())
c=0
while(num>0):
    b=num%10
    c+=1
    num=num//10
if(c==10):
    print("Valid")
else:
    print("Invalid")