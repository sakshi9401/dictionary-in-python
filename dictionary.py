d1 = { "pen" : "blue",
       "pencil" : "natraj",
       "book" : "mathematics"}


d2 = d1.copy()

print(d2)

d1.pop("book")# to remove

print(d1)

d2["notebook"] = "classmate"# to add

print(d2)

d1.popitem()

print(d1)

#d1.clear() # here elements inside dict has been dlted

print(d1)

del d1 # dictionary is no more exist so it will show error

print(d1)