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

num_data = [35, 70, 75, 89, 33, 69, 96, 121, 110, 45, 51]
num_range = range(len(num_data)//2, len(num_data))
num_sum = 0

print("3. Finding the average sums in a selective nums in a list.")
for num in num_range:
    num_sum += num_data[num]
    num_avg = num_sum/(len(num_data) - (len(num_data)//2))
print(num_avg)

print("4. List building")
print("a. buidling a list of odd and even numbers")
odd_numbers = []
even_numbers = []
n=101
n_range = range(n)

for n in n_range:
    if n%2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)
print(f"odd_numbers = {odd_numbers}")
print(f"even_numbers = {even_numbers}")

print("b. multiples of numbers list")
multi_5 = []
m = 15
multi_range = range(5, n*5+1, 5)

for m in multi_range:
    multi_5.append(m)
print(f"multi_5 = {multi_5}")


