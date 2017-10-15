# 6_primality.py


#Aim is to find prime numbers using python

import math
import time

knowPrime = [2,3]

# Even numbers except 2 cannot be prime
# Any number divisible by an other prime number smaller that it cannot be prime



primeRange = 1000000

startTime = time.time()

for number in range(5,primeRange,2):
	
	isprime = True

	for smallprime in knowPrime:
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
		knowPrime.append(number)
	# print(knowPrime)

print("Time taken in seconds",time.time()-startTime)


print(len(knowPrime))



