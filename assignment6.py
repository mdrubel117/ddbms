import random
def lehmann(p, k=10):
    if p <= 1:
        return False
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    for i in range(k):
        a = random.randint(2, p - 2)
        r = pow(a, (p - 1) // 2, p)
        if r != 1 and r != p - 1:
            return False
    return True
def main():   # MAIN PROGRAM
    print("Lehmann Primality Test")
    p = int(input("Enter number P: "))
    k = int(input("Enter number of iterations: "))
    if lehmann(p, k):
        print(p, "is probably PRIME")
    else:
        print(p, "is Not prime")
if __name__ == "__main__":
    main()
    #6.Use the Lehmann algorithm to check whether the given number P is prime or not?
