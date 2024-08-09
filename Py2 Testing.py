# These are school projects! Github page may be all cluttered until 2025 or 2026.

while True:
    try: 
        value1 = int(input("How many people is Amanda bringnig? -> "))
        break
    except ValueError:
        print("Please enter in a number, not a name!")
while True:
    try: 
        value2 = int(input("How many people is Jane bringnig? -> "))
        break
    except ValueError:
        print("Please enter in a number, noT a name!")


group = { "Fred" : 12, "Jackson" : 15, "Sophie" : 20, "Amanda" : value1, "Jane" : value2, }

total = 0

for x in group.values():
	total += x
	
print(x)