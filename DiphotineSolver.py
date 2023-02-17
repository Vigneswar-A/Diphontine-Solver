from collections import Counter


def calculate_gcd(a, b):
    mapping = {}
    a, b = sorted([a, b], reverse=1)
    while b != 0:
        q, rem = divmod(a, b)
        print(f"{a} = {b}x{q} + {rem}")
        mapping[rem] = [a, b, q]
        a, b = b, rem
    print()
    return a, mapping


def calculate_multiplicative_inverse(a, b, n, mapping, gcd):
    equation = Counter([gcd])
    print("1", end="")
    while True:
        flag = True
        for num in mapping:
            if equation[num]:
                temp_a, temp_b, temp_q = mapping[num]
                equation[temp_a] += equation[num]
                equation[temp_b] -= temp_q*equation[num]
                del equation[num]
                flag = False

        if flag:
            break
        print(convert(equation))

    print()
    print(f"({equation[a]})({a})(X) ≡ ({b})({equation[a]})(mod {n})")
    print(f" => X ≡ {equation[a]*b}(mod {n})")
    print(f" => X = {(equation[a]*b)%n}")
    return equation[a]*b % n


def convert(equation):
    res = " = "
    for key, val in equation.items():
        if not val:
            continue
        res += (f"({key})({val}) + ")
    return res[:-2]


def solve_diphontine(a, b, n):
    print(f"({a})X ≡ {b}(mod {n})\n")
    d, mapping = calculate_gcd(a, n)
    print(f"gcd = {d}\n")
    if d == 1:
        print("Unique Solution Exists")
        t = calculate_multiplicative_inverse(a, b, n, mapping, 1)
        print(f"The solution is {t}")
    elif b % d == 0:
        print(f"{d} divides {b}, so {d} solutions exists")
        print(f"=> ({a}/{d})X ≡ ({b}/{d})(mod {n}/{d})")
        print(f"=> ({a//d})X ≡ ({b//d})(mod {n//d})\n")
        gcd, mapping = calculate_gcd(a//d, n//d)
        t = calculate_multiplicative_inverse(a//d, b//d, n//d, mapping, gcd)
        print(f"\n{t = }")
        print(f"So the Solutions {d} are:")
        for co_eff in range(d):
            print(f"    {t} + {co_eff}({n}/{d}) = {t + co_eff*n//d}")
    else:
        print(f"{d} doesn't divide {b}, so no solutions exist")


flag = True
while flag:
    flag = True
    a = int(input("Enter the value of a:"))
    b = int(input("Enter the value of b:"))
    n = int(input("Enter the valud of n:"))
    solve_diphontine(a, b, n)
    print()
    flag = input("Do you want to try again? (y/?)").casefold() == "y"

print("Done by Vigneswar A :) ")
input()
