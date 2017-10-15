# 7_functions_fileOperations.py

import math

def primeTest(primeRange):
	knowPrimes = [2,3]

	for number in range(5,primeRange,2):
		
		isprime = True

		for smallprime in knowPrimes:
			if number % smallprime  == 0:
				isprime = False
				break
			else:
				if smallprime > math.sqrt(primeRange):
					break
				else:
					pass
				# pass

		if isprime == True:
			knowPrimes.append(number)
		# print(knowPrime)




	print(len(knowPrimes))




rangeList = [100,1000,10000,100000]

# for i in rangeList:
# 	primeTest(i)


def functionWithArg(arg1,arg2):
	# print(arg1*arg2)
	return arg1*arg2


result = functionWithArg(100,120)
print(result)


def functionWithMultipleArg(*args):
	result = 0
	for arg in args[0]:
		result = arg+result
	return result

args = [i for i in range(100)]

print(functionWithMultipleArg(args))

