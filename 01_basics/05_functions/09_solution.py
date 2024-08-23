# Generator function with yield
#problem: write a generator function that yield even numbers up to a specified limit


def even_generator(limit):
    for i in range(2, limit + 1, 2):
      yield i


# yield means generate the value

for num in even_generator(10):
    print(num)