def PINVALIDATION():
    PIN = int(input("Enter the PIN :").strip())
    pin_str = str(PIN)
    pin_list = list(pin_str)
    if len(pin_list) != 4 :
        print("Wrong PIN")
        print(PINVALIDATION())
        return
    pin = int("".join(pin_list))
    if pin % 4 == 0 :
        print("OPEN")
    else:
        print("LOCKED")
        print(PINVALIDATION())
        

PINVALIDATION()
