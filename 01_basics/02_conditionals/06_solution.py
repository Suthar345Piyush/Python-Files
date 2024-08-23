#  Transportation Mode solution
# Porblem: Choose a mode of transportation based on the distance (<3: walk , 3-15km : Bike , >15km : car) 


distance = 30

if distance < 3:
  transport = "Walk"

elif distance <= 15:
  transport = "Bike"

else: 
  transport = "Car"

print("Ai recommends you the transport with: " , transport)
