a = int(input("enter a value:"))
b = int(input("enter b value:"))
c = int(input("enter c value:"))
#maximum
if a>b and a>c:
    print("maximum number is:",a)
elif b>a and b>c:
    print("maximum number is:",b)
else:
    print("maximum number is:",c)
#minimum
if a<b and a<c:
    print("minimum number is:",a)
elif b<a and b<c:
    print("minimum number is:",b)
else:
    print("minimum number is:",c)
