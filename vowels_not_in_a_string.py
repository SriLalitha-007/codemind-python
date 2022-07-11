s=input()
a=0
e=0
i=0
o=0
u=0
for j in range(len(s)):
    if s[j]=='a':
        a+=1
    if s[j]=='e':
        e+=1
    if s[j]=='i':
        i+=1
    if s[j]=='o':
        o+=1
    if s[j]=='u':
        u+=1
if a==0:
    print('a',end=' ')
if e==0:
    print('e',end=' ')
if i==0:
    print('i',end=' ')
if o==0:
    print('o',end=' ')
if u==0:
    print('u',end=' ')
if a!=0 and e!=0 and i!=0 and u!=0:
    print('0')