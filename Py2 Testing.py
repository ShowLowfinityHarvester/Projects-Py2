# These are school projects! Github page may be all cluttered until 2025 or 2026.

while True:
    try: 
        value1 = int(input("pick a number -> "))
        break
    except ValueError:
        print("Please enter in a number, not a name!")
while True:
    try: 
        value2 = int(input("Pick another number -> "))
        break
    except ValueError:
        print("Please enter in a number, noT a name!")


group = { 3 : 10, 5 : 3, 10 : 6, 4 : 30, value1 : value2 }



total = 0
for x,y in group.items():
	total += x * y

print(total)

