name1 = input ("Enter name user1: ")
name2 = input ("Enter name user2: ")

print ("<<<Game started!!>>>")

print(name1,"enter 'left' or 'right': ")
gol = input()
print(name2,"enter 'left' or 'right': ")
guess = input()

if ((gol=='left'or gol=='right') and (guess=='left'or guess=='right')) :
    if gol ==guess:
        print("****",name2,"winn","****")
    else:
        print("****",name1,"winn","****")
else:
     print("invalid")