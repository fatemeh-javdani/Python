name1 = input ("Enter name user1: ")
name2 = input ("Enter name user2: ")

print ("<<<Game started!!>>>")

print(name1,"choose from <<'rock','paper','scissors'>> : ")
user1move = input()
print(name2,"choose from <<'rock','paper','scissors'>> : ")
user2move = input()

status = "draw"

while status == "draw":
    if ((user1move=='rock' and user2move =='rock') or
    (user1move=='paper' and user2move =='paper') or
    (user1move=='scissors' and user2move =='scissors')) :
        status = "draw"
    elif ((user1move=='rock' and user2move =='scissors') or
          (user1move=='paper' and user2move =='rock') or  
          (user1move=='scissors' and user2move =='paper')) :
           status = name1
    elif ((user1move=='scissors' and user2move =='rock') or
          (user1move=='rock' and user2move =='paper') or
          (user1move=='paper' and user2move =='scissors')) :
           status = name2
    else:
         print("Invalid input!")
print("****",status,"winn","****")
