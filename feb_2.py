

# # # String 
# # # list
# # # tuple

# # dictionary
# # # set

# # # function Base
# # # OOPs

# # # brand="brand"
# # thisdict = {"&": "Ford",
# #             "model": [None, "abc"],
# #             "year": 1964
# #             # "brand":"tata"
# #             }

# # # Dictionaries are used to store data values in key:value pairs.
 
# # # A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# # thisdict ={
# #     1:"one",
# #     '2':'two'
# # }
# # print(thisdict)
# thisdict = {
#     "brand": "Ford",
#     "electric": False,
#     "year": 1964,
#     "colors": ["red", "white", "blue"]
# }
# # my=[1,2,3]
# # # print(thisdict)
# # # functions:
# # # print(type(thisdict))
# # print(len(thisdict))
# # print(tuple(thisdict))
# # print(dict(my))


# # # Accessing dict:

# thisdict = {
#     "brand": "Ford",
#     "mode": "Mustang",
#     "year": 1964
# }
# # print(thisdict["yea"])

# # print(thisdict.get("yea",2024))



# print(thisdict.keys())
# print(thisdict.values())
# print(thisdict.items())
# # #
# thisdict = {
#     "brand": "Ford",
#     "mode": "Mustang",
#     "year": 1964
# }
# # thisdict["example"] = "example"
# # thisdict.update({'1':"one",'2':'two'},three=3,three=3)
# # print(thisdict)

# # for keys in thisdict.keys():
# #     if keys == 'model':
# #         print(thisdict['model'])
# # print(thisdict.values().append("1"))

# # x=thisdict.items()
# # print(x)
# # for k,v in thisdict.items():
# #     print(k,v) 
# # # print(x[0])
# # for i,j in x:
# #     print(i)
# # counter=0
# # {
# #     'one':100,
# #     'two':200,
# #     'three':300
# # }


# # thisdict={
# #     1:1,
# #     2:2,
# #     3:3,
# #     4:4,
# #     5:5
# # }
# # list1=[]
# # for k,v in thisdict.items():
# #     list1.append(v*k)
# # # [1,4,9,16,25]
# # print(list1)

# # # add data to dict:
# # car = {
# #     "brand": "Ford",
# #     "model": "Mustang",
# #     # "year": 1964,
# #     # "year": "blue",
# # }
# # # #
# # # # x = car.items()
# # print(car) #before the change
# # car["year"] = None
# # print(car)  # after the change

# # car[0]=
# # # change values of dict:
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": None
# # }
# # thisdict["year"] = 2018
# # "bod"=
# # print(thisdict)

# # # update dict:
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.update({"year": 2020,"dob":"1235"},clr="red",)
# # print(thisdict)

# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # thisdict.update({"year": 2020})

# # thisidct={}


# # # remove items:
# # #
# # # # 1) pop()
# # thisdict = {
# #   "0": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # ans=thisdict.pop("model")
# # print(ans)
# # print(thisdict)
# # #
# # # # 2)popitem()
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)

# # # 3)del
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964

# }
# del thisdict
# # # print(thisdict)

# # # 4)clear()
# # thisdict = {
# #   "brand": "Ford",
# #   "model": "Mustang",
# #   "year": 1964
# # }
# # thisdict.clear()
# # print(thisdict)
# # # thisdict['a']=1
# # # print(thisdict)

# # # 5)copy()
# # # c=[2,3]
# # # a=[1,2]
# # # b=c.copy()
# # # del a
# # # print(b)


# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # mydict = thisdict.copy()
# # # del thisdict
# # # # print(thisdict)
# # # print(mydict)

# # # thisdict = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # mydict = dict(thisdict)
# # # print(mydict)

# # # 6) setdefault()
# # # car = {
# # #   "brand": "Ford",
# # #   "model": "Mustang",
# # #   "year": 1964
# # # }
# # # print(car.setdefault("color", "white"))
# # # print(car)
# # # print(car.setdefault("color", "black"))
# # # car.update({"color": "red"})
# # # car.update({"color": "pink"})
# # # print(car)
# # # print(x)

# # # 7) fromkeys()
# # x = ('key1', 'key2', 'key3')
# # y=(1,2)
# # # thisdict = dict.fromkeys(x,y)
# # thisdict=list(zip(x,y))
# # print(thisdict)

# # # nested dict:
# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : child1,
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }
# myfamily = {
#    "child1":None,
#   "child2" : child2,
#   "child3" : child3
# }
# # # #
# print(myfamily)


# print(myfamily.get("child2").get("name"))
# # thisdict.update({})
# # myfamily["child2"]["name"]['year']=2024
# # print(myfamily["child2"]["name"]['year'])
# # # child1 = {
# #     "name": "Emil",
#     "year": 2004
# }
# child2 = {
#     "name": "Tobias",
#     "year": 2007
# }
# child3 = {
#     "name": "Linus",
#     "year": 2011
# }
# myfamily = {
#     "child1": "abc",
#     "child2": "abc",
#     "child3": "abc"
# }

# # for key,value in myfamily.items():
# #     print(key)
# #     # myfamily[key]="abc"
# #     # print(myfamily)
# #     # print(value)
# #
# #     if "child1" == key or "child2" in key :
# #         print("found")
# #
# # if "child1" in myfamily.keys():
# #     print("yes")

# l1=['a', 'b', 'c', 'd', 'e', 'f']
# l2=[1, 2, 3, 4, 5,6,7]
# l3=[7,8,9,0,1,2]

# # print(dict(zip(l1,l2)))

# input={'one':1,"two":2,"three":3}
# # print(dict(zip(input.values(),input.keys())))

# dict1={}
# for k,v in input.items():
#     # dict1[v]=k
#     dict1.update({v:k})

# print(dict1)
# output={1:'one',2:'two',3:'three'}
# myfamily = {
#     "child1": "abc",
#     "child2":
#         {"abc":1},
#     "child3": "abc"
# }
# # myfa=myfamily
# # myfam=myfamily.copy()
# # myfamily['change']=1
# # print(myfa)
# # print(myfam)
# for i,j in myfamily.items():
#     if isinstance(j,dict):
#         print("yes")


# Write a Python program to filter a dictionary based on values.
# Original Dictionary:
a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165,
 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
dict1={}
for k,v in a.items():
    if v>= 170:
      dict1[k]=v
      # dict1.update({k:v})
      
# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output:
# {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

# input_str = input()
# dict1={}
# for i in input_str:
#     dict1[i]=dict1.get(i,0) + 1
# print(dict1)
      

#  Write a Python program to filter the height and weight of students,
#        which are stored in a dictionary.
# Original Dictionary:
# student={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65),
# 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
      

# Write a Python script to concatenate the following
# dictionaries to create a new one.

# for i in (dict1,dict2,dict3):
#    dict4.update(i)
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#  Write a Python program to match key values in two dictionaries.
# Sample dictionary: 
      x={'key1': 1, 'key2': 3, 'key3': 2}, 
      y={'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y
      # print(f"{dict1['key']}")
a=1
b=2
print(f"the value of a is {a} and the value of b is {b}")
for k,v in x.items():
   for i,j in y.items():
      if k==i and v==j:
        print