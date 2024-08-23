# Multiplication table printer
# problem : print he multiplication table for a given number up to 10 but skip the fifth iteration

number = 3

for i in range(1 ,11):
  if i == 5:
    continue 
  print(number , 'x' , i , '=', number*i )

# yaha pe hamne detection kara hai , continue ek keyword hain jo ki us itreation ko bahar nikal dega

