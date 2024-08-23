# #pip install matlpotlib
# from matplotlib import pyplot as plt
# labels = ["python" , "java" , "Html" , "c++", "Javascript"]
# data = [95 , 80 , 65 , 80 , 95]
# explode = [0.0 , 0.0 , 0.1 ,0.0 , 0.0]
# plt.pie(data, labels=labels, explode=explode)
# plt.show()


# x = ['1' , '2' , '3']
# y = x[1] + x[2]
# print(y)

# i = 0
# while i<5:
      
def func(x = 1, y = 2):
       x = x + y
       y += 1
       print(x , y)
func(y = 2 , x = 1)