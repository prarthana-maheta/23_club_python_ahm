# # while:
# i=1
# while True:
#     print(i)
#     i +=1
#     if i == 5:
#         pass
#         # print("------------------")
#         # break

# # if i ==1:
# #     for i in range(1,10):
# #         print(i)
    
# # calculate the sum of five numbers entered by user using while loop
    

# tuple --- immutable --- ordered --- (12,3)

# thistuple = ("apple", "banana", "cherry")
# thistuple = ["apple", "banana", "cherry"]
# print(type(thistuple))


# # Ordered
# # When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# #
# # Unchangeable
# # Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
# #
# # Allow Duplicates


# # print(type(thistuple))
# # print(len(thistuple))
# #
# # thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# # tuple(thistuple)
# # print(thistuple[2:5:-1])

# # check if present
# thistuple = ("apple", "cherry", "apple")
# if "apple" in thistuple:
#     print("Yes, 'apple' is in the fruits tuple")
# if "cherry" in thistuple:
#     print("yes, 'cherry' in ")

# for i in (1,2,3):
#     print(i)



# # change tuple value update tuple
# #
x = ("apple", "banana", "cherry")
y =list(x)
y[0]="kiwi"
print(tuple(y))
# y = list(x)
# # print(y)
# # y=[x]
# # print(y)
# #
# # y[0] = "kiwi"
# #
# # print(y)
# # x = tuple(y)
# #
# # print(x)


# # add items to tuple
# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)
# print(thistuple)

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)

# tuple1 = ('abc','royal','pvt','ltd','Mango')
# find min and max of this tuple
# remove all the elements from 'pvt'
# add ['apple','banana'] to tuple1


# # # unpack tuple
# fruits = ["apple", "banana", "cherry"]
# # #
# green, yellow, red = fruits
# # #
# print(green)
# print(yellow)
# print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

green, yellow, *red = fruits
# #
print(green)
print(yellow)
print(red)

# # tuple method
# # count,index



# #loop through tuple
# # thistuple = ("apple", "banana", "cherry")
# # for x in thistuple:
# #     for i in x:
# #         print(i)
# #   print(x)

# # thistuple = ("apple", "banana", "cherry")
# # for i in range(1,len(thistuple),2):
# #   print(thistuple[i])


# # while loop in tuple

# # thistuple = ("apple", "banana", "cherry","abc")
# # i = 0
# # while i < len(thistuple):
# #     print(thistuple[i])
# #     i = i + 1


# # join two tuple 
tuple1 = [1,2,3]
tuple2 = [1, 2, 3]

tuple3 = tuple1 - tuple2
print(tuple3)

# l1=["hello"]
# print(l1+l1)

# # Multiply two tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)





# # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# #
# # x = thistuple.count(5)
# #
# # print(x)
# #
# # thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# #
# # x = thistuple.index(8)
# #
# # print(x)
