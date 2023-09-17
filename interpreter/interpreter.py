x = input("Expression:")
x = x.split()
match x[1]:
    case "+":
        print(float(x[0])+float(x[2]))
    case "-":
        print(float(x[0])-float(x[2]))
    case "/":
        print(float(x[0])/float(x[2]))
    case "*":
        print(float(x[0])*float(x[2]))