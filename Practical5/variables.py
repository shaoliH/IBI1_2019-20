a = 1234
b = 290401
c = 3 * a
d = b / 10
if c > d:
    print("c is greater")
else:
    print("d is greater")

X = True
Y = False

Wrong = False

for X in (True, False):
    for Y in (True, False):
        if (X and Y) or (X and not Y) or (Y and not X):
            if X or Y:
                pass
            else:
                Wrong = True
                print("wrong")
        else:
            if X or Y:
                Wrong = True
                print("wrong")
            else:
                pass

if Wrong:
    print("The truth table is Wrong")
else:
    print("The truth table is right")
