import random

movm = int(input("How many movements you want?: "))

num_1 = int(input("starting number: "))
num_2 = int(input("ending number: "))

moqmedeba = ["+", "-", "*", "/", "**", "%"]

if (num_1 > num_2):
    print(f"Your first number ({num_1}) is bigger than second ({num_2})!")
    print(f"So, we need to change places")

    tmp = num_1
    num_1 = num_2
    num_2 = tmp

else:
    pass

pick_1 = random.choice(range(num_1, num_2))
pick_2 = random.choice(range(num_1, num_2))

for i in range(movm):
    if random.choice(moqmedeba) == "+":
        if pick_1 == pick_2:
            print("{g} = {f}".format(g=pick_1, f=pick_2))

        else:
            ans = pick_1 + pick_2
            print("{g} + {f} = {h}".format(g=pick_1, f=pick_2, h=ans))

    elif random.choice(moqmedeba) == "-":
        if pick_1 > pick_2:
            ans = pick_1 + pick_2
            print("{g} + {f} = {h}".format(g=pick_1, f=pick_2, h=ans))

        elif pick_1 < pick_2:
            ans = pick_2 - pick_1
            print("{g} - {f} = {h}".format(g=pick_2, f=pick_1, h=ans))

        else:
            print("{g} = {f}".format(g=pick_1, f=pick_2))

    elif random.choice(moqmedeba) == "*":
        if pick_1 == pick_2:
            print("{g} = {f}".format(g=pick_1, f=pick_2))

        else:
            ans = pick_1 * pick_2
            print("{g} * {f} = {h}".format(g=pick_1, f=pick_2, h=ans))

    elif random.choice(moqmedeba) == "/":
        if pick_1 > pick_2:
            ans = pick_1 / pick_2
            print("{g} / {f} = {h}".format(g=pick_1, f=pick_2, h=ans))

        elif pick_1 < pick_2:
            ans = pick_2 / pick_1
            print("{g} / {f} = {h}".format(g=pick_2, f=pick_1, h=ans))

        else:
            print("{g} = {f}".format(g=pick_1, f=pick_2))

    elif random.choice(moqmedeba) == "**":
        if pick_1 == pick_2:
            ans = pick_1 ** 2
            print("{g} ** 2 = {h}".format(g=pick_1, h=ans))

        else:
            if pick_1 > 10:
                pick_1 = pick_1 / 10
                ans = pick_1 ** pick_1
                print("{g} ** {g} = {f}".format(g=pick_1, h=pick_1, f=ans))

            else:
                ans = pick_1 ** pick_1
                print("{g} ** {g} = {f}".format(g=pick_1, h=pick_1, f=ans))

    elif random.choice(moqmedeba) == "%":
        if pick_1 > pick_2:
            ans = pick_1 % pick_2
            print("{g} % {h} = {s}".format(g=pick_1, h=pick_2, s=ans))

        else:
            ans = pick_2 % pick_1
            print("{g} % {h} = {s}".format(g=pick_2, h=pick_1, s=ans))