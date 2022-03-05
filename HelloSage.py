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

sage_arr = [1, 4, 3/5, 9, 12, 90/5, -1/15, 12/-5]
print(sage_arr)

r3 = 12/3
print(r3)

arr = []
arr_len = 0

print(type(sage_arr[2]))
"""
"""
arr=[]

while(True):
    try:
        arr_len = int(input("How long will your array be? "))
        break
    except ValueError:
        print("This has to be an Integer")

print("Insert your value:")
for number in range(0, arr_len):
    while(True):
        value = input()
        try:
            value = sage.rings.rational.Rational(value)
            arr.append(value)
            break
        # problem is, numbers like "12.5" or "7.3" are not counted as Rational!
        except TypeError:
            print("This is not an accepted value! Integers or fractions only!")

print(arr)
print(sum(arr))