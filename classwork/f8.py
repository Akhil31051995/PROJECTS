# Write a program that computes the net amount of a bank account based a
# transaction log from console input. The transaction log format is shown as
# following:
# D 100
# W 200
# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

def net_amount():

    deposit=[]
    withdrawl=[]
    net=0
    while True:

        d = int(input('deposit D:'))
        w = int(input('withdrawl W:'))
        deposit.append(d)
        withdrawl.append(w)

        net = sum(deposit) - sum(withdrawl)
        print(net)

        # if type(d)!=int and type(w)!=int:
        #     break
        # else:
        #


net_amount()