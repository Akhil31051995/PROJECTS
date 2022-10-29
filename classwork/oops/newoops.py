class calc:
    def add(self, a):
        print("number is ", a)

    def add(self, a, b):
        n = a + b
        print("addition of 2 numbers is:", n)

    def add(self, a, b, c):
        n = a + b + c
        print("addition of 3 numbers is:", n)


c = calc()
c.add(7, 6)