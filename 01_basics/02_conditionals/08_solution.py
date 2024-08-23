# Password strength Checker
# problem: check if a password is "Weak", "medium" , "strong". criteria: <6chars(weak), 6-10char(medium) , >10 (storng)


# password = "Medium"
# character = 9

# if character <=6:
#   password  = "weak"

# elif character <=10:
#   password = "medium"

# else:
#   password = "strong"

# print("Your password strength is: " , password)


password = "P@ssword"
password_length = len(password)


if len(password) < 6:
 strength = "Weak"

elif len(password) <= 10:
  strength = "Medium"

else:
  strength = "Strong"


  print("password strength is: " , password)
  
  
  
  
  
