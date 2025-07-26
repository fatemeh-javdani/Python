print("Welcome!")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

a = "1"
b = "2"
c = "3"
d = "4"
e = "5"
f = "6"
g = "7"
h = "8"
i = "9"

turn = 1

while turn <= 9:
    if turn % 2 == 1:
        player = "X"
    else:
        player = "O"

    move = input("Player " + player + ", choose a number (1-9): ")

    if move == "1" and a == "1":
        a = player
    elif move == "2" and b == "2":
        b = player
    elif move == "3" and c == "3":
        c = player
    elif move == "4" and d == "4":
        d = player
    elif move == "5" and e == "5":
        e = player
    elif move == "6" and f == "6":
        f = player
    elif move == "7" and g == "7":
        g = player
    elif move == "8" and h == "8":
        h = player
    elif move == "9" and i == "9":
        i = player
    else:
        print("Invalid move, try again.")
        continue 

    print()
    print(a + " | " + b + " | " + c)
    print("--+---+--")
    print(d + " | " + e + " | " + f)
    print("--+---+--")
    print(g + " | " + h + " | " + i)
    print()

    if ((a == b == c) or 
        (d == e == f) or 
        (g == h == i) or 
        (a == d == g) or 
        (b == e == h) or 
        (c == f == i) or 
        (a == e == i) or 
        (c == e == g)):
        print("Player", player, "wins!")
        break

    turn += 1

if turn > 9:
    print("It's a draw!")