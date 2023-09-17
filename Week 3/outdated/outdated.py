months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inp = input("Date:")
    except:
        break

    if "/" in inp:
        m,d,y = inp.replace(" ", "").split("/")
        if not m.isnumeric() or not d.isnumeric() or not y.isnumeric():
            continue
    elif "," in inp:
        m,d,y = inp.replace(",","").split()
        if not m.isalpha() or not d.isnumeric() or not y.isnumeric():
            continue
        m = months.index(m)+1
    else: continue

    if int(d) > 31 or int(m) > 12: continue
    print(f"{y}-{int(m):02}-{int(d):02}")
    break

