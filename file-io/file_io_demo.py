import random

# open a file using a 'relative file path'
with open('data/last_words.txt', 'r') as f:
    line1 = f.readline()
    line2 = f.readline()
    
print(line1)
print(line2)
print()


# read the entire file file
with open('data/movies.txt', 'r') as f:
    contents = f.read()
    
print(contents)
print()


# read files into a list
with open('data/movies.txt', 'r') as f:
    movies = f.readlines()

print(movies)
print()


# splitlines() separates on linebreak and removes
# the newline character
with open('data/movies.txt', 'r') as f:
    movies = f.read().splitlines()
    
print(movies)
print()


# write a file
# try changeing 'w' to 'a' and see what happens
# (You'll need to run the program more than once)
with open('new_file.txt', 'w') as f:
    f.write('This is one line.')
    f.write('This is another.\n')
    f.write('This is actually on the next line')


# read a big file, don't try to print all items!
with open('data/scrabble_list.txt', 'r') as f:
    words = f.read().splitlines()

print(words[:10])

# select a random element from a list
print(random.choice(words))


# use a for loop to process the list
''' how many words end with an s? '''
count = 0
for w in words:
    if w[-1] == 's':
        count += 1

print(count)


''' how many words are 2 letters long? '''
count = 0
for w in words:
    if len(w) == 2:
        count += 1

print(count)


''' make a new file with all words that are 2 letters long ''' 

with open('two_letters.txt', 'w') as f:
    for w in words:
        if len(w) == 2:
            f.write(w + "\n")


