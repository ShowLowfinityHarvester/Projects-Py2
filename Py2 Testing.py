# These are school projects! Github page may be all cluttered until 2025 or 2026.

first = int(input("First Number -> "))
second = int(input("Second Number -> "))
third = int(input("Third Number -> "))
fourth = int(input("Fourth Number -> "))
fifth = int(input("Fith Number -> "))

dictionary = { 7: first, 3: second, 4: third, 8: fourth, 9: fifth }

my_list = [int(n) for n in input().split()]

for x in dictionary.values():
    if x >= 100:
        print("This person is tall enough to ride.")
else:
    print("This person is too short to ride.")