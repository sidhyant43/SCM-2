"""n=int(input("Enter the number"))
rev=0
x=n
while(n>0):
    rev=rev*10+n%10
    n=n//10
print(rev,":reverse of number")
if x==rev:
    print("is Palindrome")
else:
    print("not Palindrome")"""


n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j>=i:
            print(n-i+1,end="")
        else:
            print(n-j+1,end="")
    for j in range(n-1,0,-1):
        if j>=i:
            print(n-i+1,end="")
        else:
            print(n-j+1,end="")
        
    print()
for i in range(n-1,0,-1):
    for j in range(1,n+1):
        if j>=i:
            print(n-i+1,end="")
        else:
            print(n-j+1,end="")
    for j in range(n-1,0,-1):
        if j>=i:
            print(n-i+1,end="")
        else:
            print(n-j+1,end="")
    print()
        
