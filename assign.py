
n=int(input("enter members of list"))
borrow =[0]*n

for i in range:
    borrow[i]=int(input("enter books borrowed by member"+str(i+1)+":"))

total=0
for i in range(n):
    total =total+borrow[i]
    average = total/n
print("\naverage books borrowed:",average)

highest= borrow[0]
lowest = borrow[0]
for i in range(1,n):
    if borrow[i]>highest:
        highest= borrow[i]
    if borrow[i]<lowest:
        lowest =borrow[i]
print("Highest borrow count:",highest) 
print("Lowest borrow count:",lowest)

count=0
for i in range(n):
    if borrow[i]==0:
        count=count+1
print("\n Members who purchased no books :",count)    
    
      