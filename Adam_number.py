num=int(input())#12
rev=0
rev2=0
sq=num**2#144
while num>0:
    digit = num % 10
    rev= rev* 10 + digit#21
    num//= 10
sq_rev=rev**2#441
while(sq_rev>0):
    dig = sq_rev % 10
    rev2 =  rev2* 10 + dig#144
    sq_rev//= 10
if(rev2==sq):
    print("True")
else:
    print("False")