L = [4, 5, 2, 9, 8, 10, 9]
print("Original List:" ,L)
sum = 0
for i in L:
    sum += i
print("Sum of the list elements:", sum)
avg = sum/len(L)
print("The average of the list elements:", avg)
L.sort()
print("The sorted list is:", L)
print("The largest element is:", L[-1])
print("The smallest element is:", L[0])