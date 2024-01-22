previous_number = 0

for current_num in range(1, 11):
   sum = current_num + previous_number
   print(previous_number, current_num, sum)
   previous_number = current_num