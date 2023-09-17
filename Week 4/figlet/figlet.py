import sys
from pyfiglet import Figlet

figlet = Figlet()
fontnames = figlet.getFonts()

if len(sys.argv) == 1:
    pass
elif len(sys.argv) != 3 or sys.argv[1] not in ["-f","--font"] or sys.argv[2] not in fontnames:
    sys.exit("Incorrect arguments")
elif len(sys.argv) == 3:
     figlet.setFont(font=sys.argv[2])

s = input("Input: ")
print(figlet.renderText(s))
