#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.


#assign value for previous number
previous_number = 1
#make the range function
for num in range(1, 10):
    sum = num + previous_number
    #overwrite previous number to keep the process going
    previous_number = num
    print(previous_number, num, sum)
