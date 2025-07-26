a = int(input("Number of players:"))
i = 0
play = ["First Name: ","Last Name", "Animal","Fruit","Color","City/Country"]
print(play)
while i < a :
    print("player",i+1,":")
    j = 0
    while j<6:
        play[j] = input()
        j = j+1
    print(play)
    i = i+1