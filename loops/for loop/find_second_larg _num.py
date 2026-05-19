# find second largest number in a list

num_list = [10, 2, 6, 4, 8, 9, 11]
second_lar = num_list[0]
largest = num_list[0]

for i in num_list:
    if i > largest:
        second_lar = largest
        largest = i

    elif i < largest and i > second_lar:
             second_lar = i

print(second_lar)
    