print("Fibonachi 0 -> 1000 ")
a = 0
b = 1
print(a)
print(b)
for i in range(15):
    next = a + b
    a = b
    b = next
    print(next)
