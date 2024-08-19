# These are school projects! Github page may be all cluttered until 2025 or 2026.

NMcityNames = ["Albuquerque", "Belen", "Curry", "LosAlamos", "LosRanchos", "RioRancho", "Cochiti", "Ruidoso", "Quay", "Hobbs", "Carlsbad"]
PickANum = int(input("Choose a number between 0-10: -> "))

InpCity = NMcityNames[PickANum]
letters = list(InpCity)
turns = 12

while turns != 0:
    myletter = (input("Input a letter: -> "))
    if myletter in letters:
      print("Letter is in word") 
      letters.remove(myletter) 
    else:
      print("-")
      turns -= 1
    
if turns == 0:
    print("Game Over")
    print(letters)
