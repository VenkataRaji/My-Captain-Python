"""  Python code to create a function called most_frequent that takes a string 
and prints the letters in decreasing order of frequency using dictionaries."""

def most_frequent(s):
  d={}
  #a sorted list is created out of a set to remove duplicates from the string
  sset=sorted(list(set(s)))
  #freq of each alphabet is found and is stored as a key-value pair in dict d
  for i in sset:
    v=s.count(i)
    #in dict key must be unique value
    #key--->alphabet,value-->freq
    d[i]=v
  #dd is the sorted dict of d based on the values
  #lambda is used for dict.values() sort
  #reverse--->desc order
  dd=sorted(d.items(),key=lambda kv:kv[1],reverse=True) 
  #dict dd (each key value pair is stored as a tuple) is iterated over 
  for i in dd:
    print(i[0],"=",i[1],end=" ")

s=input("Please enter a string:").lower()
most_frequent(s) 
