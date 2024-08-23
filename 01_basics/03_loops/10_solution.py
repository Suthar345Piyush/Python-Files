# Exponential Backoff
# problem: impleament an exponential backoff stratgy that doubles the wait time between retirs , starting from 1 second , but stops after 5 retiers

import time

wait_time = 1 
max_retries = 5
attempts = 0


while attempts < max_retries:
  print("Attempt" , attempts + 1 , "_wait time" , wait_time , )
  time.sleep(wait_time)
  wait_time *= 2
  attempts += 1