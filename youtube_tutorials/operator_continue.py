numbers_taken = [2, 3, 5, 8, 17]

# continue forces interpreter to go to the beginning of current block as I understand
# so when current n is in numbers_taken, it will NOT be printed because cycle goes with next value

for n in range(20):
    if n in numbers_taken:
        continue
    print(n)
