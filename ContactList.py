answer = "y"
listOfContacts = []
while answer == "y":
    name = input("Add a contact? -> ")
    listOfContacts.sort(name)
    answer = input("Add more contacts? (y/n) -> ")