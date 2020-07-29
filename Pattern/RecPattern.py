## Solid rectangle star pattern
r = 3
c = 5
for i in range(r):
    for j in range(c):
        print("*", end=" ")
    print()

print("\n")
## Hollow rectangle star pattern

row = 4
col = 7

for i in range(row):
    for j in range(col):
        if i == 0 or i == row-1 or j == 0 or j == col - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
