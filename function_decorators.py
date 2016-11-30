#!/usr/bin/python
def greet(name):
	return "hello"+ name
print greet("kesi")

greet_someone = greet
result = greet_someone("santosh")

def greet1(name):
	def greet2():
		return "hello"
	return greet2() + name
print greet1("k")

def call_function(function_object):
	other_name = "santosh"
 	return function_object(other_name) 

print call_function(greet)  
