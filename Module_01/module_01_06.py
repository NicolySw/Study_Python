
Count_of_completed_homework = 12    # Количество выполненных ДЗ
Count_hours_spent = 1.5             # Количество затраченных часов
Course_Title = 'Python'             # Название курса
Time_for_one_task = Count_hours_spent / Count_of_completed_homework    # Время на одно задание
s = ('Курс: ' + str(Course_Title) + ', всего задач: ' + str(Count_of_completed_homework) + ', затрачено часов: ' +
     str(Count_hours_spent) + ', среднее время выполнения ' + str(Time_for_one_task) + ' часа.')
print('Курс:', Course_Title, ', всего задач:', Count_of_completed_homework, ', затрачено часов:',  Count_hours_spent,
      ', среднее время выполнения',  Time_for_one_task, 'часа.')
print(s)
print('Курс: ' + str(Course_Title) + ', всего задач: ' + str(Count_of_completed_homework) + ', затрачено часов: ' +
      str(Count_hours_spent) + ', среднее время выполнения ' + str(Time_for_one_task) + ' часа.')
