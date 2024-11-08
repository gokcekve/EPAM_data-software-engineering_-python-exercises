#context manager example
class ContextManager:
    def __init__(self):
        print('__init__ method called')

    def __enter__(self):
        print('__enter__ method called')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit___ method called')


with ContextManager() as manager:
    print('inside with statement block')



#finite iterator example

class FiniteRepeat:
    def __init__(self, msg, max_count):
        self.msg = msg
        self.max_count = max_count
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        return self.msg

obj = FiniteRepeat("car", 5)
obj_iterator = iter(obj)
while True:
  try:
    message = next(obj_iterator)
  except StopIteration:
    break
  print(message)




#iterator pattern example

class Repeat:
    def __init__(self, msg):
        self.msg = msg

    def __iter__(self):
        return self

    def __next__(self):
        return self.msg

obj = Repeat("car")
obj_iterator = obj.__iter__()
while True:
  message = obj_iterator.__next__()
  print(message)



