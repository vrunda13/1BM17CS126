n=int(input("enter the count"))
l1=[];
for i in range(0,n):
    ele =int(input("element"))
    l1.append(ele)

print(l1)
l2=[num for num in l1 if num%2==0]
print(l2)
