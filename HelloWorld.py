from Fraction import Fraction


msg = "Hello World"
print(msg)

num = 22
print(num.__add__(12))

arr = [12, 22, 45]
print(arr.__contains__(11))

arr.append('not a number')
print(arr)

try:
    print(arr[4])
except IndexError:
    print("Oopsies, index was out of range")

r1 = Fraction(25, 5)
r2 = Fraction(4)

r1.print()
r2.print()

py_arr = [1, 4, 3/5, 9, 12, 90/5]
print(py_arr)

r3 = 12/3
print(r3)

for number in range(0, 8):
    inside = input()
    arr.append(inside)

print(arr)