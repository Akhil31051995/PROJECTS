# n=input('enter the no:')
# a=('%s'%(n))
# b=('%s%s'%(n,n))
# c=n+n+n
# print(a)
# print(b)
# print(int(a)+int(b)+int(c))


#exchange first and last letters of string

# s='Python'
# l=list(s)
#
# temp=l[0]
# l[0]=l[-1]
# l[-1]=temp
#
# new=''
# for i in l:
#     new+=i
# print(new)


#write a program to prompt the user for list of numbers ,for all values greater than 100 store 'over' instead
# l=input('enter the numbers:')
# num=[int(i) for i in l.split(",") if int(i)<=100 else 'Over' ]
#
# print(num)


# l=[]
# for i in input('enter the nos:').split(','):
#     if int(i)<=100:
#         l.append(i)
#     else:
#         l.append('over')
#
# print(l)



# store a list of first names and count the occurunce of 'a' within it
# count=0
# for i in input('enter the names:').split(','):
#     for j in i:
#         if 'a' in j:
#             count+=1
# print(count)





#write a python program to count the occurence of each word in a line of text
#sample input: the quick brown fox jumps over the lazy dog
#output:{'the':2,'quick':1,'brown':1,'fox':1,'jumps':1,'over':1,'lazy':1,'dog':1}


# text='AK loves to be a good boy always and AK loves to sleep and study and travel AK loves having good friends also'
# l=list(text.split(' '))
# d={i:0 for i in l}      # since dictionary doesnt allow duplicate keys iterations does not increase the number of keys
#
#
# for i in l:
#     d[i]+=1
#
# print(d)








#Get a string from input string where all occurence of the first character are replaced by $ except the first character
#eg: onion----> oni$n

# st='onion'
# s=list(st)
# for i in range(1,len(s)):
#     if s[0]==s[i]:
#         s[i]='$'
#
# print(s)
# new=''
# for i in s:
#     new+=i
#
# print(new)


#create a single string seperated with space from two strings by swapping the character at position 1
#str1='Hello'    str2='World'      create str3='Hollo Werld'

# str1=list('Hello')
# str2=list('World')
# temp=str1[1]
# str1[1]=str2[1]
# str2[1]=temp
#
# print(str1)
# print(str2)
# new1=new2=''
# for i,j in zip(str1,str2):
#     new1+=i
#     new2+=j
#
# str3=new1+' '+new2
# print(str3)


# write a python program to read two lists color-list1 and color-list2.print out all colors in color-list1 not contained in color-list2

# cl1=['red','green','orange','yellow','pink']
# cl2=['yellow','green']
#
# cl3=[i  for i in cl1 if i not in cl2]
#
# print(cl3)


#create a list of comma seperated colors from user and display first and last colors
#
# colors=[i for i in input('enter the colors:').split(',')]
# print(colors[0],colors[-1])


#count the no of characters in a string

# s='malayala manorama'
#
# d={i:0 for i in s}
#
# for i in s:
#     d[i]+=1
#
# print(d)



# accept a list of words and return the longest word

# l=list(input('enter the words:').split(','))
#
# print(max(l,key=len))



