def self_dividing(n):
    for i in str(n):
        if i=='0' or n%int(i)>0:
            return False
    return True
min=int(input())
max=int(input())
for n in range (min,max+1):
    if self_dividing(n):
        print(n,end=' ')