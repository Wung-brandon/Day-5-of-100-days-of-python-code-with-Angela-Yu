#method 1
#code to add all even numbers from 1 to 100
sum_num = 0
for num in range(1,101):
    if num % 2 == 0:
        sum_num += num
        #print(num)
    #sum_num += num
print(sum_num)

#method 2
all_num = 0
for number in range(2,101,2):
    all_num += number
print(all_num)
