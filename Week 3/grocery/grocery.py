groceries = {}

while True:
    try:
        inp = input().upper()
    except:
        break
    groceries[inp] = groceries.get(inp, 0) + 1

for k,v in sorted(groceries.items()):
    print(v,k)

