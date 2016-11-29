#!/usr/bin/python
def add1():
	print "i m in addition"

def add2(a,b):
	return a+b

#add1()
addition_result = add2(3,4)
def div(c,d):
	return c/d
print div(addition_result,2)

def name():
	return "krishna" 
print name()

def full(first_name,last_name):
	print first_name,last_name

first_name = "krishna reddy"
last_name ="kesireddy"
full(first_name,last_name)

def add3(a,b,c,d,e):
	f = a+b+c+d+e
	return f
print add3(5,6,7,8,9)

def add4(a,b,c,d,e):
	f = a	
	g = a+b	
	h = a+b+c
	i = a+b+c+d
	j = a+b+c+d+e
	k = f+g+h+i+j
	return k

def add5(*args):
	temp = 0
	print args
	for value in args:
		temp = value+temp
		final_result = temp+temp
	return final_result
print add5(5,6,7,8)	
