# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print (grades)
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list (students)
sorted_list = sorted(students_list)
print (sorted_list)

average = sum (grades [0]) / len (grades [0])
print (sorted_list [0], round (average,2))
average1 = sum (grades [1]) / len (grades [1])
print (sorted_list [1], round (average1,2))
average2 = sum (grades [2]) / len (grades [2])
print (sorted_list [2], round (average2,2))
average3 = sum (grades [3]) / len (grades [3])
print (sorted_list [3], round (average3,2))
average4 = sum (grades [4]) / len (grades [4])
print (sorted_list [4], round (average4,2))

average_score = dict (Aaron=average, Bilbo=average1, Johnny=average2, Khendrik=average3, Steve=average4)
print (average_score)