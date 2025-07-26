# Average

n=int(input("how many number do you want to enter?"))
if n>0:
    i = 0
    sum = 0
    while i<n:
        a=float(input("enter number: "))
        sum=a+sum
        i=i+1
    avg=sum/n
    print("Average:",avg)
else:
    print("invalid number")
