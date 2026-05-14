# print numbers from 1 to 100 which is divisible by 3, 5 and both

for i in range(1, 101):
    if i % 3 == 0:
        print(i, " is divisible by 3.")
    if i % 5 == 0:
        print(i, " is divisible by 5.")
    if i % 3 == 0 and i % 5 == 0:
        print(i, " is divisible by 3 and 5 both.")
