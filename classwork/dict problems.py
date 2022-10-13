#convert two list into dict
# fruits=['apple','pineapple','grapes']
# colour=['red','yellow','violet']
# new={}
# #print(type(new))
# for i in range(len(fruits)):
#     new.update({fruits[i]:colour[i]})
# print(new)

#or
# name=['rose','jasmine','lotus','hibiscus']
# color=['red','white','pink','red']
# new={}
# for i in range(len(name)):
#     new[name[i]]=color[i]
# print(new)


#make two dict and combine
# a={'apple': 'red', 'pineapple': 'yellow', 'grapes': 'violet'}
# b={'name':'thar','colour':'black','year':2022}
# a.update(b)
# print(a)


#find physics marks

dic={'class':{'student':{'name':'mike','marks':{'physics':70,'history':80,'maths':100}}}}

a=dic['class']['student']['marks']['physics']   #single step using keys
# b=a['student']
# c=b['marks']
# d=c['physics']
print(a)




