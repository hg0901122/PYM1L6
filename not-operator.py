a = 10
b = 10
c = 5

print(a == b)

print(not(a == b))

print(not(b == c))

a = "python"
b = "coding"
if not(a == b):
    print(a, "and", b, "are different")

a = 4
b = 5

if not((a == 1) == (b == 5)):
    print("Hello")

a = int(input("Enter a number: "))

if not(a % 2 == 0):
    print(a, "is an odd number.")