import random


def main():
    level = get_level()
    score = 0
    for i in range(0,10):
        X = generate_integer(level)
        Y = generate_integer(level)
        lives = 3
        while True:
            inp = input(f" {X} + {Y} = ")
            if inp.isnumeric():
                if int(inp) == X+Y:
                    score += 1
                    break
            print("EEE")
            lives -= 1
            if lives == 0:
                print(f" {X} + {Y} = {Y+X}")
                break
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level in ["1","2","3"]:
            return int(level)


def generate_integer(level):
    match level:
        case 1: return random.randint(0,9)
        case 2: return random.randint(10,99)
        case 3: return random.randint(100,999)

if __name__ == "__main__":
    main()