## Strips all char after COMMA
## used in names, and removes \n


FILE = 'names.txt'
F = open(FILE,'r')
with open(FILE) as inf:
    LST = inf.readlines()


W = open('New_Names.txt', 'w')


for T in range(len(LST)):
    L = (LST[T].split(",")[0] + '\n')
    W.write(L)

print " okay "
