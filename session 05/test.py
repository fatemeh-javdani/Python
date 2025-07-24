# max & min

n=int(input("how many number do you want to compare?"))
if n>0:
    max=min=int(input("enter first number: "))
    i=2
    while i<=n:
        a=int(input("enter number: "))
        if a>max:
            max=a
        if a<min:
            min=a
        i=i+1
    print("max: ",max,"min: ",min)
else:
    print("invalid number")
    

print("Enter 4 number to continue: ")
a=int(input("enter number 1: "))
b=int(input("enter number 2: "))
c=int(input("enter number 3: "))
d=int(input("enter number 4: "))
#average
avg= (a+b+c+d)/4
print("average=",avg)

#variance
a=(a-avg)**2
b=(b-avg)**2
c=(c-avg)**2
d=(d-avg)**2
var= (a+b+c+d)/4
print("variance=",var)

#Standard Deviation
enheraf=var**0.5
print("Enheraf meyar=",enheraf)