# f= open("file.txt.txt",mode='r')
# f.seek(5)
# print(f.read())
# print("end",f.tell())
# f.close()

# f1= open("file.txt.txt",mode='w')
# f1.writelines('this is a new edit line')
# f1.writelines('India, officially the Republic of India is a country in South Asia')
# f1.writelines('It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world.')
# f1.writelines('Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest')
# f1.close()


# f2=open("newfile.txt",mode='r')
# print(f2.read())
# f2.close()
#
# f3=open("newfile.txt",mode="a")
#  f1.writelines('this is a new edit line')
#  f1.writelines('India, officially the Republic of India is a country in South Asia')
# # f1.writelines('It is the seventh-largest country by area, the second-most populous country, and the most populous democracy in the world.')
# # f1.writelines('Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest')


# d=open("second.txt","x")
# d.close()

# e=open("second.txt",mode='w')
# e.writelines('this is the first line')
# e.close()

import os
#os.remove("second.txt")

#os.remove("go.txt")

if os.path.exists("go.txt"):
    os.remove("go.txt")
else:
    print('no such file')

#os.rmdir for removing empty folder