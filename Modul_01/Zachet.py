grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
dict_ = {}
students_list = list(sorted(students))
print(len(grades))
for k in range(len(grades)):
    dict_.update({students_list[k]: round(sum(grades[k])/len(grades[k]), 2)})
print(dict_)


