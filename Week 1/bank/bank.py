x = input("Greeting:")
x = x.replace(" ","").lower()
if x[:5] == "hello":
    print("$0")
elif x[0] == "h":
    print("$20")
else:
    print("$100")

