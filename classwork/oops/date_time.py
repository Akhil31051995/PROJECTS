import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime('%A'))      #day
print(x.strftime('%B'))     #month
print(x.strftime('%a'))     #day in short form
print(x.strftime('%b'))

y=datetime.datetime(1995,5,31)
print(y)



