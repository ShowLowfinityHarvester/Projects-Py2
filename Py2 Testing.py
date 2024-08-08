# These are school projects! Github page may be all cluttered until 2025 or 2026.

dinos = {}
dino = input("What dino -> ")
while True:
    try:
            dinoheight = int(input("Height? -> "))
            break
    except ValueError:
          print("Please enter in a number.")
          
newdino = [dino]