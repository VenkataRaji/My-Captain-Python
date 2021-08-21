"""Finding the positive integers in a input given list and printing them in a single line"""
#input the list using map() and split the single line input by the delimiter "," to form a list
l1=list(map(int,input("Input: list1 =").split(",")))
#check if the lsit element is a positive integer if yes,the print it
for i in l1:
    if i>0:
        #end specifier is used to print the o/p in a single line while the loop runs and iterates over itself
        print(i,end=" ")
print()
"""Remove the negative integers from the given input list and return the list with only postive integers"""
l2=list(map(int,input("Input: list2 =").split(",")))
#check and remove the list element if negative
for j in l2:
    if j<=0:
        l2.remove(j)
print(l2)
