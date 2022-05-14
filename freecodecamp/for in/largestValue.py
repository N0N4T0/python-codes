largestValue = -1
print('Before', largestValue)

for numberValue in [9, 41, 12, 3, 74, 15]:
    if numberValue > largestValue:
        largestValue = numberValue
    print(largestValue, numberValue)
print('After', largestValue)