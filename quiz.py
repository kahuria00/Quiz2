

def comp():
	num=[100,110,120,130,140,150]
	comp_num=[number % 3 for number in num]
	return comp_num

def sorted():
	a=['apple','banana','mango']
	b=['avocado','peach','orange']
	c=['pineapple','lemon']
	d=a+b+c
	d.sort()
	print(d)

def  divisible_by_3(n):
	 for number in range(1,n):
	 	print(number//3)

def flat():
	x = [[1,2],[3,4],[5,6]]
	x.len()
	
	

def small():
	d=[23,45,50,25,56,12,26]
	print(min(d))

def remove():
	x = ['a','b','a','e','d','b','c','e','f','g','h']
	x.pop()
	print(x)

def squares():
	y=dict()
	for x in range(149,159):
		y[x]=x*x
		print(y)

def message():
	students = [{'age': 19, 'name': 'Eunice'}, {'age': 21, 'name': 'Agnes'}, {'age': 18, 'name': 'Teresa'}, {'age': 22, 'name': 'Asha'}]
	print("Hello {},you were born in year{}."). format(students["name"],students[2019-"age"])









