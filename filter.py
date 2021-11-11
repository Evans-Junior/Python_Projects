grades =['A','B','F','A']

def remove_fails(grade):
    return grade!='F'

#print(list(filter(remove_fails,grades)))

# filter_grades =[]
# for grade in grades:
#     if grade != 'F':
#         filter_grades.append(grade)
# print(filter_grades)

print([grade for grade in grades if grade != 'F'])