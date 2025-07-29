def avg(a):
    sum = 0
    for i in a :
        sum = i + sum
    average = sum / len(a)
    return average

def min(a):
    min = a[0]
    for i in a :
        if i < min:
            min = i
    return min

def max(a):
    max = a[0]
    for i in a :
        if i > max:
            max = i
    return max

def var(a):
    for i in a :
        variance = (i - avg(a)) ** 2
        sum = variance + sum
        v = sum/len(a)
    return v

number = [0,1,2]
output = avg(number)
print("average: ",output)

number = [0,1,2]
output = min(number)
print("min: ",output)

number = [0,1,2]
output = max(number)
print("max: ",output)

number = [1,5,6]
output = var(number)
print("varance: ",output)