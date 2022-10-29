#print the matrix in spiral order
# matrix={{1,2,3,4},
#         {5,6,7,8},
#         {9,10,11,12},
#         {13,14,15,16}}

#out=12348121615141395671110


matrix=[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],
        ]
rowbegin=0
colbegin=0
rowend=len(matrix)
colend=len(matrix[0])
res=[]

for i in range (rowbegin,colend):

        res.append(matrix[0][i])
rowbegin+=1

for j in range(rowbegin,colend):
        res.append(matrix[j][colend-1])

colend-=1
rowbegin+=2
for i in range(colend-1,colbegin-1,-1):
        res.append(matrix[rowbegin][i])

for i in range(rowbegin-1,colbegin,-1):
        res.append(matrix[i][0])

colbegin+=1
rowbegin-=2
for i in range(colbegin,colend):
        res.append(matrix[rowbegin][i])

rowbegin+=1


for i in range(colend-1,colbegin-1,-1):
        res.append(matrix[rowbegin][i])

print(res)







