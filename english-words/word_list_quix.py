with open('words_alpha.txt', 'r') as f:
    words = f.read().splitlines()

print(words[0:10])
print()
'''
count = 0
for w in words:
    count += 1
print(count)

count = 0
for w in words:
    if len(w) == 5:
        count += 1
print(count)

count = 0
for w in words:
    if len(w) > 7:
        count +=1
print(count)

count = 0
for w in words:
    if w[0] == w[-1]:
        count += 1
print(count)

bigboy = 0
for w in words:
    if bigboy < len(w):
        bigboy = len(w)
print(bigboy)
'''
count = 0
for w in words:
    count += len(w)
print(count)
'''
count = 370099
for i in words:
    if 'e' in i:
        count -= 1
print(count)

count = 0
for w in words:
    i = 0
    acount = 0
    while i < len(w):
        if w[i] == 'a':
            acount += 1
        i += 1
    if acount == 3:
        count += 1
print(count)

count = 0
for w in words:
    i = 0
    while i < len(w):
        if w[i] == 'q':
            if w[i+1] != 'u':
                count =+ 1
print(count)        
'''
