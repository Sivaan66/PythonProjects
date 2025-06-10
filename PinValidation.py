def PINVALIDATION():
    t = int(input("enter"))

    for _ in range(t):
        PIN = int(input("Enter the PIN :").strip())
        

        if PIN % 4 == 0 :
            print("OPEN")
        else:
            print("LOCKED")

PINVALIDATION()
