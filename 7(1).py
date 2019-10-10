f1=open("prime.txt","w")
for val in range(0, 1001):
    if val > 1:
        for n in range(2, val):
            if (val % n) == 0:
                break
        else:
            f1.write(str(val))
            f1.write("\n")
f1.close()
with open("prime.txt","r") as f1:
    print(f1.read())

def numSquareSum(n): 
    squareSum = 0; 
    while(n): 
        squareSum += (n % 10) * (n % 10); 
        n = int(n / 10); 
    return squareSum;
def isHappynumber(n):
    slow = n; 
    fast = n; 
    while(True): 
          slow = numSquareSum(slow);
          fast = numSquareSum(numSquareSum(fast));
          if(slow != fast):
              continue;
          else:
              break; 
    return (slow == 1);

f2=open("happy.txt","w")
for i in range(1,1001):
    if(isHappynumber(i)):
        f2.write(str(i))
        f2.write("\n")

f2=open("happy.txt","r")
print(f2.read())



common=[]
f1=open("happy.txt","r")
line=[]
l=[]
l=f1.readline()
while l:
    line.append(l)
    l=f1.readline()
f2=open("pri.txt","r")
line1=[]
l1=[]
l1=f2.readline()
while l:
    line1.append(l)
    l1=f1.readline()

for i in line1:
    if i in line:
        common.append(i)
print(i)
