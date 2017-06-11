from random import randint

magic_number = randint(0, 100)

# Ok this program checks if magic number is within a range
# Its a singe-line comment btw

'''
Here's a multiline comment
'''

for n in range(100):
    if n is magic_number:
        print("Magic number is ", n)
        break
    else:
        print(n)


