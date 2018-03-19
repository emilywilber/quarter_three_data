# make a list
nums = [3, 1, 4, 1, 5, 9]

# find the length of a list
print( len(nums) )

# select individual items from a list
begin = nums[0]
end = nums[5]
end = nums[len(nums) - 1]
end = nums[-1] # python specific shorthand

print(begin, end)

# get a "slice" of a list
print( nums[0:3] )
print( nums[:3] )
print( nums[3:] )
print( nums[2:4] )

# lists can contain strings
names = ["Terry Gilliam", "Michael Palin", "Eric Idle", "Terry Jones", "John Cleese", "Graham Chapman"]
print(len(names))
print(names)

# select a random element from a list
import random
print(random.choice(names))

# swap items in a list
temp = names[0]
names[0] = names[1]
names[1] = temp
print(names)


# In Python we can swap variables by taking advantage of tuple packing/unpacking
x = 5
y = 3
print(x, y)
x, y = y, x
print(x, y)

names[0], names[1] = names[1], names[0]
print(names)
