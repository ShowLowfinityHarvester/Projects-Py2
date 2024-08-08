# These are school projects! Github page may be all cluttered until 2025 or 2026.

shape = input("What shape? -> ")
height = int(input("How tall is the shape? -> "))

shapes = {

"Triangle": 8,

"Circle": 15,

"Square": 10,

"Rectangle" : 12

}

shapes[shape] = height

print(shapes)