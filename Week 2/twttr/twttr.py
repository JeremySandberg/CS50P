x = input("Input:")
twttr = ""

for letter in x:
    if letter.lower() in ["a","e","i","o","u"]:
        continue
    else:
        twttr += letter

print(f"Output: {twttr}")
