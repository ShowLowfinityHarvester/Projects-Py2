# These are school projects! Github page may be all cluttered until 2025 or 2026.

dictionary = {
  7: "first",
  3: "second",
  4: "third",
  8: "fourth",
  9: "fifth",
}

my_list = [int(n) for n in input("Enter in a number with spaces -> ").split()]

for x in my_list:

	if x in dictionary:
		print("Yes")
		
	else:
		print("No")
