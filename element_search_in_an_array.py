t=int(input())
a=list(map(int,input().split()))
num=int(input())
count=0
for i in a:
    # print(i)
    if num==i:
        count=1
        break
    else:
        count=0
if count==1:
    print("True")
else:
    print("False")