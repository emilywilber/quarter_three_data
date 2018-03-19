animals = ['dog', 'mouse', 'cat', 'horse', 'octopus', 'giraffe', 'lion']

print(len(animals))
print(animals[0])

i = 0
while i < len(animals):
    print(animals[i])
    i += 1


"""
for every animal in the list called animals:
    print the animal


for every animal, a, in animals:
    print(a)
"""

for a in animals:
    print(a)


# print animals with three letters
for a in animals:
    if len(a) == 3:
        print(a)


# count animals with three letters
count = 0
for a in animals:
    if len(a) == 3:
        count += 1
print(count)


# count animals without three letters
count = 0
for a in animals:
    if len(a) != 3:
        count += 1
print(count)


# find the sum of values in a list
nums = [4, 9, 14, 3, 22, 5, 11]

total = 0
for n in nums:
    total += n

print(total)


# Python does have a sum function, so don't use sum as a variable name
total = sum(nums)
print(total)


# The built-in sum won't work if you want to find
# the sum of just the even numbers in a list
total = 0
for n in nums:
    if n % 2 == 0:
        total += n

print(total)


# find the largest number in a list
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n

print(largest)

# Python does have a max function (and a min too)
largest = max(nums)
print(largest)


# But we still need to know a max algorithm to solve problems like...

# Find the length of the longest word in animals
longest = 0

for a in animals:
    if len(a) > longest:
        longest = len(a)

print(longest)


# Find the longest word in animals
longest = 0
word = animals[0]

for a in animals:
    if len(a) > longest:
        longest = len(a)
        word = a

print(word)




