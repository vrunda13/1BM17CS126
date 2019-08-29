a=input("enter the string")
a=a.split("")
a=a[-1::-1]
s=" "
for x in a:
   s+=x
print(s)
