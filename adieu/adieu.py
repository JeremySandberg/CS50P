names = []

while True:
    try:
        names.append(input())
        continue
    except:
        break
extend = ""
if len(names) > 1:
    extend = f" and {names[-1]}"
    if len(names) > 2:
        extra = ", ".join(names[1:-1])
        extend = f", {extra},{extend}"

print(f"Adieu, adieu, to {names[0]}{extend}")
