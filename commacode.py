import os, sys

old_list = ['Peanut Butter',"Celery", "Jam", "Garlic", "Apples"]
new_list=[]

for i in range(len(new_list[:-1])):
    new_list.append(i)
    new_list.append(',')

new_list.insert(len(new_list)-1, 'and')
print(str(new_list))

