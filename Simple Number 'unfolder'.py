import math
numbers = input("Enter numbers with spaces: ").split()
orderedNums = []
def oddCount(start):
    for i in range(start,len(numbers),2):
        orderedNums.append(numbers[i])
oddCount(0)
numbers.reverse()
oddCount(1)
print(' '.join(orderedNums))
