x=int(input())
for i in range (0,x):
    n,a,b,k=map(int,input().split())
    i=0
    if (a%b==0):
        i=a
    elif(b%a==0):
        i=b
    else:
        i=a*b
    f=n//i
    c=n//a
    d=n//b
    c=c-f
    d=d-f
    if c+d>=k:
        print("Win")
    else:
        print("Lose")