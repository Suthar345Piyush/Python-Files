# Movie Ticket Pricing:
# Movie tickets are priced based on the age: $12 for adults(18 and over), $8 for children.Everyone  gats a $2 discount on wednesday.




age = 25
day = "Wednesday"

price = 12 if age>=18 else 0

if day == "Wednesday":
  price = price - 2

print("TIcket price for you is $" , price)
