smallest = None
print("Before:", smallest)

for itervar in [13, 41, 12, 9, 74, 15]:
    print("Loop:", itervar, smallest)
    if smallest is None or itervar < smallest:
        smallest = itervar
print("Smallest:", smallest)