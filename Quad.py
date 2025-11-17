import math
from fractions import Fraction

# ANSI color codes
COLORS = {
    "frac1": "\033[92m",   # Green
    "float1": "\033[96m",  # Cyan
    "frac2": "\033[93m",   # Yellow
    "float2": "\033[91m",  # Red
    "reset": "\033[0m"
}

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (real_part + imaginary_part * 1j, real_part - imaginary_part * 1j)

def decimal_to_fraction(decimal):
    if isinstance(decimal, complex):
        return decimal
    try:
        fraction = Fraction(decimal).limit_denominator()
        if fraction.denominator == 1:
            return str(fraction.numerator)
        return f"{fraction.numerator}/{fraction.denominator}"
    except:
        return str(decimal)

try:
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    solutions = solve_quadratic(a, b, c)

    for idx, solution in enumerate(solutions, start=1):
        color_frac = COLORS[f"frac{idx}"]
        color_float = COLORS[f"float{idx}"]
        reset = COLORS["reset"]

        if isinstance(solution, complex):
            print(f"The solution x{idx} is a complex number: {solution}")
        else:
            frac_form = decimal_to_fraction(solution)
            float_form = round(float(solution), 6)
            print(f"The solution x{idx} is:")
            print(f"   {color_frac}Fraction: {frac_form}{reset}")
            print(f"   {color_float}Decimal : {float_form}{reset}")

except ValueError as ve:
    print(f"Input error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
