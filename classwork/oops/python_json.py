import json
x='{"name":"tom","age":20,"city":"kozhikode"}'


y=json.loads(x)        #parsing method

print(y["city"])


#convert python object to json

d={'name':'tom','age':25,'city':'kochi'}
y1=json.dumps(d)

print(y1)
print(type(y1))

print(json.dumps([1,2,'we','apple',56]))