#dictionary is nothing but key value pair
d1 ={}
print(type(d1))
d2 = {"rose" : "flower",
        "chocolate" : "sweet",
        "maths" : "operations",
        "append" : "add in lst",
      "friends" : { "b":"alex", "g":"nick", "f":"john"}}
print(d2)
print(d2["rose"])
d2['sakshi'] = "witness"
print(d2)
print(d2["friends"])
print(d2.get('chocolate'))
d2.update({"climate" : "rainy"})
print(d2)
print(d2.keys())
d3 = d2
print(d3)
del d2["append"]
print(d2)
print(d3.items())
