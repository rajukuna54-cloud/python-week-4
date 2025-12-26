n = int(input("enter number of elements:"))
count=0
count1=0
for i in range(1,n+1):
    if (i%2==0):
        count=count+1
    elif(i%2==1):
       count1=count1+1
print("how many no.of even numbers:",count)
print("how many no.of odd numbers:",count1)
