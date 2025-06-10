def PINVALIDATION():
    PIN = int(input("Enter the PIN :").strip())
    if PIN % 4 == 0 :
        print("OPEN")
    else:
        print("LOCKED")
        print(PINVALIDATION())

PINVALIDATION()
