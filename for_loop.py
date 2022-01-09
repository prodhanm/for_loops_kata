print("for_loops kata")
print("1. for loops usage of arithmetics.")
print("a. for_loops addition")
num_range = range(16)
for num in num_range:
    print(num + 3)

print("b. subtraction.")
for num in num_range:
    print(num - 3)

print("c. multiplication.")
for num in num_range:
    print(num * 3)

print("d. division.")
for num in num_range:
    print(num / 3)

print("e. floor division.")
for num in num_range:
    print(num // 3)

print("f. modulo.")
for num in num_range:
    print(f"The remainder of {num} is {num%3}")