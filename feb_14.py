# # String 
# # list 
# # tuple
# # dict
# # set

# # Collections in Python
# """
# ordered      iMMUTABLE   string
# Ordered     Mutable     list        []
# Ordered     Immutable   tuple       ()
# Unordered   Mutable     set         {}
{1,3,4,5,}

# Two special collections:
# strings: Ordered & Immutable collections of characters              " "/ ' '
# dictionaries: Unordered & Mutable collections of key-value pairs    {}
# """

# # Sets are used to store multiple items in a single variable.

# # Set is one of 4 built-in data types in Python used to store collections of data, 
# # the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# # A set is a collection which is unordered, unchangeable*, and unindexed.

# # * Note: Set items are unchangeable, but you can remove items and add new items.

# # Sets cannot have two items with the same value.

# # Once a set is created, you cannot change its items, but you can add new items.
# s2=[1,2,3,4,4,5,6]
# d1={
#     '1':2,
#     '2':2
# }
# s1 = {21,1,3,4,21}
# print(s1)
# print(type(s1))
# print(set(d1))

# # Unordered means:
# """
# NO indexing
# NO Accessing through index
# NO Slicing
# """
# # print(s1[2])

s2 = {15, 7, -17, 15, 0.78, 6, 15, 18, 15.47, 15, 98.2, 0, 15}
# """
# print(s2)
# print(type(s2))
# print(len(s2))
# print(min(s2))
# print(max(s2))
# print(sorted(s2,reverse=True))
# print(sorted("python"))
# """
# # s2 = {15, 7, -17j+1, "15", 0.78, 6, "15", 18, 15.47, "15", 98.2, 0, "15"}

# thisset = {"apple", "banana", "cherry", True,0,False ,1, 2}
# print(thisset)

# thiset={"apple", "banana", "cherry",}
# print(thiset)
# null or none =-1
# true=1
# false=0
# # s1 = {15, 7, -17, 15, 0.78, 6, 15, 18, 15.47, 15, 98.2, 0, 15}
# # # empty_set = {1}
# # empty_set = set("1")
# # print(len(empty_set))
# # print(type(empty_set))
# """
# empty_set = {}
# empty_set = set()
# print(len(empty_set))
# print(type(empty_set))

# # Example of a dictionary:
# result = {"Vedangi":95, "Khush":59, "Dharmangi":85}

# mix_set  = {"Paneer Butter Masala", 3, "Veg Handi", 3, "Butter Nan", 2, "Cheese Nan", 2, "Plain Roti", 0.5}

# # Another way to create any collection:
# student_1 = list("Krushnam")[]
# student_2 = tuple("Krushnam")()
# student_3 = set("Krushnam"){}
# print(student_1)
# print(student_2)
# print(student_3)

# myList = [1,2,3,4,5,6]
# mySet = set(myList)
# print(mySet)
# """
# # myList = [1,2,3,4,5,6]
# # mySet = set(myList)
# # print(mySet)

# # thisset = set(("apple banana"))
# # print(thisset)
# # Note: the set list is unordered, so the result will display the items in a random order.

# # set methods:
# # s1 = {15, 7, -17, 0.78, 6, 18, 15.47, 98.2, 0}
# # print(s1[0])

# # 1. add items to set 
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# thisset.add(" orange")
# print(thisset)

# # 2. add set to set
# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "apple", "papaya"}
# thisset.update(tropical)
# print(thisset)

# # 3. add any iterable
# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)

# # # 4. remove item from set with remove()
# thisset = {"apple", "cherry"}
# thisset.remove("apple")
# print(thisset)

# # 5. remove item from set with discard()
# thisset = {"apple", "cherry"}
# ans=thisset.discard("banana")
# print(ans)

# # 6. remove item from set with pop()
# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x) #removed item
# print(thisset) #the set after removal


# # 7. remove item from set using clear()
# # thisset = {"apple", "banana", "cherry"}
# # thisset.clear()
# # print(thisset)

# # 8. remove item using del
# # thisset = {"apple", "banana", "cherry"}
# # del thisset
# # print(thisset)




# # Join two set
# # You can use the union() method that returns a new set containing all items from both sets, 
# # or the update() method that inserts all the items from one set into another:


# # 9. join two set and return new set using union()
# set1 = {"a", "b" , "c"}
# set2 = 123
# set1.union(set2)
# print(set1.union(set2))


# # 10 join two set and update in one using update()
# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)


# # 11 The intersection() method will return a new set, that only contains the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)


# # 12 The intersection_update() method will keep only the items that are present in both sets.
# x = {"apple", "banana", "cherry"}
# print(x)
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

# # 13 The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)

# # 14 The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

# # thisset = {"apple", "banana", "cherry",  1,True, 2,False,0}
# # print(thisset)


# # functions:
# # 1. all()-return true if all elements are true
# # s1={True,-1}
# # print(all(s1))

# # 2. any()-return true if any of the element is true
# # s1={0,False}
# # print(any(s1))

# # 3. sorted()
# # s1={2,4,1}
# # # [2,4,1]
# # s2=sorted(s1)
# # s2.update(3)
# # print(s2)


# # min(s1)
# # max()
# # sum()



# # s1.add(500)
# # s1.clear()
# # del s1

# # s2 = s1.copy()
# # s3 = s1

# # print("s1 =", s1)
# # print("s2 =", s2)
# # print("s3 =", s3)

# # s1.discard(15.47)
# # s1.discard(15.47)
# # print("s1 =", s1)
# # s1.remove(98.2)
# # s1.remove(98.2)
# # print("s1 =", s1)

# # print(s1.pop())

# # s2 = {101, 201, 301, 401, 6}
# # s1.update(s2)
# # print("length of s1 =", len(s1))
# # print("s1 =", s1)
# # print("s2 =", s2)


# # Input three numbers
# num1 = 12
# num2 = 25
# num3 = 52


{'mam', 'madam','121'}

# # example3: pallindrome checking yes or no?
# # example4: one output with common 
#element second with not common elements






# # s1={"mam","122"}
# # for i in s1:
# #     if i == i[::-1]:
# #         print(f"{i} is pallindrome")
