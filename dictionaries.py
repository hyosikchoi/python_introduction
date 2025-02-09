thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# access

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)


# add
thisdict["age"] = 10

# remove
thisdict.pop("model")
print(thisdict)