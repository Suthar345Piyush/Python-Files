# function with *args
# Problem : write a function that takes variable number of arguments and returns their sum.

def sum_all(*args):  # it handles the arguments

    print(args)
    for i in args:
      print(i * 2)
    return sum(args)

print(sum_all(1 , 9))

# * astrick sign is compulsory and we can take any name with * it will rum properly






