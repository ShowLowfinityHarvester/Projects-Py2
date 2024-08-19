number = int(input("What number do you want to check? -> "))

mult_total = 1
sum_total = 0

for x in range(1, number+1):
   mult_total *= x
   sum_total += mult_total

print(sum_total)
