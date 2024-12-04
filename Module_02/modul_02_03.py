my_list = [42, 69, 322, 13, 0, 99, 5]
k = 0
while my_list[k] >= 0 and k < len(my_list):
    if my_list[k] != 0:
        print(my_list[k])
    k += 1
    if k >= len(my_list):
        break


