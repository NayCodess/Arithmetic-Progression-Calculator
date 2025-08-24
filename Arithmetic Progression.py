print("📘 ARITHMETIC PROGRESSION CALCULATOR 📘")

# Inputs
A1 = float(input("Enter the first term (A1): "))
A2 = float(input("Enter the second term (A2): "))

# Definitions
print("\nSymbols Used:")
print(" cd = Common Difference")
print(" An = Nth term of the AP")
print(" n  = Number of terms\n")

# Choice
what = input("What do you want to find? (cd / An / n / series): ").lower()

if what == "cd":
    d = A2 - A1
    print(f"\n👉 The Common Difference (cd) is: {d}")

elif what == "An":
    n = int(input("Enter the value of n: "))
    d = A2 - A1
    An = A1 + (n - 1) * d
    print(f"\n👉 The {n}th term (An) is: {An}")

elif what == "n":
    An = float(input("Enter the value of An: "))
    d = A2 - A1
    n = ((An - A1) / d) + 1
    if n.is_integer():
        print(f"\n👉 The term {An} occurs at position n = {int(n)}")
    else:
        print(f"\n⚠️ The value {An} is not exactly part of this AP. (Got n ≈ {n})")

elif what == "series":
    n = int(input("How many terms do you want to print? "))
    d = A2 - A1
    print("\n👉 Arithmetic Progression Series:")
    for i in range(1, n + 1):
        term = A1 + (i - 1) * d
        print(f"Term {i}: {term}")

else:
    print("\n⚠️ Invalid choice. Please enter cd, An, n, or series.")

print("\n✅ CHECK COMPLETE")