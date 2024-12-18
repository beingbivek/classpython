N = int(input("Enter the number of Students: "))
K = int(input("Enter the number of Apples: "))
if N > K:
    print(f"There\'s not enough apples to distribute evenly with {N} Students.")
else:
    each = K // N
    basket = K - each * N
    print(f"{N} Student get {each} apples each with {basket} apples remaining in the basket.")