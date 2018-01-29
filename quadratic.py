# 求解二次方程
import math
def main():
    print("This program find the rea solutions to a quadratic\n")
    a, b, c = eval(input("Please enter the coefficients(a, b, c):"))
    delta = b * b - 4 * a * c
    if a == 0:
        x = -b / c
        print("\nThere is an solution", x)
    elif delta < 0:
        print("\nThe equation has no real roots!")
    elif delta ==0:
        x = -b /(2 * a)
        print("\nThere is a double root at", x)
    
        discRoot = math.sqrt(delta)
        root1 = (-b + discRoot) / (2 * a)
        root2 = (-b - discRoot) / (2 * a)
        print("\nThe solutions are:", root1, root2)
    else:
        print("The equation has no real roots!")
main()