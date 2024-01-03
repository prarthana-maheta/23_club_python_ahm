# # Data Types:
# #
# # int
# # string --- '' or ""
# # float 1.854
# # complex
#
# a='a+b+c+d+e+f'
# c=1j+1
# print(complex(c))
# s=str(2j+1+1j-3j)
# print(type(s))


# String
# -data type
# collection module
# "sequence of charaters"
# Immutable
# Ordered


# #complex()

 # collections:
# string: Ordered & Immutable Collection Of Characters
# """
s1='Students of this batch are going to rock the INDIAN software industry!'
# find the index of 'S'
# find the index of '!'
# find the index of 'I'
# find the index of third space that comes between this and batch

# # index: 	 0123456789..................
# # -ve index
# # :	 ......................................................987654321


# print(s1[-1])
# print(s1[69])
# # print(type(s1))
# print(s1)
# s1[0]='1'
# print(s1)
# # print(s1[len(s1)-1])
# s2=s1[::69]
# print(s2)
# s2=s1[:7:2]
# print(s1[:7:2])
# print(s1)
# print(s2)

s1='Students of this batch are going to rock the INDIAN software industry!'
# print(s1[15:6:-2])

print(s1[-5:-7:-2])
# start from 5 end should be till 15

s1='ROYAL TECHNOSOFT limited'

# ROYAL
# TECHNOSOFT
# limited
# ROYAL limited


# functions vs methods
# print(type(s1))
# print(len(s1)-1)


# # methods:
s1='rOYAL TECHNOSOFT limited'
print(s1)
print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.swapcase())
print(s1.title())

#
#
# s1='students .of this batch are going to rock the INDIAN software industry!'
#
#
# output: s1 ke first letters capitilize
#         indian in lower case
#         all the s1 string should in upper case
#         all the s1 string should be in lower case
#         software industry  in uppercase
