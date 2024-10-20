grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = tuple(students)
dict1 = {
students[0]: sum(grades[0]) / len(grades[0]), 
students[1]: sum(grades[1]) / len(grades[1]), 
students[2]: sum(grades[2]) / len(grades[2]), 
students[3]: sum(grades[3]) / len(grades[3]), 
students[4]: sum(grades[4]) / len(grades[4]),
}

dict2 = dict(sorted(dict1.items()))
dict2 = sorted(dict1.items())
print(dict2)

dict3 = {}
for key, value in dict2:
      dict3[key] = value
print(dict3)