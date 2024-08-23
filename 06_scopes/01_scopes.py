username =  "chaiaurcode"


def func():
  # username = "chai"
  print(username)



print(username)
func()

x = 90 

# def func2(y):
#     z = x + y
#     return z


# result = func2(1)
# print(result)

# def func3():
#   global x # dont use this global practice this is not good 

#   x = 12

# func3()
# print(x)


def f1():
    x = 88
    def f2():
      print(x)
    return f2 # f2() iska mtlab hota hai ki execute karna
myResult = f1()
myResult() # here we executing f2


# this are called closurs or factory functions:

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(4))
print(g(4))
