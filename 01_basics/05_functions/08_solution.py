# function with **kwargs
#Problem : create a function that accept any number of keyword arguments and prints them in the format key: value

# kwargs = keywords  arguments

def print_kwargs(**kwargs):
    for key ,value in kwargs.items():
      print(f"{key}: {value}")
 #  print(f"{}") this is format string method
 

print_kwargs(power="webs", name="spiderman" )
# we can flip them from one side to anoyher side
print_kwargs(power="webs")
print_kwargs(name="spiderman")


