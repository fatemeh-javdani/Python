a = int (input("Enter a: "))
b = int (input("Enter b: "))
c = int (input("Enter c: "))
Delta = b*b-4*a*c
if Delta < 0 :
    print ("The equation has no roots")
elif Delta == 0 :
    x = -b/2*a
    print ("x = ", x)
else:
    x1 = (-b+Delta**0.5) / (2 * a)
    x2 = (-b-Delta**0.5) / (2 * a)
    print ("x1 = ", x1)
    print ("x2 = ", x2)