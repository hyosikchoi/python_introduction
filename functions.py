# vararg

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


# key word arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# dictionary
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key} : {value}")

print_info(name = "Eve" , age = 32 , city = "Seoul")

info = {"name": "Karina" , "age" : "25" , "city" : "Seoul"}

print_info(**info)