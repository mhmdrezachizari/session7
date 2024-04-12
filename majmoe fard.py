number=int(input())
s=0
z=0
for i in range(0,number+1):
    if i%2!=0:
        s+=i
for i in range(1,number+1):
    if i%5==0:
        z+=i
print(s)
print(z)