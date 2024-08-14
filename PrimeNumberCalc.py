# These are school projects! Github page may be all cluttered until 2025 or 2026.

number = int(input("What number do you want to check? -> "))

# print(range(number))
factors = []
for x in range(2, number):
	if number % x == 0:
		factors.append(x)
		
        
        
if len(factors) > 0:
	print(factors)
else: 
	print(f"{number} is a prime number")