
lCalifications = []

iCalification = 0
while iCalification != -1:
    iCalification = int(input("Enter a calification (or -1 to finish): "))
    if iCalification != -1:
        lCalifications.append(iCalification)

print("The califications are:", lCalifications)

for pos01 in lCalifications[:3]:
    print("The first 3 positions", pos01)

for pos02 in lCalifications[-3:]:
    print("The last 3 positions", pos02)

for pos03 in lCalifications[2:7]:
    print("Between", pos03)    