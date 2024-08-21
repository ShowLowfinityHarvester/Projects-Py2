# These are school projects! Github page may be all cluttered until 2025 or 2026.

answer = "y"
listOfContacts = []
while answer == "y":
    name = input("Add a contact? -> ")
    listOfContacts.append(name)
    answer = input("Add more contacts? (y/n) -> ")
listOfContacts.sort()
print(listOfContacts)
