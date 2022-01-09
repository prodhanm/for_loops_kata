print("for_loops kata")
print("1. for loops usage of arithmetics.")
print("a. for_loops addition")
num_range = range(1, 16)
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

print("2. Counting by artihmatic.")
print("a. addition ")
counter = 0
for num in num_range:
    counter += num
print(f"The total sum is {counter}.")


print("b. multiplication ")
product = 1
for num in num_range:
    product *= num
print(f"The product is {product}.")

print("c. division ")
product = 1
for num in num_range:
    product /= num
print(f"The quotient is {product}.")





