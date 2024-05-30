from threading import *
import time

class Demo2:
    def num(self):
        for i in range(1, 6):
            print("The number is", i)
            time.sleep(
                1)  # sleep function puts that thread on sleep for these seconds specified, for completion of execution

    def double(self):
        for i in range(1, 6):
            print("The double of the number is", i * 2)
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print("The square of the number is;", i * i)
            time.sleep(1)


obj = Demo2()
t1 = Thread(target=obj.num)
t2 = Thread(target=obj.double)
t3 = Thread(target=obj.square)

t1.start()
time.sleep(0.2)

t2.start()
time.sleep(0.2)

t3.start()
time.sleep(0.2)

t1.join()  # we use join to ensure these threads do not terminate before finishing their work
t2.join()
t3.join()

print("This is the main thread")