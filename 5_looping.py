# 5_looping.py

#If else loop

Money = 1000
condition1 = True
condition2 = False


if condition1:
	#Execute this statement
	print("Condition 1 is execetued")
	Money =  Money * 1.5

if condition2:
	#Execute this statement
	print("Condition 2 is executed")
	Money =  Money + Money
else:
	print("Condition 2 is false so I am in here")
	Money = Money/3


# print(Money)



# numList = [1,2,3,4,5,6]


# # for number in numList:
# # 	print(number)

# #range(startPos, endPos, step)

# for number in range(100,150,3):
# 	print(number)


for num_out in range(100,110):
	print("------- Outer loop ---------",num_out)
	for num_In in range(1000,1010):
		if (num_In > 1005):
			break
		print(num_In)
	print("End of loop",num_out)




#While Loop

# count =0 

# while(count <5):
# 	print("The count is:", count)

# 	count = count+1



var =1
while var == 1:
	num = input("The square of the number is :")
	print(  int(num)**2)




