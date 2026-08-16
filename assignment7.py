import random
def rabin_miller(p, k=10):
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    m = p - 1     # Find b and m
    b = 0
    while m % 2 == 0:
        m = m // 2
        b = b + 1
    for i in range(k):
        a = random.randint(2, p - 2)          # Choose random a
        z = pow(a, m, p)           # z = a^m mod p
        # Step 6
        if z == 1 or z == p - 1:
            continue
        for j in range(b - 1):   # Step 7
            z = pow(z, 2, p)
            if z == p - 1:               # Step 8
                break
        else:
            return False                # Step 9
    return True
def main():   # MAIN PROGRAM
    print("Rabin-Miller Primality Test")
    p = int(input("Enter number P: "))
    k = int(input("Enter number of iterations: "))
    if rabin_miller(p, k):
        print(p, "is probably PRIME")
    else:
        print(p, "is COMPOSITE")
if __name__ == "__main__":
    main()
    #7. Use the Robin-Miller algorithm to check whether the given number P is prime or not?

