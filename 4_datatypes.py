# 4_datatypes.py

List_empty = []


List1 = [1,2,3,4,5,-90] #List of numbers

List2 = ["MBA","BE","Master of Science"]






#Membership check
isMember = -900 in List1

# print(isMember)

#Slicing

numbers = [i for i in range(100)]

# print(numbers[50:70])



# print(len(numbers))



# numbers.append(1)
# print(numbers)

# #Counting the number of instances in the list
# print(numbers.count(1))



# del(numbers[-1])
# print(numbers)


# del(numbers[99])
# print(numbers)



#Dictionary

suite = {1:"Hearts", 2:"Spade", 3:"Diamond" ,4:"Clubs" }
rank = {"1":"Aces","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9","10":"10","11":"Jack","12":"Queen","13":"King"}
hand = {"0":"Nothing in hand","1":"One pair","2":"Two pairs","3":"Three of a kind","4":"Straight","5":"Flush","6":"Full house","7":"Four of a kind","8":"Straight Flush","9":"Royal Flush"}



dict1 ={}

dict1["Greetings"] = "Welcome to python "
dict1["numberList"] = [1,2,3,4,5,6,7,8,9,10]


# print(dict1)

# print(dict1["Greetings"])
# print(dict1["numberList"])


# print(dict1.get("numberList",False))






# del(dict1["numberList"])
# print(dict1)



# rank[14]="Jokker"


# print(rank)






Address = {
	"House_no":25,
	"city":"Helsingør",
	"PostCode": 3000,
}


person = {
	"FistName":"Dharani",
	"LastName":"AP"
}

# print(person)


person["Address"]= Address
person["scores"] = [1,2,34,5,6]

# print(person)




for (key,value) in person.items():
	print(key,"-->",value)


# print(person.items())
# print(len(person["Address"]))





















