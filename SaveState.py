# var examples

Name = "Name"
Age = 24
FavYear = "2012"

print(Name)
print(Age)
print(FavYear)

# input

VehModel = input('What model of vehicle do currently have? be sure to include the year: ')

print("You said you have a " + VehModel+ ". Looking at parts for you!")

# Syntax and comments

# print nombre <- This will not print!!!!

print("Under Development!")

#           |
# data types V

# "32" is a string!
# 32 (no quotes) is an integer!
# 32.0 is a float!

Temp = -23
cars = 2

# converting data types

# Integer

NumberOfFord = 15
NumberOfFord = int("15")
print(NumberOfFord)

#String

NumberOfFord = 2340
NumberOfFord = str(2340)
print(NumberOfFord)

# Float

NumberOfFord = 1293
NumberOfFord = float(1293)
print(NumberOfFord)

# Converting inputs

ManufacturePlant = int(input("How many cars are in the Plant? "))
FordCars = ManufacturePlant + 5
print(FordCars)

# Concatenation Exs

Car1 = "Car Make is"
Car2 = "2002 "
Car3 = "Ford Focus"
Car4 = Car1 + Car2 + Car3

print(Car4)

# Extra Code

MakeYear = '2002'
MakeYear = int("2002")
Miles = 142527
Engine = 5.68
Engine = int(5.68)

print(MakeYear)
print(Engine)

WheelPSI = 41
WheelPSI = float(41)
print(WheelPSI)

# wh?

c = 4 % 4
print(c)

# String Methods

string1 = "sissy liberals"
print(string1[4:9])
print(string1.split())
print(len(string1))
print(string1.find("s"))

# check strings

string1 = "Firetrucks are red"
Check = "red" in string1
print(Check)

# conctenating numbers

string1 = "The total milage of the car you are looking to by is {} miles."
milage = 210872
print(string1.format(milage))

string1 = "The total milage of the car you are looking to by is {} miles. Your car is expected to run without breaking down for about {} more miles."
milage = 210872
RemainingMilage = 500
print(string1.format(milage, RemainingMilage))

# lists

AlbumsTurning10YrsOld = ["V", "Whatever else came out in 2014"]
print(list)

# If statements

AvaTyAge = 28
RandoAge = 17

if RandoAge > 18:
    print("You are in the clear")
else:
    print("Exposed!!!")

# Conditionals (Buggy!)

age = int(input('What is your age? -> '))
license = True
if age >= 16 and "license" == True:
    print("You are old enough to drive")
else:
    print("You are not able to drive")

# Else if statements

coins = 10

if coins > 20:
    print("You have more than enough to buy a puppy")
elif coins == 20:
    print("You have exactly enough to buy a puppy")
else:
    print("you do not have enough to buy a puppy")

    # String Methods

    string_1 = "call me maybe"
print(string_1.upper())
print(string_1.lower())
print(string_1.replace("always", "Never"))

# If statement in a for loop

Worstfoods = ["Mushroom", "Apple", "Brocoli", "Steak", "Fish"]
for x in Worstfoods:
	if Worstfoods == "Mushroom":
		print(x + " is gross")
	elif Worstfoods == "Brocoli":
		print(x + " is gross")
	elif Worstfoods == "Fish":
		print(x + " is gross")
	else:
		print(x + " is pretty good")

# Adding to lists

smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies", "roses", "new car", "sweaty feet", "peach"]

smells.append("apples")
print(smells)

smells.extend(["other smells", "should", "go here"])
print(smells)

smells.insert(3, "fresh cut spring grass")
print(smells)

# Removing List

harvest = ["pumpkins", "apples", "corn", "squash", "carrots"]
harvest.remove("squash")
appleseason = harvest.pop(1)
print(harvest)
print("it's time to pick some " + appleseason+ " this season!")

# Lists Continued

activities = ["movies", "skating", "bowling", "laser tag", "escape room", "trampoline park", "library"]

print(activities[0:3])

activities[6] = "water park"

print(activities)

print(len(activities))

# While loops

number = 1
while number <= 50:
    print(number)
    number += 1

# Functions

def race():
    print("This guy won the race!")
    
race()

# Function parameters

def race(Status):
    print("You completed all laps and finished in " +Status+ " place.")
    
race("1st")
race("3rd")
race("4th")

# Multiple parameters in a fuction

def race(Status, CarType):
    print("You completed all laps and finished in " +Status+ " place in your " + CarType + ".")
    
race("1st", "1996 Chevy Impala ZLT V8")
race("3rd", "2001 Mini Cooper S")
race("4th", "2002 Ford Focus RS")

# Python dictionaries

mountains = {
    "Timpanogos": 5,
    "Everest": 10,
    "Kilimanjaro": 6,
    "Vesuvius": 7,

}

print(mountains)
print(mountains["Vesuvius"])
mountains["Kilimanjaro"] = 8

print(mountains)

# Adding to and removing from dictionaries

goals = { "piano" : 5, "run" : 3, "paint" : 2, "serve" : 7, "homework" : 7}

goal = input("goal to remove? -> ")


goals["race"] = 8 # adds

goals.pop(goal) # Removes


print(goals)

# Dictionaries continued

coins = { "pennies" : 1, "nickels" : 2, "dimes" : 3, "quarters" : 4,}

coins["silver dollar"] = 5

coins.pop("pennies")

print(coins)
print(len(coins))

# Looping through a dictionary

measurement = {"length": 10, "width": 5, "depth": 3}
for x in measurement.values():
    print(x)

# Loops continued

ride = { "Jane" : 99, "Andy Candy" : 135, "Brodi" : 92, "Jolene" : 121, "Kyrene" : 102 }

for x in ride.values():
    if x >= 100:
        print("This person is tall enough to ride.")
else:
    print("This person is too short to ride.")