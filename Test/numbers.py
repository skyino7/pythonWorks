li = list(range(1, 25))

even = []
odd = []

for i in li:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even Numbers: ", even)
print("Odd Numbers: ", odd)
