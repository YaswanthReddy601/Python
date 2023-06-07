import file1

class C1:
    def my_func(self):
        func = "from my_func we got "+file1.func()
        print(func)


c = C1()
c.my_func()