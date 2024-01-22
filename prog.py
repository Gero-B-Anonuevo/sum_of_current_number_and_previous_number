#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


#assign value for previous number
previous_number = 0

#make the range function
for current_num in range(1, 11):
    sum = current_num + previous_number
    print(previous_number, current_num, sum)
    #overwrite previous number to keep the process going
    previous_number =current_num
