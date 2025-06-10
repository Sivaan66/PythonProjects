#Pin Validation Problem (21:59)
#A problem about checking if a given N-digit PIN is divisible by 4. If divisible, output "open", else "locked".

def PINVALIDATION():
    t = int(input())

    for _ in range(t):
        PIN = (input().strip())
        sum = 0 

        for digits in PIN:
            sum += int(digits)

        if sum % 4 == 0 :
            print("OPEN")
        else:
            print("LOCKED")

PINVALIDATION()
