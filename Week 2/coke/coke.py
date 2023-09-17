due = 50

while due > 0:
    x = int(input("Insert Coin:"))
    if x == 5:
        due -= 5
    elif x == 10:
        due -= 10
    elif x == 25:
        due -= 25
    print(f"Amount Due: {due}")

print(f"Change Owed: {-due}")
