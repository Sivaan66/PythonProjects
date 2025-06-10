def coordinates():
    t = int(input("Enter a number-").strip())
    for _ in range(t) :
        moves = input().strip().upper()
        x=0
        y=0
        for move in moves:
            if move == "U" :
                y+=1
            elif move == "D":
                y-=1
            elif move == "L":
                x-=1
            elif move == "R":
                x+=1
            else:
                print("We don't have any other directions")
        print("(x,y) = ",x,y)

coordinates()
