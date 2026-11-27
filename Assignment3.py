def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])

    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return True
    else:
        return False

# Accept three sides from the user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check whether it is a right-angled triangle
if is_right_triangle(a, b, c):
    print("It is a Right-Angled Triangle")
else:
    print("It is not a Right-Angled Triangle")

