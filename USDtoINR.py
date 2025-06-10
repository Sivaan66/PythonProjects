def converter(usd):
    usd = int(usd)
    inr = usd*86.7
    print("INR Value:",inr,"Rs.")    
usd = input("USD :")
print(converter(usd))
