
while True:
    inp = input("Fraction: ")
    if "/" not in inp: continue
    x,y = inp.split("/")
    if not x.isdigit() or not y.isdigit(): continue

    try:
        fraction = float(x)/float(y)

    except (ValueError, ZeroDivisionError):
        continue

    if fraction > 1: continue
    percentage = round(fraction*100)
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")
    break